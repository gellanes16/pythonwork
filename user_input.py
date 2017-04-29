#desired_car = input("Welcome to Gerard's Cars! Please tell us what kind of car you would like today: ")
#print("Okay, we'll try to find you a " + desired_car + ".")

#family_size = input("Welcome to Olive Garden. How many in your group today? ")
#family_size = int(family_size)
#if family_size > 8:
	#print("Sorry, you'll have to wait until a bigger table opens up.")
#else:
#	print("We have a table ready for you!")

#user_number = input("Enter a positive number. We'll tell you if that number is a multiple of 10: ")
#user_number = int(user_number)
#if user_number % 10 == 0:
#	print("Yes, that's a multiple of 10!")
#else:
#	print("No, that's not a multiple of 10.")

prompt = "Type anything you like; it will be repeated."
prompt += " If you enter 'quit', the program will end. "
message = ""
while message != 'quit':
	message = input(prompt)
	if message != 'quit':
		print(message)
	
#user_input = input("Type anything or quit. ")
#while user_input != 'quit':
#	print(user_input)
prompt = "Enter a word or quit. "
active = False
while not active:
	message=input(prompt)
	
	if message == 'quit':
		active = False
	else:
		print(message)
	


	

