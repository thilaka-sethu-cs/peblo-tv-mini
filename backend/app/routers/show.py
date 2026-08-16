from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Show
from app.models.season import Season
from app.schemas.show import ShowCreate, ShowResponse
from app.schemas.season import SeasonResponse


router = APIRouter(
    prefix="/shows",
    tags=["Shows"],
)


@router.post("/", response_model=ShowResponse)
def create_show(
    show: ShowCreate,
    db: Session = Depends(get_db),
):
    new_show = Show(**show.model_dump())

    db.add(new_show)
    db.commit()
    db.refresh(new_show)

    return new_show


@router.get("/", response_model=list[ShowResponse])
def get_shows(
    db: Session = Depends(get_db),
):
    return db.query(Show).all()


@router.put("/{show_id}", response_model=ShowResponse)
def update_show(
    show_id: int,
    show: ShowCreate,
    db: Session = Depends(get_db),
):
    existing_show = db.query(Show).filter(Show.id == show_id).first()

    if existing_show is None:
        return {"detail": "Show not found"}

    existing_show.title = show.title
    existing_show.synopsis = show.synopsis
    existing_show.section = show.section
    existing_show.category = show.category
    existing_show.status = show.status

    db.commit()
    db.refresh(existing_show)

    return existing_show

@router.delete("/{show_id}")
def delete_show(
    show_id: int,
    db: Session = Depends(get_db),
):
    existing_show = db.query(Show).filter(Show.id == show_id).first()

    if existing_show is None:
        return {"detail": "Show not found"}

    db.delete(existing_show)
    db.commit()

    return {"message": "Show deleted successfully"}

@router.get("/{show_id}/seasons", response_model=list[SeasonResponse])
def get_show_seasons(
    show_id: int,
    db: Session = Depends(get_db),
):
    show = db.query(Show).filter(Show.id == show_id).first()

    if not show:
        raise HTTPException(
            status_code=404,
            detail="Show not found",
        )

    return db.query(Season).filter(Season.show_id == show_id).all()