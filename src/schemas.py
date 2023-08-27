import datetime
from pydantic import BaseModel


class WordBase(BaseModel):
    word: str
    translation: str
    
    
class WordCreate(WordBase):
    pass


class Word(WordBase):
    id: int
    user_id: int
    is_learned: bool

    
    class Config:
        orm_mode = True
    

class UserBase(BaseModel):
    email: str
    registr_data: datetime.datetime
    
    
class UserCreate(UserBase):
    hashed_password: str
    
    
class User(UserBase):
    id: int
    words: list[Word] = []
    
    class Config:
        orm_mode = True