from __future__ import annotations
import os

import asyncio
from typing import Final

from aiohttp import ClientSession
from fastapi import Depends, FastAPI
from starlette.requests import Request

app: Final = FastAPI(docs_url="/")
SERVICE_TWO_URL = os.getenv("SERVICE_TWO_URL")
SERVICE_TWO_PORT = os.getenv("SERVICE_TWO_PORT")


@app.on_event("startup")
async def startup_event():
    setattr(app.state, "client_session", ClientSession(raise_for_status=True))


@app.on_event("shutdown")
async def shutdown_event():
    await asyncio.wait((app.state.client_session.close()), timeout=5.0)


def client_session_dep(request: Request) -> ClientSession:
    return request.app.state.client_session


@app.get("/hello")
def read_root():
    return {"Hello": "FROM SERVICE ONE"}


@app.get("/call")
async def root(
    client_session: ClientSession = Depends(client_session_dep),
    q_param_example: str = None,
) -> str:
    async with client_session.get(f"http://{SERVICE_TWO_URL}:{SERVICE_TWO_PORT}/hello") as the_response:
        return await the_response.json()
