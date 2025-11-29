from fastapi import APIRouter

from app.modules.progress.router import router as progress_router

main_router = APIRouter()

main_router.include_router(progress_router, prefix="/progress", tags=["Progress"])

__all__ = ["main_router"]
