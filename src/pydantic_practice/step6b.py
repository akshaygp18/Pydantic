from typing import List, Optional
from pydantic import BaseModel, ValidationError, Field, model_validator


class Movie(BaseModel):
    title: str
    year: int = Field(ge=1888, le=2030) 
    rating : float = Field(ge=0.0, le=10.0)  # Movies started around 1888
    budget : Optional[float] = None
    box_office : Optional[float] = None


    @model_validator(mode="after")
    def check_rules(self):

        if self.rating > 9.5 and self.year > 2020:
            raise ValueError("Rating too high for a recent movie")
        if self.box_office is not None and self.budget is None:
            raise ValueError("If box_office is provided, budget must also be provided")
        
        return self

# --- valid ---
m = Movie(title="The Godfather", year=1972, rating=9.2)
print("OK:", m)

# --- Rule 1 broken ---
try:
    Movie(title="Some New Film", year=2024, rating=9.8)
except ValidationError as e:
    for err in e.errors():
        print("\nRule 1:", err["loc"], "->", err["msg"])

# --- Rule 2 broken ---
try:
    Movie(title="Tenet", year=2020, rating=7.5, box_office=365_000_000)
except ValidationError as e:
    for err in e.errors():
        print("Rule 2:", err["loc"], "->", err["msg"])