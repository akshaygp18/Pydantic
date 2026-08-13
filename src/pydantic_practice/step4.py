from typing import List, Optional
from pydantic import BaseModel, ValidationError, Field


class Movie(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    year: int = Field(ge=1888, le=2100, description="Year of theatrical release")
    rating:Optional[float] = Field(default=0.0, ge=0.0, le=10.0)
    director: Optional[str] = None
    genres: List[str] = Field(default=[], max_length=5)


m = Movie(title="Inception", year=2010, rating=8.8)
print("Valid movie:", m)

try:
    Movie(title="Inception", year=2010, rating=11.0, genres=["Action", "Crime", "Drama", "Sci-Fi", "Thriller", "Adventure"])
except ValidationError as e:
    print("\n --- Constraints Error ---")
    for err in e.errors():
        print(err["loc"][0], "->", err["msg"])

import json
print(json.dumps(Movie.model_json_schema(), indent=2))