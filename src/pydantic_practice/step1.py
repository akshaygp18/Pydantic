from pydantic import BaseModel

class Movie(BaseModel):
    title : str
    year : int


m = Movie(title="Inception", year=200)
print(m)
print(m.title)
print(m.year)
print(type(m.year))


    