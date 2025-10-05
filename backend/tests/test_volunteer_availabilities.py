# tests/test_volunteer-availabilities.py
import pytest


@pytest.mark.anyio
async def test_create_volunteer_availability(async_client, volunteer):
    payload = {
        "volunteer_id": volunteer["id"],
        "day_of_week": "Mon",
        "start_time": "09:00:00",  # ✅ ISO-формат для time
        "end_time": "17:00:00"
    }

    response = await async_client.post("/volunteer-availabilities/", json=payload)
    assert response.status_code == 200, response.text
    data = response.json()

    assert data["volunteer_id"] == volunteer["id"]
    assert data["day_of_week"] == "Mon"
    assert data["start_time"] == "09:00:00"
    assert data["end_time"] == "17:00:00"
    assert "id" in data


@pytest.mark.anyio
async def test_get_volunteer_availability(async_client, volunteer_availability):
    availability_id = volunteer_availability["id"]
    response = await async_client.get(f"/volunteer-availabilities/{availability_id}")
    assert response.status_code == 200, response.text
    data = response.json()

    assert data["id"] == availability_id
    assert "day_of_week" in data
    assert "volunteer_id" in data


@pytest.mark.anyio
async def test_get_volunteer_availabilities(async_client, volunteer_availability, volunteer):
    volunteer_id = volunteer["id"]
    response = await async_client.get(f"/volunteer-availabilities/volunteer/{volunteer_id}")
    assert response.status_code == 200, response.text
    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0  # теперь запись точно есть


@pytest.mark.anyio
async def test_update_volunteer_availability(async_client, volunteer_availability):
    availability_id = volunteer_availability["id"]
    update_payload = {
        "day_of_week": "Tue",
        "start_time": "10:00:00",
        "end_time": "18:00:00"
    }

    response = await async_client.put(f"/volunteer-availabilities/{availability_id}", json=update_payload)
    assert response.status_code == 200, response.text
    data = response.json()

    assert data["day_of_week"] == "Tue"
    assert data["start_time"] == "10:00:00"
    assert data["end_time"] == "18:00:00"


@pytest.mark.anyio
async def test_delete_volunteer_availability(async_client, volunteer_availability):
    availability_id = volunteer_availability["id"]
    response = await async_client.delete(f"/volunteer-availabilities/{availability_id}")
    assert response.status_code == 200, response.text
    assert response.json() == {"detail": "Availability deleted"}

    # проверяем, что запись действительно удалена
    response = await async_client.get(f"/volunteer-availabilities/{availability_id}")
    assert response.status_code == 404
