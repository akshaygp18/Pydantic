from pydantic import BaseModel, ValidationError


class Movie(BaseModel):
    title : str
    year : int
    rating : float


m = Movie(title="Inception", year=2010, rating=8.8)
print("Valid movie:", m)


try:
    bad = Movie(title="Inception", year=2010)
    
except ValidationError as e:
    print("\n -- Full error ---")
    print(e)

    print("\n--- As a list of dict ---")
    for err in e.errors():
        print(err)