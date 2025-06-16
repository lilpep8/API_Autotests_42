from dataclasses import dataclass, field
from dotenv import load_dotenv
import os


load_dotenv()
class EnvConfig:
    USERNAME = os.getenv('API_USERNAME')
    PASSWORD = os.getenv('API_PASSWORD')


@dataclass(frozen=True)
class APIConstants:
    BASE_URL: str = "https://restful-booker.herokuapp.com"
    HEADERS: dict = field(default_factory=lambda: {
        "Content-Type": "application/json",
        "Accept": "application/json"
    })
    AUTH_DATA: dict = field(default_factory=lambda:{
        "username": EnvConfig.USERNAME,
        "password": EnvConfig.PASSWORD
    })

api_config = APIConstants()
