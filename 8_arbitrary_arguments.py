#pizza.py
print("\n make pizza:")
def make_pizza(*toppings):
	'''showing all Pizzas'''
	print(toppings)
make_pizza('pepperroni' )
print("\n shows it takes more > 1 arguments")
make_pizza('mushroom', 'green peppers', 'extra cheeze')


print("\n pizza.py2")
#pizza.py
print(" make pizza:")
def make_pizza(*toppings):
	'''showing making Pizzas'''
	print("\n Making pizzas with the following toppings:")
	for topping in toppings:
		print("-", topping)

make_pizza('pepperroni' )
make_pizza('mushroom', 'green peppers', 'extra cheeze')


print("\n Mixing Positional and Arbitrary Arguments pizza.py2")
def make_pizza(size,*toppings):
	'''mixing'''
	print("\n making a  "+ str(size), "-inch pizza with the following toppings:")
	for topping in toppings:
		print("-", topping)
		
make_pizza(15, 'extra cheese')
make_pizza(8, 'mushroom','green peppers', 'extra cheese')



print("\n build profile Using Arbitrary Keyword Arguments:")
def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user."""
	profile = {}
	profile['first name:'] = first
	profile['last name:'] = last
	for key, value in user_info.items():
		profile [key] = value
	return profile
		
user_1 = build_profile('mauel', 'oyelola', age = '23', location = 'New Jersey',
 discipline = 'computer science ')
print(user_1) 
