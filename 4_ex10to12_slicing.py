#ex4-10
players = ["charles", "martina", "michael","florence","eli"]
print("The first 3 elements in the list are:")
print(players[0:3])
print("\n")
print("Three  elements from the middle of the list are:")
print(players[1:4])
print("\n")
print("The last three elements in the list are :")
print(players[2:])
print("\n")

#ex4-11 myPizzas,YourPizzas
pizza = ['pepperoni', 'domino', 'kfc']
friends_pizza = pizza[:]
pizza.append('slimy')
friends_pizza.append('eggy')

print("my favourite pizzas are:")
for my_pizza in pizza:
	print(my_pizza)
print("\n")
print("my friend's favourite pizzas are:")
for friend_p in friends_pizza:
	print(friend_p)

print("\n")	
#ex4-12 All versions of food.py exercises in for loops
my_foods = ["fufu", "rice", "amala"]
friends_foods = my_foods[:]
print("my favourite foods:")
for mine in my_foods:
	print(mine)
	
print("\n")
print("\n My friend's favourite foods are:")
for i in friends_foods:
	print(i)
