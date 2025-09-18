import uvicorn
from fastapi import FastAPI

from core.config import BASE_DIR
from models.model import Person
from functions.representative import get_representive_person_status

app = FastAPI()


@app.post("/GetRepresentivePersonStatus")
def get_representive_person_status_endpoint(person: Person):
    return get_representive_person_status(person)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
