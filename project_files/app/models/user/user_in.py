from pydantic import BaseModel
from typing import Optional


class UserIn(BaseModel):
    id: int
    name: str
    password: Optional[str] = None
