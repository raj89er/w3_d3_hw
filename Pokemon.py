
# pip install requests

import requests

requests


poke_base_url = "https://pokeapi.co/api/v2/"

# Class for pokemon name, height, weight, and types
class Pokemon:
    def __init__(self, name, height, weight, types):
        self.name = name
        self.height = height
        self.weight = weight
        self.types = types

    def __str__(self):
        return f"Name: {self.name}, Height: {self.height}, Weight: {self.weight}, Types: {', '.join(self.types)}"

# Class for berry name, size, and flavors
class Berry:
    def __init__(self, name, size, flavors):
        self.name = name
        self.size = size
        self.flavors = flavors

    def __str__(self):
        return f"{self.name}: Size - {self.size}, Flavors - {', '.join(self.flavors)}"


# Function to get pokemon info
def req_pkmn_info(pokemon_input):
    req_url = f"{poke_base_url}pokemon/{pokemon_input}"
    res = requests.get(req_url)
    if res.status_code == 200:
        data = res.json()
        # Info to be extracted from JSON at Pokemon level
        name = data["name"]
        height = data["height"]
        weight = data["weight"]
        types = [t['type']['name'] for t in data['types']]
        return Pokemon(name, height, weight, types)
    else:
        return None

# funtion to print pokemon info
def print_pkmn_info(pokemon):
    if pokemon is None:
        print("#"*77)
        print("No Pokemon found with that name or ID.")
        print("Please try again or have some coffee and try again later.")
        print("#"*77)
    else:
        print("#"*77)
        print(pokemon)
        print("#"*77)
    
# Function to print berry info
def req_berry_info(berry_input):
    req_url = f"{poke_base_url}berry/{berry_input.lower()}"
    res = requests.get(req_url)
    if res.status_code == 200:
        data = res.json()
        # Info to be extracted from JSON at Berry level
        name = data["name"]
        size = data["size"]
        flavors = [f['flavor']['name'] for f in data['flavors']]
        return name, size, flavors
    else:
        return None

# Function to print berry info
def print_berry_info(berry):
    if berry is None:
        print("#"*77)
        print("No Berry found with that name or ID.")
        print("Please try again or have some coffee and try again later.")
        print("#"*77)
    else:
        print("#"*77)
        print(berry)
        print("#"*77)

def main():
    print("#"*77)
    print("Welcome to the Mini-Pokedex!")
    print("What would you like to do?")
    print("1) Search for a Pokemon")
    print("2) Get information about a Berry")
    print("3) Quit")
    print("#"*77)

    while True:
        option = input("Enter your choice (1/2/3): ")
        
        if option == "1":
            pokemon_input = input("Enter a Pokemon name or ID: ").lower()
            pokemon = req_pkmn_info(pokemon_input)
            if pokemon:
                print_pkmn_info(pokemon)
            else:
                print("#"*77)
                print("No Pokemon found with that name or ID.")
                print("Please try again or have some coffee and try again later.")
                print("#"*77)
        
        elif option == "2":
            berry_input = input("Enter a Berry name or ID: ").lower()
            berry = req_berry_info(berry_input)
            if berry:
                print_berry_info(berry_input)
            else:
                print("#"*77)
                print("No Berry found with that name or ID.")
                print("Please try again or have some coffee and try again later.")
                print("#"*77)
        
        elif option == "3":
            print("#"*77)
            print("Exiting the Pokedex.")
            print("#"*77)
            break
        
        else:
            print("#"*77)
            print("Invalid choice! Please enter 1, 2, or 3.")
            print("#"*77)
            
if __name__ == "__main__":
    main()
