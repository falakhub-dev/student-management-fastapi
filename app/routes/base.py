from app.routes import (
    create_student,
    delete_students,
    get_students,
    update_student,
)
from fastapi import APIRouter

# Master router to aggregate all individual API route modules
api_router = APIRouter()

api_router.include_router(create_student.router)
api_router.include_router(get_students.router)
api_router.include_router(update_student.router)
api_router.include_router(delete_students.router)