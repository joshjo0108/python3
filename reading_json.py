import json


# STRING FORM json
c3p0 = '''{
	"name": "C-3PO",
	"height": "167",
	"mass": "75",
	"hair_color": "n/a",
	"skin_color": "gold",
	"eye_color": "yellow",
	"birth_year": "112BBY",
	"gender": "n/a",
	"homeworld": "https://swapi.dev/api/planets/1/",
	"films": [
		"https://swapi.dev/api/films/1/",
		"https://swapi.dev/api/films/2/",
		"https://swapi.dev/api/films/3/",
		"https://swapi.dev/api/films/4/",
		"https://swapi.dev/api/films/5/",
		"https://swapi.dev/api/films/6/"
	],
	"species": [
		"https://swapi.dev/api/species/2/"
	],
	"vehicles": [],
	"starships": [],
	"created": "2014-12-10T15:10:51.357000Z",
	"edited": "2014-12-20T21:17:50.309000Z",
	"url": "https://swapi.dev/api/people/2/"
}'''
# LOAD IN json FORMAT WITH THE GIVEN c3p0 STRING
c3p0 = json.loads(c3p0)

# CHANGE THE NAME
c3p0['name'] = "Jae Won Jo"
# UPDATE THE UPDATED c3p0
c3p0_str = json.dumps(c3p0)
# PRINT THE NAME
print(c3p0['name'])
print(c3p0_str)