# tests/test_users.py
import pytest


@pytest.mark.anyio
async def test_create_user(async_client, unique_email):
    payload = {"email": unique_email, "password": "secret", "role": "volunteer"}
    response = await async_client.post("/users/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == unique_email
    assert "id" in data


@pytest.mark.anyio
async def test_get_users(async_client, unique_email):
    # создаём ещё одного пользователя, чтобы был хотя бы один в базе
    await async_client.post("/users/", json={"email": unique_email, "password": "secret", "role": "volunteer"})

    response = await async_client.get("/users/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


@pytest.mark.anyio
async def test_get_user(async_client, unique_email):
    create_resp = await async_client.post("/users/",
                                          json={"email": unique_email, "password": "secret", "role": "volunteer"})
    user_id = create_resp.json()["id"]

    response = await async_client.get(f"/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == unique_email


@pytest.mark.anyio
async def test_update_user(async_client, unique_email):
    create_resp = await async_client.post("/users/",
                                          json={"email": unique_email, "password": "secret", "role": "volunteer"})
    user_id = create_resp.json()["id"]

    updated_email = f"updated_{unique_email}"
    update_payload = {"email": updated_email, "role": "volunteer"}
    response = await async_client.put(f"/users/{user_id}", json=update_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == updated_email


@pytest.mark.anyio
async def test_delete_user(async_client, unique_email):
    create_resp = await async_client.post("/users/",
                                          json={"email": unique_email, "password": "secret", "role": "volunteer"})
    user_id = create_resp.json()["id"]

    response = await async_client.delete(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json() == {"detail": "User deleted"}

    # проверяем, что пользователь больше не существует
    response = await async_client.get(f"/users/{user_id}")
    assert response.status_code == 404
