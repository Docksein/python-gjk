import json
import requests

s = requests.get("https://swapi.co/api/starships/?search=executor")
data = json.loads(s.text)["results"][0]
print([data["name"], data["model"], data["starship_class"], data["hyperdrive_rating"]])
