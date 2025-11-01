import math
from sqlalchemy.dialects.sqlite import insert
from models import DocumentStat, TermStat, Document, get_session
from sqlalchemy import func
from .logger import logger

def check_if_document_exists(name: str) -> bool:
    with get_session() as session:
        doc =  session.query(Document).filter_by(name=name).first()
        if doc:
            return True
        return False

def ingest_new_document(name: str, term_freq: dict[str, int]) -> dict[str, float]:

    with get_session() as session:
        try:

            new_doc = Document(name=name)
            session.add(new_doc)
            session.flush()

            for token, freq in term_freq.items():
                term_stat = TermStat(document_id=new_doc.id, term=token, tf=freq)
                session.add(term_stat)
            
            for term in term_freq.keys():
                stmt = insert(DocumentStat).values(term=term, doc_freq=1)
                stmt = stmt.on_conflict_do_update(
                    index_elements=[DocumentStat.term],
                    set_={"doc_freq": DocumentStat.doc_freq + 1}
                )
                session.execute(stmt)
                
            session.commit()
        except Exception as e:
            session.rollback()
            logger.error(f"Error ingesting document: {e}")
            raise e


def search_top_k(term: str, k: int):

    with get_session() as session:

        df_entry = session.query(DocumentStat).filter_by(term=term).first()
        if not df_entry:
            return []

        df = df_entry.doc_freq
        N = session.query(func.count(Document.id)).scalar()
        idf = math.log(N / df)

        logger.info(f"df: {df}, N: {N}, idf: {idf}, term: {term}")

        results = []    
        term_stats = session.query(TermStat).join(Document).filter(TermStat.document_id == Document.id).filter(TermStat.term == term).all()
        for stat in term_stats:
            tf = stat.tf
            score = tf * idf
            results.append((stat.document.name, score))

        logger.info(f"results: {results}")

        return sorted(results, key=lambda x: x[1], reverse=True)[:k]