from pydantic import BaseModel


class EpisodeCreate(BaseModel):
    season_id: int
    title: str
    synopsis: str | None = None
    episode_number: int


class EpisodeResponse(BaseModel):
    id: int
    season_id: int
    title: str
    synopsis: str | None = None
    episode_number: int

    model_config = {
        "from_attributes": True
    }