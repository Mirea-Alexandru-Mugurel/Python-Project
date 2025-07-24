from fastapi import FastAPI
from contextlib import asynccontextmanager

from core.middleware import setup_middleware
from core.config import setup_app_config
from api.routes import router
from models.db import init_db
from services.worker import start_worker, stop_worker


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    worker_task = await start_worker()
    yield
    await stop_worker(worker_task)


app = FastAPI(lifespan=lifespan)

# Setup config and middleware
setup_app_config(app)
setup_middleware(app)

# Register routes
app.include_router(router)
