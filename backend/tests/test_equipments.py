# tests/test_equipments.py
import pytest


@pytest.mark.anyio
async def test_create_equipment(async_client):
    payload = {
        "type": "gear",  # из EquipmentType
        "description": "Rescue kit",
        "status": "new",  # из EquipmentStatus
        "availability_status": True
    }
    response = await async_client.post("/equipments/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["type"] == "gear"
    assert data["description"] == "Rescue kit"
    assert data["status"] == "new"
    assert data["availability_status"] is True
    assert "id" in data


@pytest.mark.anyio
async def test_get_equipment(async_client, equipment):
    equipment_id = equipment["id"]
    response = await async_client.get(f"/equipments/{equipment_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == equipment_id
    assert data["type"] == equipment["type"]


@pytest.mark.anyio
async def test_get_all_equipment(async_client, equipment):
    response = await async_client.get("/equipments/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(item["id"] == equipment["id"] for item in data)


@pytest.mark.anyio
async def test_update_equipment(async_client, equipment):
    equipment_id = equipment["id"]
    update_payload = {
        "description": "Updated rescue kit",
        "status": "old",
        "availability_status": False
    }
    response = await async_client.put(f"/equipments/{equipment_id}", json=update_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["description"] == "Updated rescue kit"
    assert data["status"] == "old"
    assert data["availability_status"] is False


@pytest.mark.anyio
async def test_delete_equipment(async_client, equipment):
    equipment_id = equipment["id"]
    response = await async_client.delete(f"/equipments/{equipment_id}")
    assert response.status_code == 200
    assert response.json() == {"detail": "Equipment deleted"}

    # проверяем, что оборудование больше не существует
    response = await async_client.get(f"/equipments/{equipment_id}")
    assert response.status_code == 404
