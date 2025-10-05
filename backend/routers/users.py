# app/routers/users.py
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from backend.database import crud, schemas
from backend.database.database import get_db

router = APIRouter(
    prefix="/users",
    tags=["users"]
)


# ---------- GET ALL ----------
@router.get("/", response_model=List[schemas.UserRead])
async def read_users(db: AsyncSession = Depends(get_db)):
    return await crud.get_users(db)


# ---------- GET ONE ----------
@router.get("/{user_id}", response_model=schemas.UserRead)
async def read_user(user_id: int, db: AsyncSession = Depends(get_db)):
    db_user = await crud.get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


# ---------- CREATE ----------
@router.post("/", response_model=schemas.UserRead)
async def create_user(user: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    # Проверяем, есть ли уже пользователь с таким email
    existing_user = await crud.get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return await crud.create_user(db, user)


# ---------- UPDATE ----------
@router.put("/{user_id}", response_model=schemas.UserRead)
async def update_user(user_id: int, user_update: schemas.UserBase, db: AsyncSession = Depends(get_db)):
    await crud.update_user(db, user_id, user_update)
    updated_user = await crud.get_user(db, user_id)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user


# ---------- DELETE ----------
@router.delete("/{user_id}")
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    db_user = await crud.get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    await crud.delete_user(db, user_id)
    return {"detail": "User deleted"}
