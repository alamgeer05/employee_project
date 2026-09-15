# from sqlalchemy.orm import Session

# from models.user import User
# from schemas.user import UserCreate
# from core.security import hashed_password


# def register_user(db: Session, user: UserCreate):
#     db_user = User(
#         username=user.username,
#         email=user.email,
#         hashed_password=hashed_password(user.password)
#     )

#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)

#     return db_user