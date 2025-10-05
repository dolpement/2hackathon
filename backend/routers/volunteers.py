from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from backend.database import crud, schemas
from backend.database.database import get_db

router = APIRouter(
    prefix="/volunteers",
    tags=["Volunteers"]
)


@router.post("/", response_model=schemas.VolunteerRead)
async def create_volunteer(volunteer: schemas.VolunteerCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_volunteer(db, volunteer)


@router.get("/{volunteer_id}", response_model=schemas.VolunteerRead)
async def read_volunteer(volunteer_id: int, db: AsyncSession = Depends(get_db)):
    db_volunteer = await crud.get_volunteer(db, volunteer_id)
    if not db_volunteer:
        raise HTTPException(status_code=404, detail="Volunteer not found")
    return db_volunteer


@router.get("/", response_model=List[schemas.VolunteerRead])
async def read_volunteers(db: AsyncSession = Depends(get_db)):
    return await crud.get_volunteers(db)


@router.put("/{volunteer_id}", response_model=schemas.VolunteerRead)
async def update_volunteer(volunteer_id: int, volunteer_update: schemas.VolunteerBase,
                           db: AsyncSession = Depends(get_db)):
    db_volunteer = await crud.get_volunteer(db, volunteer_id)
    if not db_volunteer:
        raise HTTPException(status_code=404, detail="Volunteer not found")
    await crud.update_volunteer(db, volunteer_id, volunteer_update)
    # возвращаем обновлённого волонтёра
    return await crud.get_volunteer(db, volunteer_id)


@router.delete("/{volunteer_id}")
async def delete_volunteer(volunteer_id: int, db: AsyncSession = Depends(get_db)):
    db_volunteer = await crud.get_volunteer(db, volunteer_id)
    if not db_volunteer:
        raise HTTPException(status_code=404, detail="Volunteer not found")
    await crud.delete_volunteer(db, volunteer_id)
    return {"detail": "Volunteer deleted"}
