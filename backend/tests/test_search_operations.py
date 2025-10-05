# tests/test_search_operations.py
import pytest
from httpx import AsyncClient
from datetime import datetime


@pytest.mark.anyio
async def test_create_search(async_client: AsyncClient):
    payload = {
        "request_info": "Test request info",
        "coordinator_id": 1,
        "info_coordinator_id": 2,
        "meeting_place": "Test Location",
        "meeting_time": datetime.now().isoformat(),
        "autonomous_request": True,
        "report": "Test report",
        "status": None,
        "participants": []
    }

    response = await async_client.post("/search-operations/", json=payload)
    assert response.status_code == 200, response.text

    data = response.json()
    assert data["request_info"] == payload["request_info"]
    assert data["coordinator_id"] == payload["coordinator_id"]
    assert data["info_coordinator_id"] == payload["info_coordinator_id"]
    assert data["meeting_place"] == payload["meeting_place"]
    assert data["autonomous_request"] == payload["autonomous_request"]
    assert data["report"] == payload["report"]
    assert "id" in data
    assert "participants" in data
    assert isinstance(data["participants"], list)


@pytest.mark.anyio
async def test_read_search(async_client: AsyncClient):
    payload = {"request_info": "Read test", "participants": []}
    create_resp = await async_client.post("/search-operations/", json=payload)
    search_id = create_resp.json()["id"]

    response = await async_client.get(f"/search-operations/{search_id}")
    assert response.status_code == 200, response.text

    data = response.json()
    assert data["id"] == search_id
    assert data["request_info"] == payload["request_info"]


@pytest.mark.anyio
async def test_read_search_not_found(async_client: AsyncClient):
    response = await async_client.get("/search-operations/999999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Search operation not found"


@pytest.mark.anyio
async def test_read_searches(async_client: AsyncClient):
    payloads = [
        {"request_info": "Search 1", "participants": []},
        {"request_info": "Search 2", "participants": []},
    ]
    for payload in payloads:
        await async_client.post("/search-operations/", json=payload)

    response = await async_client.get("/search-operations/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 2


@pytest.mark.anyio
async def test_update_search(async_client: AsyncClient):
    payload = {"request_info": "Original request", "participants": []}
    create_resp = await async_client.post("/search-operations/", json=payload)
    search_id = create_resp.json()["id"]

    update_payload = {"request_info": "Updated request", "autonomous_request": True}
    response = await async_client.put(f"/search-operations/{search_id}", json=update_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["request_info"] == update_payload["request_info"]
    assert data["autonomous_request"] is True


@pytest.mark.anyio
async def test_delete_search(async_client: AsyncClient):
    payload = {"request_info": "To Delete", "participants": []}
    create_resp = await async_client.post("/search-operations/", json=payload)
    search_id = create_resp.json()["id"]

    response = await async_client.delete(f"/search-operations/{search_id}")
    assert response.status_code == 200
    assert response.json() == {"detail": "Search operation deleted"}

    response = await async_client.get(f"/search-operations/{search_id}")
    assert response.status_code == 404
