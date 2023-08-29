import datetime
from sqlalchemy import DATE, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from .database import Base

    
class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    hashed_password = Column(String)
    registr_data: Mapped[datetime.datetime] = mapped_column(DATE, default=datetime.datetime.today())

    words: Mapped["Word"] = relationship(back_populates="users")

class Word(Base):
    __tablename__ = "words"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    word: Mapped[str] = mapped_column(String)
    translation: Mapped[str] = mapped_column(String)
    is_learned: Mapped[bool] = mapped_column(Boolean, default=False)

    users: Mapped["User"] = relationship(back_populates="words")