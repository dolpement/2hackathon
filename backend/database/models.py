from sqlalchemy import (
    Column, String, Text, Boolean, Date, DateTime,
    Enum, ForeignKey, Float, Integer, Table
)
from sqlalchemy.orm import relationship, declarative_base
import enum

Base = declarative_base()


# ---------- ENUMS ----------
class ActivityStatus(enum.Enum):
    active = "active"
    inactive = "inactive"


class EquipmentStatus(enum.Enum):
    new = "new"
    old = "old"
    worn = "worn"


class EquipmentType(enum.Enum):
    vehicle = "vehicle"
    gear = "gear"
    navigation = "navigation"
    communication = "communication"
    other = "other"


class SkillCategory(enum.Enum):
    rescue = "rescue"
    technical = "technical"


class SearchStatus(enum.Enum):
    planned = "planned"
    ongoing = "ongoing"
    completed = "completed"


class UserRole(enum.Enum):
    volunteer = "volunteer"
    admin = "admin"


class WeekDay(enum.Enum):
    Mon = "Mon"
    Tue = "Tue"
    Wed = "Wed"
    Thu = "Thu"
    Fri = "Fri"
    Sat = "Sat"
    Sun = "Sun"


# ---------- ASSOCIATION TABLES ----------
search_participants = Table(
    "search_participants", Base.metadata,
    Column("search_id", ForeignKey("search_operations.id"), primary_key=True),
    Column("volunteer_id", ForeignKey("volunteers.id"), primary_key=True)
)


# ---------- TABLES ----------
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(Enum(UserRole), nullable=False)

    volunteer_id = Column(Integer, ForeignKey("volunteers.id"), nullable=True)
    volunteer = relationship("Volunteer", backref="user")


class Volunteer(Base):
    __tablename__ = "volunteers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(255), nullable=False)
    email = Column(String(255))
    phone = Column(String(50))
    avatar_url = Column(String(255))
    activity_status = Column(Enum(ActivityStatus), default=ActivityStatus.active)
    experience_years = Column(Integer)
    description = Column(Text)
    temporary_unavailable = Column(Boolean, default=False)

    skills = relationship("VolunteerSkill", back_populates="volunteer")
    certificates = relationship("Certificate", back_populates="owner")
    locations = relationship("VolunteerLocation", back_populates="volunteer")
    availability = relationship("VolunteerAvailability", back_populates="volunteer")


class VolunteerSkill(Base):
    __tablename__ = "volunteer_skills"

    id = Column(Integer, primary_key=True, autoincrement=True)
    volunteer_id = Column(Integer, ForeignKey("volunteers.id"), nullable=False)
    category = Column(Enum(SkillCategory), nullable=False)
    description = Column(Text)

    volunteer = relationship("Volunteer", back_populates="skills")


class Certificate(Base):
    __tablename__ = "certificates"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    file_url = Column(String(255))
    issued_by = Column(String(255))
    verified_by_admin = Column(Boolean, default=False)
    issue_date = Column(Date)
    expiry_date = Column(Date)
    owner_id = Column(Integer, ForeignKey("volunteers.id"), nullable=False)

    owner = relationship("Volunteer", back_populates="certificates")


class VolunteerLocation(Base):
    __tablename__ = "volunteer_locations"

    id = Column(Integer, primary_key=True, autoincrement=True)
    volunteer_id = Column(Integer, ForeignKey("volunteers.id"))
    city = Column(String(100), nullable=False)
    district = Column(String(100), nullable=True)
    max_travel_radius_km = Column(Float)

    volunteer = relationship("Volunteer", back_populates="locations")


class Equipment(Base):
    __tablename__ = "equipment"

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(Enum(EquipmentType))
    description = Column(Text)
    status = Column(Enum(EquipmentStatus))
    photo_url = Column(String(255))
    location = Column(String(255))
    responsible_person_id = Column(Integer, ForeignKey("volunteers.id"))
    availability_status = Column(Boolean, default=True)


class VolunteerAvailability(Base):
    __tablename__ = "volunteer_availability"

    id = Column(Integer, primary_key=True, autoincrement=True)
    volunteer_id = Column(Integer, ForeignKey("volunteers.id"), nullable=False)
    day_of_week = Column(Enum(WeekDay), nullable=False)
    start_time = Column(DateTime, nullable=True)
    end_time = Column(DateTime, nullable=True)

    volunteer = relationship("Volunteer", back_populates="availability")


class SearchOperation(Base):
    __tablename__ = "search_operations"

    id = Column(Integer, primary_key=True, autoincrement=True)
    request_info = Column(Text)
    coordinator_id = Column(Integer, ForeignKey("volunteers.id"))
    info_coordinator_id = Column(Integer, ForeignKey("volunteers.id"))
    meeting_place = Column(String(255))
    meeting_time = Column(DateTime)
    autonomous_request = Column(Boolean, default=False)
    report = Column(Text)
    status = Column(Enum(SearchStatus))

    participants = relationship("Volunteer", secondary=search_participants)
