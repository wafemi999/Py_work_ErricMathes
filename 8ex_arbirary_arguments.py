print("\n 8-12: sandwiches")
def sandwich_orders(*orders):
	'''summarizes orders'''
	print("sandwich orders are: ")
	for i in orders:
		print("- ",i)
		
sandwich_orders('french dip')
print("\n")
sandwich_orders('small bread', 'egg salad')	
print("\n")
sandwich_orders('french dip', 'small bread', 'egg salad','caprese')	


print("\n 8-13: user_profile")
def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user."""
	profile = {}
	profile['first name:'] = first
	profile['last name:'] = last
	for key, value in user_info.items():
		profile [key] = value
	return profile
wafemi = build_profile('mauel', 'oyelola', age = '23', location = 'New Jersey',
 discipline = 'computer science ',alma_mater = 'AAUA' )
print(wafemi) 


print("\n 8-14: cars:")
def make_car(m,n,**specs):
	'''show car info'''
	car = {}
	car ['MANUFACTURER'] = m
	car ['MODEL'] = n
	for i, j in specs.items():
		car [i] = j
	return car
my_car = make_car('KIA', 'stealth', color = 'blue', roof = True)
print("-------------------------------------------------------------------------------")
print(my_car)
print("-------------------------------------------------------------------------------")
