from pydantic import BaseModel

# for the character you're creating
class Character(BaseModel):
    character_class: str
    character_race: str
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int

    def __repr__(self):
        return f"You are a {self.character_class}. Your race is {self.character_race}.\n Your stats are:\n" +\
                f"Strength: {self.strength}\nDexterity: {self.dexterity}\nConstitution: {self.constitution}\n" +\
                f"Intelligence: {self.intelligence}\nWisdom: {self.wisdom}\nCharisma: {self.charisma}\n"