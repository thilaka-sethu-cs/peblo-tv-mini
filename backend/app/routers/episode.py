from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.episode import Episode
from app.schemas.episode import EpisodeCreate, EpisodeResponse


router = APIRouter(
    prefix="/episodes",
    tags=["Episodes"],
)


@router.post("/", response_model=EpisodeResponse)
def create_episode(
    episode: EpisodeCreate,
    db: Session = Depends(get_db),
):
    new_episode = Episode(
        season_id=episode.season_id,
        title=episode.title,
        synopsis=episode.synopsis,
        episode_number=episode.episode_number,
    )

    db.add(new_episode)
    db.commit()
    db.refresh(new_episode)

    return new_episode

@router.get("/", response_model=list[EpisodeResponse])
def get_episodes(
    db: Session = Depends(get_db),
):
    return db.query(Episode).all()

@router.get("/{episode_id}", response_model=EpisodeResponse)
def get_episode(
    episode_id: int,
    db: Session = Depends(get_db),
):
    episode = db.query(Episode).filter(Episode.id == episode_id).first()

    if not episode:
        raise HTTPException(status_code=404, detail="Episode not found")

    return episode

@router.put("/{episode_id}", response_model=EpisodeResponse)
def update_episode(
    episode_id: int,
    episode: EpisodeCreate,
    db: Session = Depends(get_db),
):
    existing_episode = (
        db.query(Episode)
        .filter(Episode.id == episode_id)
        .first()
    )

    if not existing_episode:
        raise HTTPException(
            status_code=404,
            detail="Episode not found",
        )

    existing_episode.season_id = episode.season_id
    existing_episode.title = episode.title
    existing_episode.synopsis = episode.synopsis
    existing_episode.episode_number = episode.episode_number

    db.commit()
    db.refresh(existing_episode)

    return existing_episode

@router.delete("/{episode_id}")
def delete_episode(
    episode_id: int,
    db: Session = Depends(get_db),
):
    episode = db.query(Episode).filter(Episode.id == episode_id).first()

    if not episode:
        raise HTTPException(
            status_code=404,
            detail="Episode not found",
        )

    db.delete(episode)
    db.commit()

    return {"message": "Episode deleted successfully"}