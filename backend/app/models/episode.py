from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Episode(Base):
    __tablename__ = "episodes"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    season_id: Mapped[int] = mapped_column(
        ForeignKey("seasons.id"),
        nullable=False,
    )

    title: Mapped[str] = mapped_column(String(200), nullable=False)
    synopsis: Mapped[str | None] = mapped_column(String(1000), nullable=True)
    episode_number: Mapped[int] = mapped_column(nullable=False)

    season = relationship("Season", back_populates="episodes")