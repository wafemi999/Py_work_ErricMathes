players = ["charles", "martina", "michael","florence","eli"]
print(players[:5])#prints the first three element of the list
print(players[1:4])#prints the 2nd, 3rd and 4th element of a list
print(players[:4])#omitting the first index sets python to start with index0
print(players[2:])#omitting the 2nd index prints the rest of the items
print(players[-3:0])
print(players[3:])#prints the 3rd element to the end of the list 
print("\n")
#looping through a slice list
print("the first 3 elements through loop:")
for player in players[0:3]:
	print(player.upper())
	

#Copying a list i.e creatinga new list from an existing list
my_foods = ["fufu", "rice", "amala"]
friends_foods = my_foods[:]

print("These are my favourite foods:")
print(my_foods)
print("\n")
print("my friends favourite food")
print(friends_foods)
print("\n")
#proof the lists operate independently
my_foods.append('doughnut')
print("These are my favourite foods:")
print(my_foods)
print("\n")

friends_foods.append('ice cream')
print("my friends favourite food")
print(friends_foods)
