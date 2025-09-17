from fastapi import FastAPI

from models.representative import Person
from functions.representative import get_representive_person_status

app = FastAPI()


@app.post("/GetRepresentivePersonStatus")
def get_representive_person_status_endpoint(person: Person):
    return get_representive_person_status(person)
