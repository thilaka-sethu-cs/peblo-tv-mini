from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Season(Base):
    __tablename__ = "seasons"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    show_id: Mapped[int] = mapped_column(
        ForeignKey("shows.id"),
        nullable=False,
    )

    season_number: Mapped[int] = mapped_column(nullable=False)

    show = relationship("Show", back_populates="seasons")
    episodes = relationship("Episode", back_populates="season")