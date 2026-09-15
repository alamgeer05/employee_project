from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from core.database import get_db
from schemas.employee import EmployeeCreate, Employee_Response
from services.employee import create_employee, get_all_employees, get_employee_by_id, update_employee, delete_employee
from core.security import get_current_user, User

from typing import Literal

router = APIRouter()


# FastAPI, before allowing this endpoint to execute, give me the currently authenticated User and give me a database session.
@router.post("/employees", response_model=Employee_Response)
def add_employees(
    employee: EmployeeCreate,
    # current_user: User = Depends(get_current_user),
    # current_user: User = Depends(require_admin)
    db: Session = Depends(get_db)
):
    return create_employee(db, employee)

# Notice the difference:

# One employee → EmployeeResponse
# Many employees → list[EmployeeResponse]
from typing import Literal
from fastapi import APIRouter, Depends, Query

@router.get("/employees", response_model=list[Employee_Response])
def get_employees(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    search: str | None = None,
    sort_by: Literal["id", "name", "email"] = "id",
    order: Literal["asc", "desc"] = "asc",
    # current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return get_all_employees(
        db, page, limit, search, sort_by, order
    )




@router.get("/employees/{employee_id}", response_model=Employee_Response)
def get_employee(
    employee_id: int,
    # current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return get_employee_by_id(db, employee_id)


@router.put("/employees/{employee_id}")
def update_employee_data(
    employee_id: int,
    employee: EmployeeCreate,
    # current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return update_employee(db, employee_id, employee)


@router.delete("/employees/{employee_id}")
def delete_employee_data(
    employee_id: int,
    # current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return delete_employee(db, employee_id)





# Depends
# Depends

# is FastAPI's dependency injection system.

# Simple meaning:

# "FastAPI, before running my function, give me something I need."

# Here we need a database session.

# Example:

# db: Session = Depends(get_db)



    #          Client
    #            |
    #            |
    #     HTTP Request
    #            |
    #            ↓
    #  routes/employee.py
    #            |
    #            |
    #    Validate using Schema
    #            |
    #            |
    #    Get DB using Depends
    #            |
    #            |
    #    Call Service Function
    #            |
    #            |
    #       Database



#     Route file does only three things:

# Receive request
# Get required things (schema + database)
# Send work to service function