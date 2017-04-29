gerard_llanes = {
	'name':'gerard llanes',
	'age':16,
	'school':'la canada',
	}
brian_saranec = {
	'name':'brian saranec',
	'age':16,
	'school':'loyola',
	}
john_cruz = {
	'name':'john cruz',
	'age':17,
	'school':'providence'
	}

people = [gerard_llanes,brian_saranec,john_cruz]
for person in people:
	name = person['name'].title()
	age = str(person['age'])
	school = person['school']
	print(name + " is " + age + " years old and goes to " + school.title() + ".")

print("")

bandit = {
	'name':'bandit',
	'owner':'gerard',
	'animal':'dog',
	}
arthur = {
	'name':'arthur',
	'owner':'gabriel',
	'animal':'cat',
	}
bubbles = {
	'name':'bubbles',
	'owner':'ben',
	'animal':'fish',
	}
pets = [bandit,arthur,bubbles]
for pet in pets:
	name = pet['name'].title()
	owner = pet['owner'].title()
	animal = pet['animal']
	print(name + " is a " + animal + " and his owner is " + owner + ".")

print("")

favorite_places = {
	'Gerard':['Joshua Tree','Sequoia'],
	'Gabriel':['Yosemite','Yellowstone','Pinnacles'],
	'Ben':['Zion','Grand Canyon','Grand Teton'],
	}
	
for person, places in favorite_places.items():
	print(person + "'s favorite places are: ")
	for place in places:
		print(place + " National Park")
	print("")

cities = {
	'Los Angeles':{
		'country':'United States',
		'population':3000000,
		'attraction':'Griffith Observatory',
		},
	'Madrid':{
		'country':'Spain',
		'population':4000000,
		'attraction':'Plaza Mayor',
		},
	'New York':{
		'country':'United States',
		'population':8000000,
		'attraction':'Wall Street',
		},
	}

for city, info in cities.items():
	print("Facts about " + city + ":")
	country = info['country']
	population = str(info['population'])
	attraction = info['attraction']
	print("\tCountry: " + country)
	print("\tPopulation: " + population)
	print("\tAttraction: " + attraction)
	
gellanes = {
	'first_name':'Gerard',
	'last_name':'Llanes',
	'age':16,
	'city':'La Canada',
	}

print(gellanes['first_name'] + " " + gellanes['last_name'] + " is " + str(gellanes['age']) + " and lives in " + gellanes['city'] + ".")


	



