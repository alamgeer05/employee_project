from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
# from dotenv import load_dotenv
# import os

from core.config import settings

# load_dotenv()

# DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_URL = settings.DATABASE_URL

# engine as SQLAlchemy's main connection manager to PostgreSQL.
# Which database should I communicate with and how?
engine = create_engine(DATABASE_URL)


# Whenever an API needs to work with the database, we create a session.
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

class Base(DeclarativeBase):
    pass
# Now Base is the parent class for all your SQLAlchemy models.

# You have: 

# class Base(DeclarativeBase):
#     pass

# This is the parent class for your SQLAlchemy models.

# Your model:

# class Employee(Base):

# Your user model:

# class User(Base):

# So:

# Base
#  │
#  ├── Employee
#  │
#  └── User

# SQLAlchemy uses these models to understand your database tables.


# We create a database dependency so every API request gets its own 
# database session automatically, and FastAPI closes it safely after the request is finished.
# Dependency to provide DB session

# Without Dependency

# Suppose you write:

# @app.post("/employees")
# def create_employee():

#     db = SessionLocal()

#     employee = Employee(name="Alam", email="abc@gmail.com")

#     db.add(employee)
#     db.commit()

#     db.close()

# It works.
# That's called code duplication.

# Now imagine you have 50 APIs.
def get_db():
    db = SessionLocal()
    try:
        yield db
        # "We use yield so FastAPI can provide the database session "
        # "to the API and automatically close it after the request completes."
    finally:
        db.close()



# Now every route simply says:

# db: Session = Depends(get_db)

# Done.

# FastAPI automatically does the rest.      
# 
# 
# 
# With

# yield

# the function pauses instead of ending.  



# We are creating a dependency that provides a database session.

# The database (PostgreSQL) already exists. The dependency is just a reusable helper that says:

# "Whenever a route needs to talk to PostgreSQL, I'll create a session, hand it over, and clean it up afterward."



# | Line              | Purpose                                                       |
# | ----------------- | ------------------------------------------------------------- |
# | `load_dotenv()`   | Load variables from `.env`.                                   |
# | `os.getenv()`     | Read `DATABASE_URL`.                                          |
# | `create_engine()` | Connect SQLAlchemy to the database.                           |
# | `sessionmaker()`  | Create a factory for database sessions.                       |
# | `Base`            | Parent class for all models/tables.                           |
# | `get_db()`        | Give one database session per request and close it afterward. |


# Overall responsibility of database.py

# You can remember it with one sentence:

# database.py sets up everything needed to talk to the database: 
# it loads the database URL, creates the connection (engine), 
# creates sessions (SessionLocal), defines the base class (Base), and
#  provides get_db() so each API request gets a database session that is
#  automatically closed afterward.





# What is a Session?

# Suppose your endpoint says:

# db.query(Employee).all()

# That db is a SQLAlchemy Session.

# For example:

# db: Session

# It allows your application to:

# db.add()
# db.query()
# db.commit()
# db.delete()
# db.refresh()




# Now the MOST important part: get_db()

# You have:

# def get_db():
#     db = SessionLocal()

#     try:
#         yield db
#     finally:
#         db.close()

# This function means:

# "Create a database session, give it to the API, and close it when the API is finished."




# yield db

# gives that session to your endpoint.


# Request
#    ↓
# Depends(get_db)
#    ↓
# SessionLocal()
#    ↓
# db session created
#    ↓
# give db to endpoint
#    ↓
# endpoint uses database

# When the request finishes:

# finally:
    # db.close()

# runs.

# So the session gets cleaned up.



        #         .env
        #          │
        #          │ DATABASE_URL
        #          ▼
        #      config.py
        #          │
        #          │ settings.DATABASE_URL
        #          ▼
        #    database.py
        #          │
        #          ▼
        # create_engine()
        #          │
        #          ▼
        #       engine
        #          │
        #          ▼
        #   sessionmaker()
        #          │
        #          ▼
        #     SessionLocal
        #          │
        #          ▼
        #       get_db()
        #          │
        #          ▼
        #      db: Session
        #          │
        #          ▼
        #       ROUTER
        #          │
        #          ▼
        #      SERVICE
        #          │
        #          ▼
        #       MODEL
        #          │
        #          ▼
        #     PostgreSQL