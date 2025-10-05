# tests/test_certificates.py
import pytest
from datetime import date


@pytest.mark.anyio
async def test_create_certificate(async_client, volunteer):
    payload = {
        "name": "First Aid Certificate",
        "file_url": "http://example.com/cert.pdf",
        "issued_by": "Red Cross",
        "verified_by_admin": False,
        "issue_date": str(date.today()),
        "expiry_date": str(date.today()),
        "owner_id": volunteer["id"]
    }
    response = await async_client.post("/certificates/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["owner_id"] == volunteer["id"]
    assert data["name"] == "First Aid Certificate"
    assert "id" in data


@pytest.mark.anyio
async def test_get_certificate(async_client, certificate):
    cert_id = certificate["id"]
    response = await async_client.get(f"/certificates/{cert_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == cert_id


@pytest.mark.anyio
async def test_get_certificates_by_owner(async_client, volunteer, certificate):
    owner_id = volunteer["id"]
    response = await async_client.get(f"/certificates/owner/{owner_id}")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(cert["id"] == certificate["id"] for cert in data)


@pytest.mark.anyio
async def test_update_certificate(async_client, certificate):
    cert_id = certificate["id"]
    update_payload = {
        "name": "Updated Certificate Name",
        "file_url": certificate["file_url"],
        "issued_by": certificate["issued_by"],
        "verified_by_admin": True,
        "issue_date": certificate["issue_date"],
        "expiry_date": certificate["expiry_date"],
    }
    response = await async_client.put(f"/certificates/{cert_id}", json=update_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Certificate Name"
    assert data["verified_by_admin"] is True


@pytest.mark.anyio
async def test_delete_certificate(async_client, certificate):
    cert_id = certificate["id"]
    response = await async_client.delete(f"/certificates/{cert_id}")
    assert response.status_code == 200
    assert response.json() == {"detail": "Certificate deleted"}

    # проверяем, что сертификат больше не существует
    response = await async_client.get(f"/certificates/{cert_id}")
    assert response.status_code == 404
