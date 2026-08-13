from typing import List, Optional
from pydantic import BaseModel, ValidationError, Field, field_validator


class Movie(BaseModel):
    title : str = Field(min_lenght=1)
    year : int = Field(ge=1888)
    rating : float = Field(ge=0.0, le=10.0)
    genres : List[str] = []
    director: str = Field(min_length=1)



    @field_validator("title")
    @classmethod
    def clean_title(cls, v: str) -> str:
        v = v.strip()
        if v.isupper():
            raise ValueError("Title cannot be all uppercase")
        cleaned = v.title()
        print(cleaned)        
        return cleaned


    @field_validator("genres")
    @classmethod
    def lowercase_genres(cls, v : List[str]) -> List[str]:
        print([g.strip().lower() for g in v])

    
    @field_validator("title", "director")
    @classmethod
    def no_empty(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("Cannot be empty")
        cleaned = v.title()
        print("\n --no empty --")
        print(cleaned)        # print if you want to watch it
        return cleaned        # but you MUST return



m = Movie(title="knight", year=2008, rating=9.0,
          genres=["  Action ", "CRIME"], director=" christopher nolan ")
print(m)


# --- rejection in action ---
try:
    Movie(title="INCEPTION", year=2010, rating=8.8)
except ValidationError as e:
    for err in e.errors():
        print(err["loc"], "->", err["msg"])


