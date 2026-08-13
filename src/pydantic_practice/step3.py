from pydantic import BaseModel, ValidationError
from typing import List, Optional

class Movie(BaseModel):
    title: str
    year: int
    rating: Optional[float] = 0.0
    director: Optional[str] = None
    genres: List[str] = []


m1 = Movie(title="Inception", year=2010)
print(m1)


m2 = Movie(title="The Dark Knight", year=2008, rating=9.0, director="Christopher Nolan", genres=["Action", "Crime", "Drama"])
print(m2)


m3= Movie(title="Interstellar", year=2014, rating=8.6, director=None)
print(m3)

a = Movie(title="A", year=2000)
b = Movie(title="B", year=2001)
a.genres.append("horror")
print("a.genres:", a.genres)
print("b.genres:", b.genres)

# class Ticket(BaseModel):
#     seat : Optional[str] 

# try:
#     t = Ticket(seat=None)
#     print(t)
# except ValidationError as e:
#     print("\n -- Ticket Error --")
#     print(e.errors())