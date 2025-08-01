from fastapi import FastAPI
import logging

from config import API_TITLE, API_DESCRIPTION, API_VERSION, HOST, PORT
from routes import router

logging.basicConfig(level=logging.INFO)

app = FastAPI(
    title=API_TITLE,
    description=API_DESCRIPTION,
    version=API_VERSION
)

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=HOST, port=PORT) 