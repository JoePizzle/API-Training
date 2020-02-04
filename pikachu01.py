#!/usr/bin/python3

import requests

#define base URL
POKEURL = "http://pokeapi.co/api/v2/pokemon/"

def main():
    
    #Make HTTP GET request using requests, and decode
    #JSON attachment as pythonic data structure
    #Augment the base URL with a limit parameter to 1000 results
    pokemon = requests.get(f"{POKEURL}?limit=1000")
    pokemon = pokemon.json()  # JSON is neededd for the destination server to return traffic to Python

    #Loop through data, and print pokemon names
    for poke in pokemon["results"]:
        #Display the values associated with 'name'
        #print(poke.get[("name"))
        print (poke.get("name"))

        print(f"Total number of Pkemon returned: {len(pokemon['results'])}")

        if __name__ == "__main__":
            main()
            
