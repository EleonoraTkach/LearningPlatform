from fastapi import APIRouter
from learning_platform_common.utils import ResponseUtils

router = APIRouter()


@router.get("/")
async def root():
  return ResponseUtils.success("ok")
