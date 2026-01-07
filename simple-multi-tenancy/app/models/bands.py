from sqlmodel import Field, SQLModel


class Band(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str


class BandPublic(SQLModel):
    id: int
    name: str
