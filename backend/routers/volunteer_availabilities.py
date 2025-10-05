from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from backend.database import crud, schemas
from backend.database.database import get_db

router = APIRouter(
    prefix="/volunteer-availabilities",
    tags=["Volunteer Availabilities"]
)


@router.post("/", response_model=schemas.VolunteerAvailabilityRead)
async def create_availability(availability: schemas.VolunteerAvailabilityCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_volunteer_availability(db, availability)


@router.get("/{availability_id}", response_model=schemas.VolunteerAvailabilityRead)
async def read_availability(availability_id: int, db: AsyncSession = Depends(get_db)):
    db_avail = await crud.get_volunteer_availability(db, availability_id)
    if not db_avail:
        raise HTTPException(status_code=404, detail="Availability not found")
    return db_avail


@router.get("/volunteer/{volunteer_id}", response_model=List[schemas.VolunteerAvailabilityRead])
async def read_availabilities_for_volunteer(volunteer_id: int, db: AsyncSession = Depends(get_db)):
    return await crud.get_volunteer_availabilities(db, volunteer_id)


@router.put("/{availability_id}", response_model=schemas.VolunteerAvailabilityRead)
async def update_availability(availability_id: int, availability_update: schemas.VolunteerAvailabilityUpdate,
                              db: AsyncSession = Depends(get_db)):
    db_avail = await crud.get_volunteer_availability(db, availability_id)
    if not db_avail:
        raise HTTPException(status_code=404, detail="Availability not found")
    await crud.update_volunteer_availability(db, availability_id, availability_update)
    return await crud.get_volunteer_availability(db, availability_id)


@router.delete("/{availability_id}")
async def delete_availability(availability_id: int, db: AsyncSession = Depends(get_db)):
    db_avail = await crud.get_volunteer_availability(db, availability_id)
    if not db_avail:
        raise HTTPException(status_code=404, detail="Availability not found")
    await crud.delete_volunteer_availability(db, availability_id)
    return {"detail": "Availability deleted"}
