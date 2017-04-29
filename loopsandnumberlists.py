list_20 = list(range(1,21))
print(list_20)

list_mill = list(range(1,1000001))
print(str(min(list_mill)) + " is the min.")
print(str(max(list_mill)) + " is the max.")
print(str(sum(list_mill)) + " is the sum.")

odd_numbers = list(range(1,21,2))
for number in odd_numbers:
	print(number)
print("These are the odd numbers from 1-20.")

for value in range(1,11):
	print(value**3)

cubes = [value**3 for value in range(1,11)]
print(str(cubes) + " is the list of the first 10 cubes.")


