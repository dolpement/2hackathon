from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from backend.database import crud, schemas
from backend.database.database import get_db

router = APIRouter(
    prefix="/certificates",
    tags=["Certificates"]
)


@router.post("/", response_model=schemas.CertificateRead)
async def create_certificate(certificate: schemas.CertificateCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_certificate(db, certificate)


@router.get("/{certificate_id}", response_model=schemas.CertificateRead)
async def read_certificate(certificate_id: int, db: AsyncSession = Depends(get_db)):
    db_cert = await crud.get_certificate(db, certificate_id)
    if not db_cert:
        raise HTTPException(status_code=404, detail="Certificate not found")
    return db_cert


@router.get("/owner/{owner_id}", response_model=List[schemas.CertificateRead])
async def read_certificates(owner_id: int, db: AsyncSession = Depends(get_db)):
    return await crud.get_certificates(db, owner_id)


@router.put("/{certificate_id}", response_model=schemas.CertificateRead)
async def update_certificate(certificate_id: int, certificate_update: schemas.CertificateBase,
                             db: AsyncSession = Depends(get_db)):
    db_cert = await crud.get_certificate(db, certificate_id)
    if not db_cert:
        raise HTTPException(status_code=404, detail="Certificate not found")
    await crud.update_certificate(db, certificate_id, certificate_update)
    # возвращаем обновлённый сертификат
    return await crud.get_certificate(db, certificate_id)


@router.delete("/{certificate_id}")
async def delete_certificate(certificate_id: int, db: AsyncSession = Depends(get_db)):
    db_cert = await crud.get_certificate(db, certificate_id)
    if not db_cert:
        raise HTTPException(status_code=404, detail="Certificate not found")
    await crud.delete_certificate(db, certificate_id)
    return {"detail": "Certificate deleted"}
