from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from backend.database import crud, schemas
from backend.database.database import get_db

router = APIRouter(
    prefix="/equipments",
    tags=["Equipments"]
)


@router.post("/", response_model=schemas.EquipmentRead)
async def create_equipment(equipment: schemas.EquipmentCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_equipment(db, equipment)


@router.get("/{equipment_id}", response_model=schemas.EquipmentRead)
async def read_equipment(equipment_id: int, db: AsyncSession = Depends(get_db)):
    db_equipment = await crud.get_equipment(db, equipment_id)
    if not db_equipment:
        raise HTTPException(status_code=404, detail="Equipment not found")
    return db_equipment


@router.get("/", response_model=List[schemas.EquipmentRead])
async def read_all_equipment(db: AsyncSession = Depends(get_db)):
    return await crud.get_all_equipment(db)


@router.put("/{equipment_id}", response_model=schemas.EquipmentRead)
async def update_equipment_endpoint(
        equipment_id: int,
        equipment_update: schemas.EquipmentUpdate,  # <- новая модель
        db: AsyncSession = Depends(get_db)
):
    db_equipment = await crud.get_equipment(db, equipment_id)
    if not db_equipment:
        raise HTTPException(status_code=404, detail="Equipment not found")

    await crud.update_equipment(db, equipment_id, equipment_update)
    return await crud.get_equipment(db, equipment_id)


@router.delete("/{equipment_id}")
async def delete_equipment(equipment_id: int, db: AsyncSession = Depends(get_db)):
    db_equipment = await crud.get_equipment(db, equipment_id)
    if not db_equipment:
        raise HTTPException(status_code=404, detail="Equipment not found")
    await crud.delete_equipment(db, equipment_id)
    return {"detail": "Equipment deleted"}


@router.get("/owner/{person_id}", response_model=List[schemas.EquipmentRead])
async def read_equipment_by_responsible_person(person_id: int, db: AsyncSession = Depends(get_db)):
    equipments = await crud.get_equipment_by_responsible_person(db, person_id)
    if not equipments:
        raise HTTPException(status_code=404, detail="No equipment found for this person")
    return equipments
