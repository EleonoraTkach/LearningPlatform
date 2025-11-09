import logging

from fastapi import FastAPI

from app.common.db.session import SessionLocal
from app.core.logging import setup_logging
from app.modules.auth.bootstrap import run_bootstrap


def register_startup(app: FastAPI) -> None:
  setup_logging()

  @app.on_event("startup")
  async def _on_startup():
    async with SessionLocal() as db:
      try:
        # await run_bootstrap(db)
        print('Learning Platform')
      except Exception as e:
        logging.getLogger(__name__).exception("Bootstrap failed: %s", e)
