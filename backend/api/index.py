# backend/api/index.py
from backend.main import app
from mangum import Mangum

# створюємо один екземпляр адаптера
asgi_handler = Mangum(app)


# експортуємо handler як функцію, яку викличе Vercel
def handler(event, context):
    return asgi_handler(event, context)
