from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from backend.database import crud, schemas
from backend.database.database import get_db

router = APIRouter(
    prefix="/volunteer-locations",
    tags=["Volunteer Locations"]
)


@router.post("/", response_model=schemas.VolunteerLocationRead)
async def create_location(location: schemas.VolunteerLocationCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_volunteer_location(db, location)


@router.get("/{location_id}", response_model=schemas.VolunteerLocationRead)
async def read_location(location_id: int, db: AsyncSession = Depends(get_db)):
    db_location = await crud.get_volunteer_location(db, location_id)
    if not db_location:
        raise HTTPException(status_code=404, detail="Location not found")
    return db_location


@router.get("/volunteer/{volunteer_id}", response_model=List[schemas.VolunteerLocationRead])
async def read_locations(volunteer_id: int, db: AsyncSession = Depends(get_db)):
    return await crud.get_volunteer_locations(db, volunteer_id)


@router.put("/{location_id}", response_model=schemas.VolunteerLocationRead)
async def update_location(location_id: int, location_update: schemas.VolunteerLocationBase,
                          db: AsyncSession = Depends(get_db)):
    db_location = await crud.get_volunteer_location(db, location_id)
    if not db_location:
        raise HTTPException(status_code=404, detail="Location not found")
    await crud.update_volunteer_location(db, location_id, location_update)
    return await crud.get_volunteer_location(db, location_id)


@router.delete("/{location_id}")
async def delete_location(location_id: int, db: AsyncSession = Depends(get_db)):
    db_location = await crud.get_volunteer_location(db, location_id)
    if not db_location:
        raise HTTPException(status_code=404, detail="Location not found")
    await crud.delete_volunteer_location(db, location_id)
    return {"detail": "Location deleted"}
