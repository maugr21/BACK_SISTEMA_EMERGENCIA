from fastapi import APIRouter

router=APIRouter()

@router.get("/")
def say_hello():
    print
    return {"message":"hello world"}