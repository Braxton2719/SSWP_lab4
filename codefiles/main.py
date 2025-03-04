import requests
from models import Character

# Global character class object to modify
character = Character(character_class="", character_race="", 
                      strength=0, dexterity=0, constitution=0,
                      intelligence=0, wisdom=0, charisma=0)

# Dedicated to making API requests to view the class options
def character_classes():
    class_url = "https://www.dnd5eapi.co/api/2014/classes"
    class_headers = {'Accept': 'application/json'}

    class_response = requests.get(class_url, headers=class_headers)
    if class_response.status_code == 200:
        classes_data = class_response.json()
        classes = classes_data['results']

        while True:
            print("\nStarting off with character class, the available classes are:\n"
                + "--------------------------------------------------------------\n")
            class_index = 1
            for each_class in classes:
                print(f"{class_index}. {each_class['name']}")
                class_index += 1

            # Made to let the user pick a race, and confirm that it is the race they want
            class_selection = input("Which class would you like to choose? Select the number associated with the class: ")
            if class_selection.isdigit():
                class_selection = int(class_selection)
                if class_selection > 0 and class_selection < 13:
                    character.character_class = classes[class_selection - 1]['name']

                    # Confirmation loop to decide on class
                    while True:
                        print(f"\nAre you sure you want to be a {character.character_class}?\n"
                              + "1. Yes\n2. No\n")
                        confirm = input("Enter here: ")
                        if confirm == "1":
                            return  # Exit if confirmed
                        elif confirm == "2":
                            character.character_class = ""
                            break  # Go back to class selection
                        else:
                            print("Invalid Selection...")
    else:
        print(f"Fetch Failed for {class_url}, Error Code: {class_response.status_code}")

# Dedicated to doing API call for D&D races
def races():
    r_url = "https://www.dnd5eapi.co/api/2014/races"
    r_headers = {'Accept': 'application/json'} 

    r_response = requests.get(r_url, headers=r_headers)
    if r_response.status_code == 200: #successful
        r_data = r_response.json()
        races = r_data['results']

        while True:
            print("\nThe options for races include:\n"
              + "--------------------------------------------------------------\n")
            r_index = 1
            for each_race in races:
                print(f"{r_index}. {each_race['name']}")
                r_index += 1
            
            # Let the user choose the race they want to learn about
            r_decision = input("Select the number associated with the option to learn more: ")
            if r_decision.isdigit():
                r_decision = int(r_decision)
                if(r_decision > 0 and r_decision < 10):
                    selected_race_url = races[r_decision - 1]['url']
                    if race_selection(selected_race_url):  # If True, break the loop
                        break
                else:
                    print("Race does not exist...")
            else:
                print("Invalid entry...")
    else:
        print(f"Fetch Failed for {r_url}, Error Code: {r_response.status_code}")
    return

# Redirect from races() to this function to display info about selected race
def race_selection(race_url):
    new_r_url = f"https://www.dnd5eapi.co{race_url}"
    new_r_headers = {'Accept': 'application/json'}

    new_r_response = requests.get(new_r_url, headers=new_r_headers)
    if new_r_response.status_code == 200:
        new_r_data = new_r_response.json()
        print("\nRace has been selected...\n")
        print(new_r_data['name'])
        print("---------------------------------------")
        print(f"Alignment: {new_r_data['alignment']}")
        
        while True:
            print(f"\nAre you sure you wish to be a {new_r_data['name']}?")
            print("1. Yes\n2. No")
            decision = input("Enter Here: ")
            if decision == "1":
                character.character_race = new_r_data['name']
                print(f"\nYour character race is {character.character_race}")
                return True # Confirmation to move onto next function
            elif decision == "2":
                return False # Reject selected option to re-select a new one
            else:
                print("Invalid Option...")
    else: 
        print(f"Fetch Failed for {new_r_url}, Error Code: {new_r_response.status_code}")
    return

# Display Ability Score Names from endpoint
def ability_scores():
    as_url = "https://www.dnd5eapi.co/api/2014/ability-scores"
    as_headers = {'Accept': 'application/json'}

    as_response = requests.get(as_url, headers=as_headers)
    if as_response.status_code == 200:
        as_data = as_response.json()
        ability_scores = as_data['results']

        while True:
            print("\nIn D&D, there are the following ability scores:\n"
                + "------------------------------------------------------\n")
            as_index = 1
            for each_as in ability_scores:
                print(f"{as_index}. {each_as['name']}\n")
                as_index += 1

            # Allow user to pick an abiltiy score to learn about 
            as_decision = input("Select the number associated with the option to learn more: ")
            if as_decision.isdigit():
                as_decision = int(as_decision)
                if(as_decision > 0 and as_decision < 7):
                    selected_as_url = ability_scores[as_decision - 1]['url']
                    as_selection(selected_as_url)
                    return
                else:
                    print("Ability Score does not exist...")
            else:
                print("Invalid entry...")
    else:
        print(f"Fetch Failed for {as_url}, Error Code: {as_response.status_code}")
    return

# View description of selected Ability Score
def as_selection(as_url_sect):
    new_as_url = f"https://www.dnd5eapi.co{as_url_sect}"
    new_as_headers = {'Accept': 'application/json'}

    new_as_response = requests.get(new_as_url, headers=new_as_headers)
    if new_as_response.status_code == 200:
        new_as_data = new_as_response.json()

        while True:
            print(f"\n{new_as_data['full_name']}\n"
                  + "---------------------------------")
            print(f"Description: {new_as_data['desc']}\n")
            
            # Ask if the user would want to view other ability scores
            print("Would you like to view other ability scores?")
            print("1. Yes\n2. No, continue")
            choice = input("Enter Here: ")

            if choice == "1":
                ability_scores()  # Redirect to ability scores
                return  # Exit current function after redirect
            elif choice == "2":
                return  # Exit if they choose to continue
            else:
                print("Invalid Option...")
    else:
        print(f"Fetch Failed for {new_as_url}, Error Code: {new_as_response.status_code}")

# Used ChatGPT for the creation of this function.
# Wanted to see a usage of a dictionary in Python
# Gives the user a standard array of points to allocate to the abilities of their choice
def as_allocation():
    # Standard array of ability scores
    standard_array = [15, 14, 13, 12, 10, 8]
    abilities = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
    assigned_scores = {}

    print("\nYou will allocate the following standard array of ability scores:\n"
          + "15, 14, 13, 12, 10, 8\n")

    for ability in abilities:
        while True:
            print("Available scores:")
            for score in standard_array:
                print(f"- {score}")
            try:
                score = int(input(f"Assign a score to {ability}: "))
                if score in standard_array:
                    assigned_scores[ability] = score
                    standard_array.remove(score)  # Remove assigned score from available scores
                    break
                else:
                    print("Invalid choice. Please select from the available scores.")
            except ValueError:
                print("Invalid input. Please enter a number from the available scores.")
    
    # Assign allocated scores to the character
    character.strength = assigned_scores["Strength"]
    character.dexterity = assigned_scores["Dexterity"]
    character.constitution = assigned_scores["Constitution"]
    character.intelligence = assigned_scores["Intelligence"]
    character.wisdom = assigned_scores["Wisdom"]
    character.charisma = assigned_scores["Charisma"]

    # Display allocated scores
    print("\nYour character's ability scores have been allocated as follows:")
    for ability, score in assigned_scores.items():
        print(f"{ability}: {score}")

def start():
    print("\nWelcome to the D&D character creator! You will choose what class and race your character will have."
          + "You will also allocate your ability points to finish your character stats.\n")

    character_classes()
    races()
    ability_scores()
    as_allocation()

    print(character.__repr__())

start()