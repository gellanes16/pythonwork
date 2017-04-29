# 4/22/17 - Lists!
guest_list = ['Danny', 'Brian', 'John', 'Derek']
print("First three guests: " + str(guest_list[0:3]))


message_1 = "You're invited to dinner, "

print (message_1 + guest_list[0] + "!")
print (message_1 + guest_list[1] + "!")
print (message_1 + guest_list[2] + "!")
print (message_1 + guest_list[3] + "!")

noshow_guest = guest_list.pop(1)
print ("Unfortunately, " + noshow_guest + " cannot make it to dinner.")

guest_list.insert(1, 'Louie')

message_2  = "You're still invited, "
print (message_2 + guest_list[0] + "!")
print (message_2 + guest_list[2] + "!")
print (message_2 + guest_list[3] + "!")
print (message_1 + guest_list[1] + "!")

print ("We just found more guests to attend!")

guest_list.insert(0, 'Hector')
guest_list.append('Elliot')

print (message_1 + guest_list[0] + "!")
print (message_1 + guest_list[5] + "!")

print ("Bad luck. The new table didn't arrive, and now only two people can come over.")

message_sorry = "Sorry, but you can't come over anymore, " 

popped_guest_1 = guest_list.pop()
print (message_sorry + popped_guest_1 + ".")
popped_guest_2 = guest_list.pop(3)
print (message_sorry + popped_guest_2 + ".")
popped_guest_3 = guest_list.pop(3)
print (message_sorry + popped_guest_3 + ".")
popped_guest_4 = guest_list.pop(2)
print (message_sorry + popped_guest_4 + ".")

print (message_2 + guest_list[0])
print (message_2 + guest_list[1])

del guest_list[1]
del guest_list[0]

print ("My list is now empty:")
print (guest_list)

print (str(len(guest_list)))







