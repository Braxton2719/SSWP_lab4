from pydantic import BaseModel

class Classes(BaseModel):
    index: str
    name: str
    url: str

class Races(BaseModel):
    index: str
    name: str
    url: str

