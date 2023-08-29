from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from sqlalchemy import select

from models import User, Word
from .schemas import UserCreate

async def get_user(async_session: async_sessionmaker[AsyncSession], user_id: int):
    async with async_session() as session:
        stmt = select(User).where(User.id == user_id)
        result = await session.execute(stmt)
        return result.scalars().first()


async def get_user_by_email(async_session: async_sessionmaker[AsyncSession], email: str):
    async with async_session() as session:
        stmt = select(User).where(User.email == email)
        result = await session.execute(stmt)
        return result.scalars().first()
    
    
async def register_user(email: str, hashed_password: str, async_session: async_sessionmaker[AsyncSession], user: UserCreate):
    async with async_session() as session:
        async with session.begin():
            new_user = User(
                email=email,
                hashed_password=hashed_password
            )
            session.add(new_user)
    
    
