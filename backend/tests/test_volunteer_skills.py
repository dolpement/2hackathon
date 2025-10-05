# tests/test_volunteer_skills.py
import pytest


@pytest.mark.anyio
async def test_create_volunteer_skill(async_client, volunteer):
    payload = {
        "volunteer_id": volunteer["id"],
        "category": "rescue",
        "description": "Basic first aid"
    }
    response = await async_client.post("/volunteer-skills/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["volunteer_id"] == volunteer["id"]
    assert data["category"] == "rescue"
    assert "id" in data


@pytest.mark.anyio
async def test_get_volunteer_skill(async_client, volunteer_skill):
    skill_id = volunteer_skill["id"]
    response = await async_client.get(f"/volunteer-skills/{skill_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == skill_id


@pytest.mark.anyio
async def test_get_volunteer_skills(async_client, volunteer):
    volunteer_id = volunteer["id"]
    response = await async_client.get(f"/volunteer-skills/volunteer/{volunteer_id}")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


@pytest.mark.anyio
async def test_update_volunteer_skill(async_client, volunteer_skill):
    skill_id = volunteer_skill["id"]
    # Передаем все обязательные поля схемы VolunteerSkillBase
    update_payload = {
        "category": volunteer_skill["category"],  # обязательно
        "description": "Updated description"
    }
    response = await async_client.put(f"/volunteer-skills/{skill_id}", json=update_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["description"] == "Updated description"
    assert data["category"] == volunteer_skill["category"]


@pytest.mark.anyio
async def test_delete_volunteer_skill(async_client, volunteer_skill):
    skill_id = volunteer_skill["id"]
    response = await async_client.delete(f"/volunteer-skills/{skill_id}")
    assert response.status_code == 200
    assert response.json() == {"detail": "Skill deleted"}

    # Проверяем, что скилл больше не существует
    response = await async_client.get(f"/volunteer-skills/{skill_id}")
    assert response.status_code == 404
