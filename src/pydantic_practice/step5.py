from pydantic import BaseModel, ValidationError, Field
from typing import List, Optional




class Director(BaseModel):
    name: str = Field(min_length=1)
    birth_year : int = Field(ge=1800)


class Movie(BaseModel):
    title : str = Field(min_length=1, max_length=100)
    year : int = Field(ge=1888)
    rating : float = Field(ge=0.0, le=10.0)
    director : Director
    genres : List[str] = []


raw = {
    "title": "Inception",
    "year": 2010,
    "rating": 8.8,
    "director": {
        "name": "Christopher Nolan",
        "birth_year": 1970
    },
    "genres": ["Action", "Crime", "Drama"]
}

# m = Movie(**raw)
# print(m)
# print()
# print("Director name:", m.director.name)
# print("Director type:", type(m.director))


raw["director"] = {"name": "", "birth_year": 1500}
try:
    Movie(**raw)
except ValidationError as e:
    for err in e.errors():
        print(err["loc"], "->", err["msg"])