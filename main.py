from fastapi import FastAPI
from api.routes.employee import router
from api.routes.auth import router as user_router
from api.routes.upload import router as upload_router

from models.employee import Employee
from models.user import User
from core.database import engine,Base

# app = FastAPI()
# What it does

# It creates a FastAPI application object.




app = FastAPI()

# Create all database tables from imported models
# Runs only if the tables don't already exist
Base.metadata.create_all(bind=engine)

# Why router?

# Because it receives HTTP requests.
app.include_router(router)
app.include_router(user_router)
app.include_router(upload_router)


# Root endpoint
# URL: GET /
@app.get("/")
def home():
    # FastAPI automatically converts Python dict to JSON
    return {
        "message": "Home Page"
    }


# Revision
# app = FastAPI() → Create app.
# @app.get("/") → Create GET endpoint.
# return dict → Automatically converted to JSON.
# uvicorn main:app --reload → Run app.




# ================= QUICK REVISION =================
# FastAPI()                -> Create the application
# main.py                  -> Entry point of the project
# Base.metadata.create_all -> Create database tables
# include_router(router)   -> Register API routes
# @app.get("/")            -> Create a GET endpoint
# return dict              -> Automatically returned as JSON
# uvicorn main:app --reload-> Start the FastAPI server
# ================================================



# Project
#    │
#    ▼
# main.py
#    │
#    ▼
# database.py
#    │
#    ▼
# models/
#    │
#    ▼
# schemas/
#    │
#    ▼
# routes/
#    │
#    ▼
# CRUD (optional)