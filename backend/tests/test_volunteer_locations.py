# tests/test_volunteer_locations.py
import pytest


@pytest.mark.anyio
async def test_create_volunteer_location(async_client, volunteer):
    payload = {
        "volunteer_id": volunteer["id"],
        "city": "New York",
        "district": "Manhattan",
        "max_travel_radius_km": 15.5
    }
    response = await async_client.post("/volunteer-locations/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["volunteer_id"] == volunteer["id"]
    assert data["city"] == "New York"
    assert "id" in data


@pytest.mark.anyio
async def test_get_volunteer_location(async_client, volunteer_location):
    location_id = volunteer_location["id"]
    response = await async_client.get(f"/volunteer-locations/{location_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == location_id


@pytest.mark.anyio
async def test_get_volunteer_locations(async_client, volunteer, volunteer_location):
    """
    Для этого теста добавляем зависимость от фикстуры volunteer_location,
    чтобы была хотя бы одна локация в базе.
    """
    volunteer_id = volunteer["id"]
    response = await async_client.get(f"/volunteer-locations/volunteer/{volunteer_id}")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0  # проверяем, что есть хотя бы одна локация


@pytest.mark.anyio
async def test_update_volunteer_location(async_client, volunteer_location):
    location_id = volunteer_location["id"]
    update_payload = {"city": "Brooklyn", "max_travel_radius_km": 20.0}
    response = await async_client.put(f"/volunteer-locations/{location_id}", json=update_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["city"] == "Brooklyn"
    assert data["max_travel_radius_km"] == 20.0


@pytest.mark.anyio
async def test_delete_volunteer_location(async_client, volunteer_location):
    location_id = volunteer_location["id"]
    response = await async_client.delete(f"/volunteer-locations/{location_id}")
    assert response.status_code == 200
    assert response.json() == {"detail": "Location deleted"}

    # проверяем, что локация больше не существует
    response = await async_client.get(f"/volunteer-locations/{location_id}")
    assert response.status_code == 404
