from pydantic import BaseModel, EmailStr,Field

# -------------------------------------------------------
# Schema File (employee.py)
#
# Purpose:
# Defines the data that the API accepts and returns.
# Pydantic automatically validates the incoming data.
#
# Model  -> Database Table (SQLAlchemy)
# Schema -> API Request & Response (Pydantic)
# -------------------------------------------------------

# Request Schema, user are allowed to send this data only
class EmployeeCreate(BaseModel):
    # Employee name (Required)
    name: str = Field(max_length=100, min_length=3, description="Employee ka naam")

    # Employee email (Required)
    email: EmailStr


# ===================== QUICK REVISION =====================
# BaseModel       -> Parent class for all Pydantic schemas.
#
# Schema          -> Validates request/response data.
#
# name: str       -> Required string field.
#
# email: str      -> Required string field.
#
# If a required field is missing,
# FastAPI automatically returns a 422 Validation Error.
#
# Example Request:
#
# {
#     "name": "Rahul",
#     "email": "rahul@gmail.com"
# }
#
# Example Invalid Request:
#
# {
#     "name": "Rahul"
# }
#
# Response:
# 422 Unprocessable Entity
#
# Difference:
#
# Model  -> Creates database tables.
# Schema -> Validates API input/output.
# ==========================================================




class Employee_Response(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True

# creating response model only in schemas and we add it in routes simple not more than this

# Why from_attributes = True?

# Your service returns:

# db_employee

# which is a SQLAlchemy object, not a dictionary.

# Pydantic needs permission to read its attributes        