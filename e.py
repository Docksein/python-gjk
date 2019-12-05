import requests


def ship_detail(ship_name):
    x = requests.get("https://swapi.co/api/starships/?search=" + ship_name).json()["results"][0]
    film_names = []
    for url in x["films"]:
        film_names.append(requests.get(url).json()["title"])
    return [x["name"], x["model"], x["starship_class"], x["hyperdrive_rating"], film_names]


def species_detail(species_name):
    x = requests.get("https://swapi.co/api/species/?search=" + species_name).json()["results"][0]
    y = requests.get(x["homeworld"]).json()
    film_names = []
    for url in x["films"]:
        film_names.append(requests.get(url).json()["title"])
    return [x["name"], x["classification"], x["designation"], y["name"], film_names]


def person_detail(name):
    x = requests.get("https://swapi.co/api/people/?search=" + name).json()["results"][0]
    y = requests.get(x["homeworld"]).json()
    film_names = []
    for url in x["films"]:
        film_names.append(requests.get(url).json()["title"])
    return [x["name"], x["gender"], y["name"], film_names]


def film_detail(filmname):
    x = requests.get("https://swapi.co/api/films/" + filmname).json()
    characters_name = []
    for url_char in x["characters"]:
        characters_name.append(requests.get(url_char).json()["name"])
    starships_name = []
    for url_ship in x["starships"]:
        starships_name.append(requests.get(url_ship).json()["name"])
    return [x["title"], x["director"], x["episode_id"], sorted(characters_name), sorted(starships_name)]


def op_crawl(namefilm):
    x = requests.get("https://swapi.co/api/films/" + namefilm).json()
    return x["opening_crawl"]

print(ship_detail("falcon"))
print(species_detail("ewok"))
print(person_detail("anakin"))
print(film_detail("3"))
print(op_crawl("5"))
