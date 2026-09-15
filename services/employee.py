from fastapi import HTTPException
from sqlalchemy.orm import Session
# Session is the database connection object.
# You use it for:

# adding data
# searching data
# updating data
# deleting data
# Example:
# db.add()
# db.query()
# db.delete()

from models.employee import Employee
from schemas.employee import EmployeeCreate


def create_employee(db: Session, employee: EmployeeCreate):
    db_employee = Employee(
        name=employee.name,
        email=employee.email
    )

    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)

#     Sends the created employee back to the route.
# Route sends it to the user as JSON.

#     Why db.refresh()?

# After commit(), PostgreSQL generates values like:

# id
# default timestamps (if any)

# refresh() reloads the object so you get those values.

    return db_employee


def get_all_employees(
    db: Session,
    page: int,
    limit: int,
    search: str | None = None,
    sort_by: str = "id",
    order: str = "asc"
):
    query = db.query(Employee)

    if search:
        query = query.filter(
            Employee.name.ilike(f"%{search}%")
        )

    if sort_by == "name":
        column = Employee.name

    elif sort_by == "email":
        column = Employee.email

    else:
        column = Employee.id

    if order == "desc":
        query = query.order_by(column.desc())
    else:
        query = query.order_by(column.asc())

    offset = (page - 1) * limit

    return (
        query
        .offset(offset)
        .limit(limit)
        .all()
    )

def get_employee_by_id(db: Session, employee_id: int):
    employee =  db.query(Employee).filter(Employee.id == employee_id).first()

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee




def update_employee(db: Session, employee_id: int, employee: EmployeeCreate):
    db_employee = db.query(Employee).filter(Employee.id == employee_id).first()

    if not db_employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    db_employee.name = employee.name
    db_employee.email = employee.email

    db.commit()
    db.refresh(db_employee)

    return db_employee


def delete_employee(db: Session, employee_id: int):
    db_employee = db.query(Employee).filter(Employee.id == employee_id).first()

    if not db_employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    db.delete(db_employee)
    db.commit()

    return {"message": "Employee deleted successfully"}





# Route
#   |
#   | receives request
#   ↓
# Service
#   |
#   | performs database operations
#   ↓
# Model
#   |
#   | represents table
#   ↓
# Database




# Your route says:

# "Someone wants to create an employee."

# Your service says:

# "Okay, I will actually insert that employee into the database."



# Client sends JSON
#         |
#         |
#         v
# Route
# --------------------------------
# employee = EmployeeCreate(...)
# db = Database Session


#         |
#         |
#         v

# create_employee(db, employee)


#         |
#         |
#         v

# Service
# --------------------------------
# def create_employee(db, employee):


# db  = same database session
# employee = same EmployeeCreate object


#         |
#         |
#         v

# Employee Model created


#         |
#         |
#         v

# Database saved