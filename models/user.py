from sqlalchemy import Integer,String,Enum as SQLEnum
from sqlalchemy.orm import mapped_column,Mapped

from core.database import Base

from enum import Enum

class UserRole(str, Enum):
    ADMIN = "admin"
    USER = "user"



class User(Base):
    __tablename__ = "users"
    id:Mapped[int] = mapped_column(Integer,primary_key=True,index=True)
    username:Mapped[str] = mapped_column(String(100),unique=True)
    email:Mapped[str] = mapped_column(String(100), unique=True)
    hashed_password:Mapped[str]=mapped_column(String(255))
    role:Mapped[UserRole] = mapped_column(        
        SQLEnum(UserRole),
        default=UserRole.USER,
        nullable=False,)
