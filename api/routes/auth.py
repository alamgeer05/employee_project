from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from core.database import get_db
from core.security import get_current_user, User
from schemas.user import UserCreate, UserResponse
from services.auth import register_user, login_user
from schemas.token import Token


router = APIRouter(
    prefix = "/auth",
    tags = ["Authentication"]
)



# This function is called the Route Handler.

# Its job is not to write SQL queries.

# Its job is only to:

# Receive the request
# Validate it
# Get dependencies
# Call the service
# Return the response



@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    return register_user(db, user)


@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    return login_user(db, form_data)

# OAuth2PasswordRequestForm FastAPI ka ek helper class hai jo OAuth2 password 
# flow me login credentials receive karne ke kaam aati hai.


@router.get("/me", response_model=UserResponse)
def read_current_user(current_user: User = Depends(get_current_user)):
    return current_user



# FastAPI creates form_data

# This:

# form_data: OAuth2PasswordRequestForm = Depends()

# means:

# "FastAPI, read the username and password from the request and create an OAuth2PasswordRequestForm object."

# So FastAPI gives our route something like:

# form_data.username
# form_data.password

# For example:

# form_data.username → "alam@gmail.com"
# form_data.password → "123456"




        #          LOGIN
        #            │
        #            ▼
        # username + password
        #            │
        #            ▼
        #        FastAPI
        #            │
        #            ├── OAuth2PasswordRequestForm
        #            └── DB Session
        #            │
        #            ▼
        #          Router
        #            │
        #            ▼
        #       login_user()
        #            │
        #            ▼
        #      Find User
        #            │
        #      ┌─────┴─────┐
        #      │           │
        #    Not found    Found
        #      │           │
        #     401          ▼
        #             Verify Password
        #                  │
        #             ┌────┴────┐
        #             │         │
        #           Wrong     Correct
        #             │         │
        #            401        ▼
        #                  Create JWT
        #                      │
        #                      ▼
        #                {"sub": email}
        #                      │
        #                      ▼
        #                 Sign with
        #                SECRET_KEY
        #                      │
        #                      ▼
        #                    JWT
        #                      │
        #                      ▼
        #             Return access_token
        #                      │
        #                      ▼
        #                   Client