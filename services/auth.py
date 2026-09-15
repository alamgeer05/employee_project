from sqlalchemy import or_
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from models.user import User
from schemas.user import UserCreate
from core.security import hashed_password, verify_password, create_access_token



# Password proves who you are during login. JWT proves that you already logged in during later requests.

# db_user = User(

# Question:

# Why not directly write

# db.add(user)

# ?

# Very important interview question.

# Because

# user

# is NOT a database object.

# It is a

# UserCreate

# Schema.
# So we convert

# Schema
#       │
#       ▼
# Model

def register_user(db: Session, user: UserCreate):
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password(user.password)
    )

    db.add(db_user)
    db.commit()
    # Without refresh

# your object may not contain database-generated values like auto-increment IDs, timestamps, or defaults.
    db.refresh(db_user)

    return db_user








def login_user(db: Session, form_data: OAuth2PasswordRequestForm):
    db_user = db.query(User).filter(
        or_(User.email == form_data.username, User.username == form_data.username)
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )

    if not verify_password(form_data.password, db_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )

    token = create_access_token({"sub": db_user.email})

    return {
        "access_token": token,
        "token_type": "bearer"
    }


# What is sub?

# sub means:

# subject

# In our application, we're saying:

# "sub": db_user.email

# means:

# "This token belongs to this user."

# So:

# {
#     "sub": "alam@gmail.com"
# }

# means:

# This token belongs to alam@gmail.com

# That's all you need to remember for now.