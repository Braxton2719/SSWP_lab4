import requests
from pydantic import ValidationError

# dedicated to making API requests to view the class options
def character_classes():
    class_url = "https://www.dnd5eapi.co/api/2014/classes"
    class_headers = {'Accept': 'application/json'}

    class_response = requests.get(class_url, headers=class_headers)
    if class_response.status_code == 200: # successful, do work
        classes_data = class_response.json()
        classes = classes_data['results']

        print("Starting off with character class, the available classes are:\n"
              + "--------------------------------------------------------------\n")
        for each_class in classes:
            print(each_class['name'])
    else:
        print(f"Fetch Failed, Error Code: {class_response.status_code}")
    return

def start():
    print("\nWelcome to the D&D character creator! You will choose what class and race your character will have."
          + "You will also allocate your ability points to finish your character stats.\n")

    character_classes()

start()