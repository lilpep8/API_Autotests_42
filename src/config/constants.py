from dataclasses import dataclass, field


@dataclass(frozen=True)
class APIConstants:
    BASE_URL: str = "https://restful-booker.herokuapp.com"
    HEADERS: dict = field(default_factory=lambda: {
        "Content-Type": "application/json",
        "Accept": "application/json"
    })

api_config = APIConstants()
