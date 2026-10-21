from app.database import Base, engine
from app.routes.base import api_router
from fastapi import FastAPI
from app.routes import ai_query


# Automatically create database tables on startup if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Management API",
    description="Modular CRUD API for managing student records using FastAPI and SQLite ORM",
    version="1.0.0",
)

app.include_router(ai_query.router)


# Include the aggregated router
app.include_router(api_router)


@app.get("/", tags=["Root"])
def root():
  return {
      "message": "Welcome to Student Management API. Visit /docs for Swagger UI."
  }