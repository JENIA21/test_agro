import geojson
from sqlmodel import SQLModel, Field


class FieldsCoordinates(SQLModel):
    name: str
    coordinates: str


class Fields(FieldsCoordinates, table=True):
    id: int = Field(default=None, primary_key=True)


class FieldsCreate(FieldsCoordinates):
    pass
