from pydantic_settings import BaseSettings
BaseSettings
# class Settings(BaseSettings):
# config.py — reads and validates .env
# You're telling Pydantic:

# "These are the configuration values my application expects."
class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"

settings = Settings()


# settings = Settings()

# This creates an object containing your configuration.

# This line is VERY important
# class Config:
    # env_file = ".env"

# It tells BaseSettings:

# "Look inside the .env file for these values."

# config.py is used to centralize all application settings
# (like database URL, API keys, and secrets) in one place.
# This makes the code easier to manage, more secure, and simpler
# to configure across different environments.


# class Settings(BaseSettings):
#     DATABASE_URL: str
#     SECRET_KEY: str
#     ALGORITHM: str
#     ACCESS_TOKEN_EXPIRE_MINUTES: int

#     class Config:
#         env_file = ".env"

# settings = Settings()

# Now instead of:

# os.getenv("DATABASE_URL")

# you write:

# settings.DATABASE_URL




# Now other files can use settings

# For example:

# from core.config import settings

# Then:

# settings.DATABASE_URL

# or:

# settings.SECRET_KEY


