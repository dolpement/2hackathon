# tests/test_volunteers.py
import pytest


@pytest.mark.anyio
async def test_create_volunteer(async_client, unique_email):
    payload = {
        "full_name": "John Doe",
        "email": unique_email,
        "phone": "1234567890",
        "activity_status": "active"
    }
    response = await async_client.post("/volunteers/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == unique_email
    assert "id" in data


@pytest.mark.anyio
async def test_get_volunteers(async_client, unique_email):
    # создаём ещё одного волонтёра
    await async_client.post("/volunteers/", json={
        "full_name": "Jane Doe",
        "email": unique_email,
        "phone": "9876543210",
        "activity_status": "active"
    })

    response = await async_client.get("/volunteers/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


@pytest.mark.anyio
async def test_get_volunteer(async_client, unique_email):
    create_resp = await async_client.post("/volunteers/", json={
        "full_name": "Single Volunteer",
        "email": unique_email,
        "phone": "5555555555",
        "activity_status": "active"
    })
    volunteer_id = create_resp.json()["id"]

    response = await async_client.get(f"/volunteers/{volunteer_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == unique_email


@pytest.mark.anyio
async def test_update_volunteer(async_client, unique_email):
    create_resp = await async_client.post("/volunteers/", json={
        "full_name": "Update Volunteer",
        "email": unique_email,
        "phone": "1112223333",
        "activity_status": "active"
    })
    volunteer_id = create_resp.json()["id"]

    updated_email = f"updated_{unique_email}"
    update_payload = {"email": updated_email, "full_name": "Updated Name"}
    response = await async_client.put(f"/volunteers/{volunteer_id}", json=update_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == updated_email
    assert data["full_name"] == "Updated Name"


@pytest.mark.anyio
async def test_delete_volunteer(async_client, unique_email):
    create_resp = await async_client.post("/volunteers/", json={
        "full_name": "Delete Volunteer",
        "email": unique_email,
        "phone": "4445556666",
        "activity_status": "active"
    })
    volunteer_id = create_resp.json()["id"]

    response = await async_client.delete(f"/volunteers/{volunteer_id}")
    assert response.status_code == 200
    assert response.json() == {"detail": "Volunteer deleted"}

    # проверяем, что волонтёр больше не существует
    response = await async_client.get(f"/volunteers/{volunteer_id}")
    assert response.status_code == 404
