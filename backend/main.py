from fastapi import FastAPI
from app.routers.show import router as show_router
from app.routers.season import router as season_router
from app.routers.episode import router as episode_router

app = FastAPI(
    title="Peblo TV Mini API",
    description="Backend API for the Peblo TV Mini platform",
    version="1.0.0",
)
app.include_router(show_router)
app.include_router(season_router)
app.include_router(episode_router)

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "peblo-tv-mini-api"
    }