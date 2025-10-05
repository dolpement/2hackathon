from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from sqlalchemy.orm import selectinload

from . import models, schemas


# ---------- USER ----------
async def create_user(db: AsyncSession, user: schemas.UserCreate) -> models.User:
    db_user = models.User(email=user.email, password_hash=user.password, role=user.role, volunteer_id=user.volunteer_id)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


# В crud.py, в секции USER
async def get_user_by_email(db: AsyncSession, email: str) -> Optional[models.User]:
    result = await db.execute(select(models.User).where(models.User.email == email))
    return result.scalars().first()


async def get_user(db: AsyncSession, user_id: int) -> Optional[models.User]:
    result = await db.execute(select(models.User).where(models.User.id == user_id))
    return result.scalars().first()


async def get_users(db: AsyncSession) -> List[models.User]:
    result = await db.execute(select(models.User))
    return result.scalars().all()


async def update_user(db: AsyncSession, user_id: int, user_update: schemas.UserUpdate):
    await db.execute(
        update(models.User)
        .where(models.User.id == user_id)
        .values(**user_update.dict(exclude_unset=True))
    )
    await db.commit()


async def delete_user(db: AsyncSession, user_id: int):
    await db.execute(delete(models.User).where(models.User.id == user_id))
    await db.commit()


# ---------- VOLUNTEER ----------
async def create_volunteer(db: AsyncSession, volunteer: schemas.VolunteerCreate) -> models.Volunteer:
    db_volunteer = models.Volunteer(**volunteer.dict())
    db.add(db_volunteer)
    await db.commit()
    await db.refresh(db_volunteer)
    return db_volunteer


async def get_volunteer(db: AsyncSession, volunteer_id: int) -> Optional[models.Volunteer]:
    result = await db.execute(select(models.Volunteer).where(models.Volunteer.id == volunteer_id))
    return result.scalars().first()


async def get_volunteers(db: AsyncSession) -> List[models.Volunteer]:
    result = await db.execute(select(models.Volunteer))
    return result.scalars().all()


async def update_volunteer(db: AsyncSession, volunteer_id: int, volunteer_update: schemas.VolunteerBase):
    await db.execute(
        update(models.Volunteer)
        .where(models.Volunteer.id == volunteer_id)
        .values(**volunteer_update.dict(exclude_unset=True))
    )
    await db.commit()


async def delete_volunteer(db: AsyncSession, volunteer_id: int):
    await db.execute(delete(models.Volunteer).where(models.Volunteer.id == volunteer_id))
    await db.commit()


# ---------- VOLUNTEER SKILL ----------
async def create_volunteer_skill(db: AsyncSession, skill: schemas.VolunteerSkillCreate) -> models.VolunteerSkill:
    db_skill = models.VolunteerSkill(**skill.dict())
    db.add(db_skill)
    await db.commit()
    await db.refresh(db_skill)
    return db_skill


async def get_volunteer_skill(db: AsyncSession, skill_id: int) -> Optional[models.VolunteerSkill]:
    result = await db.execute(select(models.VolunteerSkill).where(models.VolunteerSkill.id == skill_id))
    return result.scalars().first()


async def get_volunteer_skills(db: AsyncSession, volunteer_id: int) -> List[models.VolunteerSkill]:
    result = await db.execute(select(models.VolunteerSkill).where(models.VolunteerSkill.volunteer_id == volunteer_id))
    return result.scalars().all()


async def update_volunteer_skill(db: AsyncSession, skill_id: int, skill_update: schemas.VolunteerSkillBase):
    await db.execute(
        update(models.VolunteerSkill)
        .where(models.VolunteerSkill.id == skill_id)
        .values(**skill_update.dict(exclude_unset=True))
    )
    await db.commit()


async def delete_volunteer_skill(db: AsyncSession, skill_id: int):
    await db.execute(delete(models.VolunteerSkill).where(models.VolunteerSkill.id == skill_id))
    await db.commit()


# ---------- CERTIFICATE ----------
async def create_certificate(db: AsyncSession, certificate: schemas.CertificateCreate) -> models.Certificate:
    db_certificate = models.Certificate(**certificate.dict())
    db.add(db_certificate)
    await db.commit()
    await db.refresh(db_certificate)
    return db_certificate


async def get_certificate(db: AsyncSession, certificate_id: int) -> Optional[models.Certificate]:
    result = await db.execute(select(models.Certificate).where(models.Certificate.id == certificate_id))
    return result.scalars().first()


async def get_certificates(db: AsyncSession, owner_id: int) -> List[models.Certificate]:
    result = await db.execute(select(models.Certificate).where(models.Certificate.owner_id == owner_id))
    return result.scalars().all()


async def update_certificate(db: AsyncSession, certificate_id: int, certificate_update: schemas.CertificateBase):
    await db.execute(
        update(models.Certificate)
        .where(models.Certificate.id == certificate_id)
        .values(**certificate_update.dict(exclude_unset=True))
    )
    await db.commit()


async def delete_certificate(db: AsyncSession, certificate_id: int):
    await db.execute(delete(models.Certificate).where(models.Certificate.id == certificate_id))
    await db.commit()


# ---------- VOLUNTEER LOCATION ----------
async def create_volunteer_location(db: AsyncSession,
                                    location: schemas.VolunteerLocationCreate) -> models.VolunteerLocation:
    db_location = models.VolunteerLocation(**location.dict())
    db.add(db_location)
    await db.commit()
    await db.refresh(db_location)
    return db_location


async def get_volunteer_location(db: AsyncSession, location_id: int) -> Optional[models.VolunteerLocation]:
    result = await db.execute(select(models.VolunteerLocation).where(models.VolunteerLocation.id == location_id))
    return result.scalars().first()


async def get_volunteer_locations(db: AsyncSession, volunteer_id: int) -> List[models.VolunteerLocation]:
    result = await db.execute(
        select(models.VolunteerLocation).where(models.VolunteerLocation.volunteer_id == volunteer_id))
    return result.scalars().all()


async def update_volunteer_location(db: AsyncSession, location_id: int, location_update: schemas.VolunteerLocationBase):
    await db.execute(
        update(models.VolunteerLocation)
        .where(models.VolunteerLocation.id == location_id)
        .values(**location_update.dict(exclude_unset=True))
    )
    await db.commit()


async def delete_volunteer_location(db: AsyncSession, location_id: int):
    await db.execute(delete(models.VolunteerLocation).where(models.VolunteerLocation.id == location_id))
    await db.commit()


# ---------- EQUIPMENT ----------
async def create_equipment(db: AsyncSession, equipment: schemas.EquipmentCreate) -> models.Equipment:
    db_equipment = models.Equipment(**equipment.dict())
    db.add(db_equipment)
    await db.commit()
    await db.refresh(db_equipment)
    return db_equipment


async def get_equipment(db: AsyncSession, equipment_id: int) -> Optional[models.Equipment]:
    result = await db.execute(select(models.Equipment).where(models.Equipment.id == equipment_id))
    return result.scalars().first()


async def get_all_equipment(db: AsyncSession) -> List[models.Equipment]:
    result = await db.execute(select(models.Equipment))
    return result.scalars().all()


async def update_equipment(db: AsyncSession, equipment_id: int, equipment_update: schemas.EquipmentUpdate):
    await db.execute(
        update(models.Equipment)
        .where(models.Equipment.id == equipment_id)
        .values(**equipment_update.dict(exclude_unset=True))
    )
    await db.commit()


async def get_equipment_by_responsible_person(db: AsyncSession, person_id: int) -> List[models.Equipment]:
    result = await db.execute(
        select(models.Equipment).where(models.Equipment.responsible_person_id == person_id)
    )
    return result.scalars().all()


async def delete_equipment(db: AsyncSession, equipment_id: int):
    await db.execute(delete(models.Equipment).where(models.Equipment.id == equipment_id))
    await db.commit()


# ---------- VOLUNTEER AVAILABILITY ----------
async def create_volunteer_availability(db: AsyncSession,
                                        availability: schemas.VolunteerAvailabilityCreate) -> models.VolunteerAvailability:
    db_avail = models.VolunteerAvailability(**availability.dict())
    db.add(db_avail)
    await db.commit()
    await db.refresh(db_avail)
    return db_avail


async def get_volunteer_availability(db: AsyncSession, availability_id: int) -> Optional[models.VolunteerAvailability]:
    result = await db.execute(
        select(models.VolunteerAvailability).where(models.VolunteerAvailability.id == availability_id))
    return result.scalars().first()


async def get_volunteer_availabilities(db: AsyncSession, volunteer_id: int) -> List[models.VolunteerAvailability]:
    result = await db.execute(
        select(models.VolunteerAvailability).where(models.VolunteerAvailability.volunteer_id == volunteer_id))
    return result.scalars().all()


async def update_volunteer_availability(db: AsyncSession, availability_id: int,
                                        availability_update: schemas.VolunteerAvailabilityUpdate):
    await db.execute(
        update(models.VolunteerAvailability)
        .where(models.VolunteerAvailability.id == availability_id)
        .values(**availability_update.dict(exclude_unset=True))
    )
    await db.commit()


async def delete_volunteer_availability(db: AsyncSession, availability_id: int):
    await db.execute(delete(models.VolunteerAvailability).where(models.VolunteerAvailability.id == availability_id))
    await db.commit()


# ---------- SEARCH OPERATION ----------
async def create_search_operation(
        db: AsyncSession, search: schemas.SearchOperationCreate
) -> models.SearchOperation:
    db_search = models.SearchOperation(**search.dict(exclude={"participants"}))
    db.add(db_search)
    await db.commit()
    await db.refresh(db_search)

    # Добавляем участников, если есть
    if search.participants:
        result = await db.execute(
            select(models.Volunteer).where(models.Volunteer.id.in_(search.participants))
        )
        db_search.participants = result.scalars().all()
        await db.commit()
        await db.refresh(db_search)

    # Подгружаем участников для безопасной сериализации
    await db.refresh(db_search, attribute_names=["participants"])
    return db_search


async def get_search_operation(
        db: AsyncSession, search_id: int
) -> Optional[models.SearchOperation]:
    result = await db.execute(
        select(models.SearchOperation)
        .options(selectinload(models.SearchOperation.participants))
        .where(models.SearchOperation.id == search_id)
    )
    return result.scalars().first()


async def get_search_operations(db: AsyncSession) -> List[models.SearchOperation]:
    result = await db.execute(
        select(models.SearchOperation).options(selectinload(models.SearchOperation.participants))
    )
    return result.scalars().all()


async def update_search_operation(
        db: AsyncSession, search_id: int, search_update: schemas.SearchOperationUpdate
):
    await db.execute(
        update(models.SearchOperation)
        .where(models.SearchOperation.id == search_id)
        .values(**search_update.dict(exclude_unset=True))
    )
    await db.commit()


async def delete_search_operation(db: AsyncSession, search_id: int):
    await db.execute(delete(models.SearchOperation).where(models.SearchOperation.id == search_id))
    await db.commit()
