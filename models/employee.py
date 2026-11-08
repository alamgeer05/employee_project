from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from core.database import Base


class Employee(Base):
    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100), unique=True)



#     Mapped[str]

# It is a type hint for SQLAlchemy.

# It tells SQLAlchemy:

# "This attribute stores a string."

# Python side:   id is an int
# Database side: id is an INTEGER column

# Mapped[int]       → Python/SQLAlchemy type information
# mapped_column()   → database column configuration