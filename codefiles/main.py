import requests
from models import Character
from pydantic import ValidationError

character = Character(character_class="", character_race="")

# dedicated to making API requests to view the class options
def character_classes():
    class_url = "https://www.dnd5eapi.co/api/2014/classes"
    class_headers = {'Accept': 'application/json'}

    class_response = requests.get(class_url, headers=class_headers)
    if class_response.status_code == 200: # successful
        classes_data = class_response.json()
        classes = classes_data['results']

        print("\nStarting off with character class, the available classes are:\n"
              + "--------------------------------------------------------------\n")
        for each_class in classes:
            print(each_class['name'])
    else:
        print(f"Fetch Failed for {class_url}, Error Code: {class_response.status_code}")
    return

def races():
    r_url = "https://www.dnd5eapi.co/api/2014/races"
    r_headers = {'Accept': 'application/json'} 

    r_response = requests.get(r_url, headers=r_headers)
    if r_response.status_code == 200: #successful
        r_data = r_response.json()
        races = r_data['results']
        #print(races[1]['url'])


        while True:
            print("\nThe options for races include:\n"
              + "--------------------------------------------------------------\n")
            r_index = 1
            for each_race in races:
                print(f"{r_index}. {each_race['name']}")
                r_index += 1
            
            r_decision = input("Select the number associated with the option to learn more: ")
            if r_decision.isdigit():
                r_decision = int(r_decision)
                if(r_decision > 0 and r_decision < 10):
                    selected_race_url = races[r_decision - 1]['url']
                    race_selection(selected_race_url)
                    return
                else:
                    print("Race does not exist...")
            else:
                print("Invalid entry...")
    else:
        print(f"Fetch Failed for {r_url}, Error Code: {r_response.status_code}")
    return

def race_selection(race_url):
    new_r_url = f"https://www.dnd5eapi.co{race_url}"
    new_r_headers = {'Accept': 'application/json'}

    new_r_response = requests.get(new_r_url, headers=new_r_headers)
    if new_r_response.status_code == 200:
        new_r_data = new_r_response.json()
        print(new_r_data['name'])
        print("--------------------------")
        print(f"Alignment: {new_r_data['alignment']}")
        
        while True:
            print(f"Are you sure you wish to be a {new_r_data['name']}?")
            print("1. Yes\n2. No")
            decision = input("Enter Here:")
            if decision == "1":
                character.character_race = new_r_data['name']
                print(f"Your character race is {character.character_race}")
                return
            elif decision == "2":
                race()
            else:
                print("Invalid Option...")


def start():
    print("\nWelcome to the D&D character creator! You will choose what class and race your character will have."
          + "You will also allocate your ability points to finish your character stats.\n")

    character_classes()
    races()

start()