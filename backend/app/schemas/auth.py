from pydantic import BaseModel


class UserOut(BaseModel):
    id: str
    email: str | None = None
    name: str | None = None
    role: str
