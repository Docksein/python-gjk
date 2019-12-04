import requests

def ship_detail(ShipName):
    x = requests.get("https://swapi.co/api/starships/?search=" + ShipName).json()["results"][0]
    return {x["name"], x["model"], x["starship_class"], x["hyperdrive_rating"]}


def species_detail(SpeciesName):
    x = requests.get("https://swapi.co/api/species/?search=" + SpeciesName).json()["results"][0]
    y = requests.get(x["homeworld"]).json()
    return {x["name"], x["classification"], x["designation"], y["name"]}


def person_detail(Name):
    x = requests.get("https://swapi.co/api/people/?search=" + Name).json()["results"][0]
    y = requests.get(x["homeworld"]).json()
    return {x["name"], x["gender"], y["name"]}


def film_detail(filmname):
    x = requests.get("https://swapi.co/api/films/" + filmname).json()["results"][0]
    return {x["title"], x["director"], x["episode_id"]}


try:
    print(species_detail("ewok"))
except IndexError as err:
    print(err)