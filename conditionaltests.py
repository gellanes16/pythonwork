value = 1
print ("Is value == 1? I predict YES.")
value == 1
print ("\nIs value == 2? I predict NO.")
value == 2

missingword = "house"
print ("\nIs missingword == 'house'? I predict YES.\n")
missingword == 'house'
print ("Is missingword == 'home'? I predict NO.\n")
missingword == 'home'

cap_word = "Hello"
print (cap_word == "hello")
print (cap_word.lower() == "hello")

drinkingage = 21
person_1_age = 23
person_2_age = 16
no_message = "No, you're too young!"
print ("Person 1: Can I get a drink? I'm 23.")
if person_1_age >= 21:
	print ("Sure, go ahead!")
else:
	print (no_message)
print("Person 2: Can I get a drink too? I'm 16.")
if person_2_age >= 21:
	print("Sure, go ahead!")
else:
	print(no_message)

print("Can you get a drink for the both of us?")
if person_1_age >= 21 and person_2_age >= 21:
	print("Yes, of course!")
else:
	print("No, not the both of you are of legal drinking age!")

print("How about for just one of us?")
if person_1_age >= 21 or person_2_age >= 21:
	print("Sure, but only one.")

login_message = "Sure, go ahead."
denial_message = "No, you're banned."
banned_users = ['gerard', 'gabriel', 'ben']
print("Gerard: May I login?")
if 'gerard' in banned_users:
	print(denial_message)
else:
	print(login_message)

print("Mom: May I login?")
if 'mom' not in banned_users:
	print(login_message)
else:
	print(denial_message)

alien_color = 'blue'
if alien_color == 'green':
	print("You have just earned 5 points!")
elif alien_color == 'yellow':
	print("You have just earned 10 points!")
else:
	print("You have just earned 15 points!")

family_ages = [1,3,15,33,34,79]
for age in family_ages:
	if age < 2:
		print("You are a baby.")
	elif 2 <= age < 4:
		print("You are a toddler.")
	elif 4 <= age < 13:
		print("You are a kid.")
	elif 13 <= age < 20:
		print("You are a teen.")
	elif 20 <= age < 65:
		print("You are an adult.")
	else:
		print("You old tho!")

available_foods = ['burger','french fries','pizza']
requested_foods = ['burger','pizza','pasta']

for requested_food in requested_foods:
	print("I would like a " + requested_food + ".")
	if requested_food in available_foods:
		print("Sure, we can get that for you.")
	else:
		print("Sorry, we don't have that today.")

username_list = ['admin','gerard01','gabriel01','ben01']
for username in username_list:
	print("Logging in " + username + ".")
	if username == 'admin':
		print("Hello admin, would you like to see a status report?")
	elif username != 'admin':
		print("Hello, " + username + ", thank you for logging in.")

new_username_list = []
if new_username_list:
	print("There are users.")
else:
	print("We need to find some users!")

current_users = ['gerard01','ben01','gabriel01','grace01','hubert01']
new_users = ['gerard01','danny01','brian01','gRaCe01','john01']

for new_user in new_users:
	print("Enter username: " + new_user)
	if new_user.lower() not in current_users:
		print("Username available.")
	elif new_user.lower() in current_users:
		print("Sorry, that username is taken.")
		
numbers_list = list(range(1,10))

for val in numbers_list:
	if val == 1:
		print(str(val) + "st")
	elif val == 2:
		print(str(val) + "nd")
	elif val == 3:
		print(str(val) + "rd")
	else:
		print(str(val) + "th")




		

		









