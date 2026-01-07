from typing import Annotated, Sequence

from fastapi import APIRouter, Query
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from sqlmodel import select

from app.deps.db import SessionDep
from app.models.bands import Band, BandPublic

router = APIRouter(prefix="/bands")


class FilterParams(BaseModel):
    offset: int
    limit: int


@router.get("/", response_model=list[BandPublic])
def get_bands(
    session: SessionDep, parameters: Annotated[FilterParams, Query()]
) -> Sequence[Band]:
    return session.exec(
        select(Band).offset(parameters.offset).limit(parameters.limit)
    ).all()


@router.get("/{band_id}", response_model=BandPublic)
def get_band_by_id(band_id: int, session: SessionDep) -> Band:
    if model := session.get(Band, band_id):
        return model
    raise HTTPException(status_code=404, detail="Model not found")


@router.get("/{band_name}", response_model=BandPublic)
def get_band_by_name(band_name: str, session: SessionDep) -> Band:
    if model := session.exec(select(Band).where(Band.name == band_name)).first():
        return model
    raise HTTPException(status_code=404, detail="Model not found")
