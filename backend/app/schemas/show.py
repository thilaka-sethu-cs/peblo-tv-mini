from pydantic import BaseModel


class ShowCreate(BaseModel):
    title: str
    synopsis: str | None = None
    section: str | None = None
    category: str | None = None
    status: str = "draft"


class ShowResponse(BaseModel):
    id: int
    title: str
    synopsis: str | None = None
    section: str | None = None
    category: str | None = None
    status: str

    class Config:
        from_attributes = True