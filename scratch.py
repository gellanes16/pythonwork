for value in range(1,6):
	print ("The number is " + str(value) + ".")
print("The multiples of 3 are...")
multiples_3 = list(range(3,31,3))
for multiple in multiples_3:
	print(multiple)
	
print("and so on.")
print("The first ten perfect squares are:")
squares_list = []

for value in range(1,11):
	squares_list.append(value**2)
print(squares_list)

print(list(range(2,11,2)))

numbers = list(range(1,11))
print ("Here are the numbers 1-10: " + str(numbers))
print("The maximum number is " + str(max(numbers)))
print("The minimum number is " + str(min(numbers)))
print("The sum of all of these numbers is " + str(sum(numbers)))

names = ['bob','mike','bryan','federer','nadal']
print(str(names[0:3]).title())
print(names[:3])
print(names[2:])
print(names[-3:])

for name in names[2:]:
	print(name.title() + " is a good tennis player.")
for name in names[:2]:
	print(name.title() + " is not a good tennis player.")

	
my_foods = ['pizza', 'ice cream', 'burger']
for myfood in my_foods:
	print(myfood.title() + " is a food that I like.")

friend_foods = my_foods[:]
for friendfood in friend_foods:
	print(friendfood.title() + " is a food that my friend likes.")
	
my_foods.append('cake')
friend_foods.append('chocolate')
print(my_foods)
print(friend_foods) 

tuple_greeting = ('hello','hi')
print(str(tuple_greeting) + " is the original tuple.")
tuple_greeting = ('howdy', 'hey')
print("However, you can modify a tuple: ")
for greeting in tuple_greeting:
	print(greeting)

#IF STATEMENTS########################################################

clean_list = ['clean1','clean2','clean3','dirty1']

print("Not all items in my list are clean:\n" + str(clean_list))
print("Deleting dirty items...")

for item in clean_list:
	if item == 'dirty1':
		clean_list.remove(item)
	else:
		print(item)
print("The dirty item is gone!")

time = "9:00"
if time != "9:00":
	print ("It's not time yet!")
else:
	print ("Time to go!")

value = "hello"
value_1 = "hey"

if value == "hey" and value_1 == "hey":
	print ("YES!")
else:
	print ("Conditions not met!")
	

values = ['item_0', 'item_1', 'item_2']

if 'item_0' in values:
	print ("Yes, Item 0 is in the list!")
else:
	print ("Nope, that value is not in the list!")
	
if 'item_3' not in values:
	print ("No, Item 3 is not in the list!")

family_ages = [3, 15, 18, 60]
for age in family_ages:
	if age < 4:
		price = 0
	elif 4 <= age < 18:
		price = 5
	else:
		price = 10
	print("Your price is $" + str(price) + ".")

requested_toppings = ['mushrooms','extra cheese']

if 'mushrooms' in requested_toppings:
	print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
	print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
	print("Adding extra cheese.")

print("\nFinished making the pizza!")



colors = {'danny': 'blue','gabe':'green','ben':'orange', 'brian':'yellow'}
friends_list = ['danny','brian']
for name in colors.keys():
	print(name + " likes the color " + colors[name])
	
	if name in friends_list:
		print("BTW, " + name + ", your color sucks!")

for name in sorted(colors.keys()):
	print(name)

new_list = ['hello','hi','hey','hello']
print(new_list)
new_list = set(new_list)
print(new_list)

gerard = {'age': 16,'last_name':'llanes'}
brian = {'age':16, 'last_name':'saranec'}
danny = {'age':17, 'last_name':'zaragoza'}

people = [gerard,brian,danny]

for person in people:
	print(person)

aliens = []
for alien_number in range(1,31):
	 new_alien = {'color':'green','points':5,'speed':'slow'}
	 aliens.append(new_alien)

for alien in aliens[:5]:
	print(alien)

print("Total number of aliens: " + str(len(aliens)))


number = 1
while number <= 10:
	print(number)
	number = number + 1














		

		
	









	

