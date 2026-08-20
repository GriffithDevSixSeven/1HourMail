from core.redis import redis_manager

from contextlib import asynccontextmanager
from fastapi import FastAPI
import logging

@asynccontextmanager
async def lifespan(app : FastAPI):
    redis_manager.init_pool()
    logging.info("Redis start...")
    yield
    await redis_manager.close_pool()
    print("Redis stop...")

app = FastAPI()