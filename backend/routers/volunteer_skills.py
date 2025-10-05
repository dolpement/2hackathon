from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from backend.database import crud, schemas
from backend.database.database import get_db

router = APIRouter(
    prefix="/volunteer-skills",
    tags=["Volunteer Skills"]
)


@router.post("/", response_model=schemas.VolunteerSkillRead)
async def create_volunteer_skill(skill: schemas.VolunteerSkillCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_volunteer_skill(db, skill)


@router.get("/{skill_id}", response_model=schemas.VolunteerSkillRead)
async def read_volunteer_skill(skill_id: int, db: AsyncSession = Depends(get_db)):
    db_skill = await crud.get_volunteer_skill(db, skill_id)
    if not db_skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    return db_skill


@router.get("/volunteer/{volunteer_id}", response_model=List[schemas.VolunteerSkillRead])
async def read_volunteer_skills(volunteer_id: int, db: AsyncSession = Depends(get_db)):
    return await crud.get_volunteer_skills(db, volunteer_id)


@router.put("/{skill_id}", response_model=schemas.VolunteerSkillRead)
async def update_volunteer_skill(skill_id: int, skill_update: schemas.VolunteerSkillBase,
                                 db: AsyncSession = Depends(get_db)):
    db_skill = await crud.get_volunteer_skill(db, skill_id)
    if not db_skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    await crud.update_volunteer_skill(db, skill_id, skill_update)
    # возвращаем обновлённый навык
    return await crud.get_volunteer_skill(db, skill_id)


@router.delete("/{skill_id}")
async def delete_volunteer_skill(skill_id: int, db: AsyncSession = Depends(get_db)):
    db_skill = await crud.get_volunteer_skill(db, skill_id)
    if not db_skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    await crud.delete_volunteer_skill(db, skill_id)
    return {"detail": "Skill deleted"}
