from fastapi import APIRouter

order_router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@order_router.get('/')
def hello():
    return {"message": "Hello from auth routes!"}



