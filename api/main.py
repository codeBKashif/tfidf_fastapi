import uvicorn
from app import app
from models import create_tables


if __name__ == "__main__":
    create_tables()
    uvicorn.run(app, host="0.0.0.0", port=8000)