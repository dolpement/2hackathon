from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional, List
from datetime import date, datetime, time
import enum


# ---------- ENUMS ----------
class ActivityStatus(str, enum.Enum):
    active = "active"
    inactive = "inactive"


class EquipmentStatus(str, enum.Enum):
    new = "new"
    old = "old"
    worn = "worn"


class EquipmentType(str, enum.Enum):
    vehicle = "vehicle"
    gear = "gear"
    navigation = "navigation"
    communication = "communication"
    other = "other"


class SkillCategory(str, enum.Enum):
    rescue = "rescue"
    technical = "technical"


class SearchStatus(str, enum.Enum):
    planned = "planned"
    ongoing = "ongoing"
    completed = "completed"


class UserRole(str, enum.Enum):
    volunteer = "volunteer"
    admin = "admin"


class WeekDay(str, enum.Enum):
    Mon = "Mon"
    Tue = "Tue"
    Wed = "Wed"
    Thu = "Thu"
    Fri = "Fri"
    Sat = "Sat"
    Sun = "Sun"


# ---------- USER ----------
class UserBase(BaseModel):
    email: EmailStr
    role: UserRole
    volunteer_id: Optional[int] = None


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    role: Optional[UserRole] = None
    volunteer_id: Optional[int] = None


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int

    class Config:
        orm_mode = True


# ---------- VOLUNTEER ----------
class VolunteerBase(BaseModel):
    full_name: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    avatar_url: Optional[str] = None
    activity_status: ActivityStatus = ActivityStatus.active
    experience_years: Optional[int] = None
    description: Optional[str] = None
    temporary_unavailable: bool = False


class VolunteerCreate(VolunteerBase):
    pass


class VolunteerRead(VolunteerBase):
    id: int

    class Config:
        orm_mode = True


# ---------- VOLUNTEER SKILL ----------
class VolunteerSkillBase(BaseModel):
    category: SkillCategory
    description: Optional[str] = None


class VolunteerSkillCreate(VolunteerSkillBase):
    volunteer_id: int


class VolunteerSkillRead(VolunteerSkillBase):
    id: int
    volunteer_id: int

    class Config:
        orm_mode = True


# ---------- CERTIFICATE ----------
class CertificateBase(BaseModel):
    name: str
    file_url: Optional[str] = None
    issued_by: Optional[str] = None
    verified_by_admin: bool = False
    issue_date: Optional[date] = None
    expiry_date: Optional[date] = None


class CertificateCreate(CertificateBase):
    owner_id: int


class CertificateRead(CertificateBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


# ---------- VOLUNTEER LOCATION ----------
class VolunteerLocationBase(BaseModel):
    city: str
    district: Optional[str] = None
    max_travel_radius_km: Optional[float] = None


class VolunteerLocationCreate(VolunteerLocationBase):
    volunteer_id: int


class VolunteerLocationRead(VolunteerLocationBase):
    id: int
    volunteer_id: int

    class Config:
        orm_mode = True


# ---------- EQUIPMENT ----------
class EquipmentBase(BaseModel):
    type: EquipmentType
    description: Optional[str] = None
    status: Optional[EquipmentStatus] = None
    photo_url: Optional[str] = None
    location: Optional[str] = None
    responsible_person_id: Optional[int] = None
    availability_status: bool = True


class EquipmentCreate(EquipmentBase):
    pass


class EquipmentUpdate(BaseModel):
    type: Optional[EquipmentType] = None
    status: Optional[EquipmentStatus] = None
    description: Optional[str] = None
    availability_status: Optional[bool] = None
    location: Optional[str] = None
    responsible_person_id: Optional[int] = None


class EquipmentRead(EquipmentBase):
    id: int

    class Config:
        orm_mode = True


# ---------- VOLUNTEER AVAILABILITY ----------
class VolunteerAvailabilityBase(BaseModel):
    day_of_week: WeekDay
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None


class VolunteerAvailabilityCreate(VolunteerAvailabilityBase):
    volunteer_id: int
    day_of_week: WeekDay
    start_time: datetime
    end_time: datetime

    @field_validator("start_time", "end_time", mode="before")
    def parse_time(cls, value):
        if isinstance(value, str) and len(value) <= 8:  # "HH:MM:SS"
            return datetime.strptime(value, "%H:%M:%S")
        return value


class VolunteerAvailabilityUpdate(BaseModel):
    day_of_week: Optional[WeekDay] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None

    @field_validator("start_time", "end_time", mode="before")
    def parse_time(cls, value):
        if isinstance(value, str) and len(value) <= 8:  # "HH:MM:SS"
            return datetime.strptime(value, "%H:%M:%S")
        return value


class VolunteerAvailabilityRead(BaseModel):
    id: int
    volunteer_id: int
    day_of_week: str
    start_time: datetime
    end_time: datetime

    @field_validator("start_time", "end_time", mode="after")
    def strip_date(cls, value: datetime) -> str:
        # Вернём только "HH:MM:SS"
        return value.strftime("%H:%M:%S")

    class Config:
        orm_mode = True


# ---------- SEARCH OPERATION ----------
class SearchOperationBase(BaseModel):
    request_info: Optional[str] = None
    coordinator_id: Optional[int] = None
    info_coordinator_id: Optional[int] = None
    meeting_place: Optional[str] = None
    meeting_time: Optional[datetime] = None
    autonomous_request: bool = False
    report: Optional[str] = None
    status: Optional[SearchStatus] = None


class SearchOperationUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    request_info: Optional[str] = None
    coordinator_id: Optional[int] = None
    info_coordinator_id: Optional[int] = None
    meeting_place: Optional[str] = None
    meeting_time: Optional[datetime] = None
    autonomous_request: Optional[bool] = None
    report: Optional[str] = None
    status: Optional[SearchStatus] = None


class SearchOperationCreate(SearchOperationBase):
    participants: Optional[List[int]] = []  # список volunteer_id


class SearchOperationRead(SearchOperationBase):
    id: int
    participants: List[VolunteerRead] = []

    class Config:
        orm_mode = True
