from fastapi import FastAPI

from models import Word

app = FastAPI()


@app.get("/word/{id}")   
async def get_word():
    return {"message": "Hello World!"} 

@app.post("/word")   
async def set_word(new_word: Word):
    print(new_word)
    return {"message": "New word added!"}