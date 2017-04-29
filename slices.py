odd_numbers = list(range(1,21,2))
print(odd_numbers)

print("The first three numbers in the list are " + str(odd_numbers[0:3]))
print("Three numbers from the middle of the list are " + str(odd_numbers[3:6]))
print("The last three numbers in the list are " + str(odd_numbers[-3:]))

my_pizzas = ['sausage','pepperoni','cheese']
friend_pizzas = my_pizzas[:]

my_pizzas.append('marghertia')
friend_pizzas.append('veggie')

for mypizza in my_pizzas:
	print(mypizza.title() + " is a pizza that I like.")
print("")
for friendpizza in friend_pizzas:
	print(friendpizza.title() + " is a pizza that my friend likes.")
	


