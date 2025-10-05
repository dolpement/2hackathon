from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

DATABASE_URL = "mysql+aiomysql://root:root@localhost:3306/volunteer_db"

# Асинхронный движок
engine = create_async_engine(
    DATABASE_URL,
    echo=True,  # показывает SQL-запросы в консоли
    future=True
)

# Асинхронная сессия
async_session = async_sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)


# Зависимость для FastAPI
async def get_db():
    async with async_session() as session:
        yield session
