from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "AI Recruiter Agent"
    admin_email: str
    api_key: str

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings()