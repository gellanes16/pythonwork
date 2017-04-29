# 4/22/17 - Introduction to lists.
favorite_foods = ['egg', 'bacon', 'sausage']
print (favorite_foods[0])
print (favorite_foods[1])
print (favorite_foods[2])

favorite_foods.append('cheese')
print (favorite_foods)

tennis_players = ['Roger Federer', 'Rafael Nadal', 'Andy Murray']

tennis_players.append('Sam Groth')

print (tennis_players)
tennis_players.insert(1, 'Novak Djokovic')
print (tennis_players)

del tennis_players[1]
print (tennis_players)

print ("My favorite tennis player is " + tennis_players[0])

popped_player = tennis_players.pop()
print ("A tennis player who will probably never win the Australian Open is " + popped_player.upper() + "!")
first_player = tennis_players.pop(0)
print ("A tennis player who will win another Aussie is " + first_player.upper() + "!")

tennis_players.remove('Rafael Nadal')
print (tennis_players)

too_british = 'Andy Murray'
tennis_players.remove(too_british)
print (tennis_players)
print ("\n" + too_british + " was removed from the list because he is too British.")


print (favorite_foods)

print (sorted(favorite_foods))

favorite_foods.reverse()
print (favorite_foods)

foods_length = len(favorite_foods)
print (foods_length)



