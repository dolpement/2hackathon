from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from backend.database import crud, schemas
from backend.database.database import get_db

router = APIRouter(
    prefix="/search-operations",
    tags=["Search Operations"]
)


@router.post("/", response_model=schemas.SearchOperationRead)
async def create_search(search: schemas.SearchOperationCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_search_operation(db, search)


@router.get("/{search_id}", response_model=schemas.SearchOperationRead)
async def read_search(search_id: int, db: AsyncSession = Depends(get_db)):
    db_search = await crud.get_search_operation(db, search_id)
    if not db_search:
        raise HTTPException(status_code=404, detail="Search operation not found")
    return db_search


@router.get("/", response_model=List[schemas.SearchOperationRead])
async def read_searches(db: AsyncSession = Depends(get_db)):
    return await crud.get_search_operations(db)


@router.put("/{search_id}", response_model=schemas.SearchOperationRead)
async def update_search(search_id: int, search_update: schemas.SearchOperationBase, db: AsyncSession = Depends(get_db)):
    db_search = await crud.get_search_operation(db, search_id)
    if not db_search:
        raise HTTPException(status_code=404, detail="Search operation not found")
    await crud.update_search_operation(db, search_id, search_update)
    return await crud.get_search_operation(db, search_id)


@router.delete("/{search_id}")
async def delete_search(search_id: int, db: AsyncSession = Depends(get_db)):
    db_search = await crud.get_search_operation(db, search_id)
    if not db_search:
        raise HTTPException(status_code=404, detail="Search operation not found")
    await crud.delete_search_operation(db, search_id)
    return {"detail": "Search operation deleted"}
