import requests

req = requests.get("https://swapi.dev/api/people/2/")
# IF THE DATA WE GET IS json FORMAT
# TURN JSON INTO DICTIONARY
person = req.json()

print(person)
print(f"Name is {person['name']}")
print(f"Birth year is {person['birth_year']}")

print("Films involved in...")
i = 0

for film in person['films']:
    req = requests.get(film)
    film = req.json()
    print(f"Film {i} is: {film['title']}")
    i += 1