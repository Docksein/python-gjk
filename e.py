import requests
import json


def ship_detail(ShipName):
    x = requests.get("https://swapi.co/api/starships/?search=" + ShipName)
    data = x.json()["results"][0]
    return {data["name"], data["model"], data["starship_class"], data["hyperdrive_rating"]}


def species_detail(SpeciesName):
    x = requests.get("https://swapi.co/api/species/?search=" + SpeciesName)
    data = x.json()["results"][0]
    return {data["name"], data["classification"], data["designation"]}


def person_detail(Name):
    x = requests.get("https://swapi.co/api/people/?search=" + Name).json()["results"][0]
    y = requests.get(x["homeworld"]).json()
    return {x["name"], x["gender"], y["name"]}


def film_detail(filmname):
    x = requests.get("https://swapi.co/api/films/" + filmname)
    data = x.json()["results"][0]
    return {data["title"], data["director"], data["episode_id"]}


print(person_detail("luke"))
