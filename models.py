from pydantic import BaseModel


class Movie(BaseModel):
    title: str
    year: str
    rating: str
    poster: str | None = None
    plot: str | None = None