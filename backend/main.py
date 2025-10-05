from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

from backend.routers import users, volunteers, volunteer_skills, certificates, volunteer_locations, equipments, \
    volunteer_availabilities, search_operations

app = FastAPI(title="VolunteerMap API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # или 3000
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Пример health endpoint
@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok", "timestamp": datetime.utcnow()}


app.include_router(users.router)
app.include_router(volunteers.router)
app.include_router(volunteer_skills.router)
app.include_router(certificates.router)
app.include_router(volunteer_locations.router)
app.include_router(equipments.router)
app.include_router(volunteer_availabilities.router)
app.include_router(search_operations.router)
