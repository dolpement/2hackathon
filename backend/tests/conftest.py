# tests/conftest.py

import uuid

import pytest
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from backend.database.database import get_db
from backend.database.models import Base
from backend.main import app

# ----------------- ТЕСТОВАЯ БАЗА -----------------
TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"
engine = create_async_engine(TEST_DATABASE_URL, echo=False)
AsyncTestingSessionLocal = async_sessionmaker(
    bind=engine, expire_on_commit=False, class_=AsyncSession
)


# ----------------- Переопределяем get_db -----------------
async def override_get_db():
    async with AsyncTestingSessionLocal() as session:
        yield session


app.dependency_overrides[get_db] = override_get_db


# ----------------- ФИКСТУРЫ -----------------
@pytest.fixture(scope="module", autouse=True)
async def prepare_db():
    """Создание таблиц перед тестами и очистка после них."""
    async with engine.begin() as conn:
        # Создание таблиц
        await conn.run_sync(Base.metadata.drop_all)  # опционально, чтобы очистить старые таблицы
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        # Очистка после тестов
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture
async def async_client():
    """Асинхронный клиент для FastAPI тестов."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client


@pytest.fixture
def unique_email():
    """Генератор уникальных email для тестов."""
    return f"test_{uuid.uuid4().hex}@example.com"


@pytest.fixture
async def volunteer(async_client, unique_email):
    payload = {
        "full_name": "John Doe",
        "email": unique_email,
        "phone": "1234567890",
        "activity_status": "active"
    }
    response = await async_client.post("/volunteers/", json=payload)
    return response.json()


@pytest.fixture
async def volunteer_skill(async_client, volunteer):
    payload = {
        "volunteer_id": volunteer["id"],
        "category": "rescue",
        "description": "Basic first aid"
    }
    response = await async_client.post("/volunteer-skills/", json=payload)
    return response.json()


@pytest.fixture
async def certificate(async_client, volunteer):
    payload = {
        "owner_id": volunteer["id"],
        "name": "First Aid Certificate",
        "file_url": "http://example.com/cert.pdf",
        "issued_by": "Red Cross",
        "verified_by_admin": False,
        "issue_date": "2025-01-01",
        "expiry_date": "2026-01-01"
    }
    response = await async_client.post("/certificates/", json=payload)
    assert response.status_code == 200
    return response.json()


@pytest.fixture
async def volunteer_location(async_client, volunteer):
    payload = {
        "volunteer_id": volunteer["id"],
        "city": "New York",
        "district": "Manhattan",
        "max_travel_radius_km": 15.5
    }
    response = await async_client.post("/volunteer-locations/", json=payload)
    assert response.status_code == 200
    return response.json()


@pytest.fixture
def unique_name():
    return f"equipment_{uuid.uuid4().hex}"


@pytest.fixture
async def equipment(async_client):
    payload = {
        "type": "gear",  # обязательное поле из enum EquipmentType
        "status": "new",  # обязательное поле из enum EquipmentStatus
        "description": "Rescue kit",
        "availability_status": True
    }
    response = await async_client.post("/equipments/", json=payload)
    data = response.json()
    yield data


@pytest.fixture
async def volunteer_availability(async_client, volunteer):
    payload = {
        "volunteer_id": volunteer["id"],
        "day_of_week": "Mon",
        "start_time": "09:00:00",
        "end_time": "17:00:00"
    }
    response = await async_client.post("/volunteer-availabilities/", json=payload)
    return response.json()
