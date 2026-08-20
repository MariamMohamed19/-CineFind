from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware

from movie_service import search_movie


app = FastAPI(
    title="CineFind Movie API",
    description="A simple movie search API built with FastAPI",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Welcome to CineFind Movie API"
    }


@app.get("/search")
def search(
    title: str = Query(
        ...,
        min_length=1,
        description="Movie title to search for"
    )
):

    movie = search_movie(title)

    if movie is None:
        raise HTTPException(
            status_code=404,
            detail="Movie not found"
        )

    return movie