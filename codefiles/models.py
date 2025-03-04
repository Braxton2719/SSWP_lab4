from pydantic import BaseModel

class Character(BaseModel):
    character_class: str
    character_race: str

    def __repr__(self):
        return f"You are a {self.character_class}. Your race is {self.character_race}."