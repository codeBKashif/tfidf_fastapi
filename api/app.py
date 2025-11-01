from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from libs import logger
from controller import router

logger.info("Starting the application")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)