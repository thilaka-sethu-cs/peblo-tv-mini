from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.season import Season
from app.models.episode import Episode
from app.schemas.season import SeasonCreate, SeasonResponse
from app.schemas.episode import EpisodeResponse


router = APIRouter(
    prefix="/seasons",
    tags=["Seasons"],
)


@router.post("/", response_model=SeasonResponse)
def create_season(
    season: SeasonCreate,
    db: Session = Depends(get_db),
):
    new_season = Season(
        show_id=season.show_id,
        season_number=season.season_number,
    )

    db.add(new_season)
    db.commit()
    db.refresh(new_season)

    return new_season


@router.get("/", response_model=list[SeasonResponse])
def get_seasons(
    db: Session = Depends(get_db),
):
    return db.query(Season).all()

@router.get("/{season_id}", response_model=SeasonResponse)
def get_season(
    season_id: int,
    db: Session = Depends(get_db),
):
    season = (
        db.query(Season)
        .filter(Season.id == season_id)
        .first()
    )

    if not season:
        raise HTTPException(
            status_code=404,
            detail="Season not found",
        )

    return season


@router.get("/{season_id}/episodes", response_model=list[EpisodeResponse])
def get_season_episodes(
    season_id: int,
    db: Session = Depends(get_db),
):
    season = db.query(Season).filter(Season.id == season_id).first()

    if not season:
        raise HTTPException(
            status_code=404,
            detail="Season not found",
        )

    return db.query(Episode).filter(Episode.season_id == season_id).all()

@router.put("/{season_id}", response_model=SeasonResponse)
def update_season(
    season_id: int,
    season: SeasonCreate,
    db: Session = Depends(get_db),
):
    existing_season = (
        db.query(Season)
        .filter(Season.id == season_id)
        .first()
    )

    if not existing_season:
        raise HTTPException(
            status_code=404,
            detail="Season not found",
        )

    existing_season.show_id = season.show_id
    existing_season.season_number = season.season_number

    db.commit()
    db.refresh(existing_season)

    return existing_season


@router.delete("/{season_id}")
def delete_season(
    season_id: int,
    db: Session = Depends(get_db),
):
    existing_season = (
        db.query(Season)
        .filter(Season.id == season_id)
        .first()
    )

    if not existing_season:
        raise HTTPException(
            status_code=404,
            detail="Season not found",
        )

    db.delete(existing_season)
    db.commit()

    return {"message": "Season deleted successfully"}