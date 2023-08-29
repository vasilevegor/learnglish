from fastapi import FastAPI

from .schemas import Word, UserCreate
from .crud import register_user
app = FastAPI()


@app.get("/word/{id}")   
async def get_word():
    return {"message": "Hello World!"} 


@app.post("/word")   
async def set_word(new_word: Word):
    print(new_word)
    return {"message": "New word added!"}


@app.post("/user")
async def set_user(user: UserCreate):
    await register_user(user.email, user.hashed_password)
    return {"message": "New user added!"}