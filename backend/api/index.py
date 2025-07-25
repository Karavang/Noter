# backend/api/index.py
from backend.main import app  # імпортуємо FastAPI app
from mangum import Mangum

handler = Mangum(app)  # адаптер для AWS Lambda / Vercel


def handler(event, context):
    asgi_handler = Mangum(app)
    return asgi_handler(event, context)
