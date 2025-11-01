# TF-IDF Search

This application is built with Python FastAPI and NextJS.

## Installation

Run the backend application inside `/api` folder

```bash
cd api
Docker build -t tfidf_fastapi .
Docker run -p 8000:8000 tfidf_fastapi
```

Now go to `/frontend` directory, install dependencies, and run application

```bash
cd frontend
npm install
# to run as dev server
npm run dev
# to build artefacts for production
npm run build
```

now, go to [http://localhost:3000](http://localhost:3000)

## Considerations

Currently it is using SQLite for assignment purpose, for production level we can consider following considerations.

- Use PSQL for better row level locking, currently SQLite locks the table while inserting and updating document frequencies.
- Calculate IDF and store against each term by using some background task or scheduled cron, to scale search when dealing with large document list.
- Use Alembic migrations.
- Use separate docker container for PSQL to run locally.
