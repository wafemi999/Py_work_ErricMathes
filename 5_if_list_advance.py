requested_toppings = ["mushroom", "green peppers", "extra cheese"]
for requested_topping in requested_toppings:
	print("Adding ",requested_topping," .")
print("Finished making your pizza")

print("\n")
#pizzeria 2
requested_toppings = ["mushroom", "green peppers", "extra cheese"]
for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("sorry we are out of green peppers")
	else:
		print("Adding ",requested_topping,".")
print("Finished making your pizza")

#checking for an empty list:
print("\n")
requested_toppings = []
if requested_toppings:
	for requested_topping in requested_toppings:
		print("Adding ",requested_topping," .")
	print("\n Finished making your pizza")
else:
	print("are you sure you want a plain pizza?")
	
	
print("\n")
#using multiple lists:
availabe_toppngs = ['mushrooms', "green peppers", "olives", "pepperoni", 'pineaple', 'extra cheese']
requested_toppings = ["mushrooms", "french fries", "extra cheese"] 
for requested_topping in requested_toppings:
	if requested_topping in availabe_toppngs:
		print("Adding ", requested_topping,".")
else:
	print("Sorry we don't have ", requested_topping, ".")
print("finished making your pizza")


#exercise 5-8 hello admin:
print("\n Hello Admin:")
names = ['admin', 'eric', 'femi', 'manuel', 'segun']
for name in names:
	if name =='admin':
		print("hello ",name ,"would you like to see a status report.")
	else:
		print("hello ", name," Thank you for logging in again.")


#5-9 No users
print("\n no users test:")
names = [] #remove list to see clearer output
if names:
	for name in names:
		if name =='admin':
			print("hello ",name ,"would you like to see a status report.")
		elif name !='admin':
			print("hello ", name," Thank you for logging in again.")
else:
	print("we need more users")


#5-10 checking user names:
print("\n checking user names:")
current_users = ['vicky09', 'eric', 'femi', 'manuel', 'segun']
new_users = ['vicky09', 'tola','FEMI', 'femi007','dimi99']
for new_user in new_users:
	if new_user.lower() in current_users:
		print("\n please enter a new username ",new_user)
	else:
		print(" \n Username is available ", new_user)


#5-11 ordinal numbers:*****
print('\n Ordinal numbers:')
ord_no = [1,2,3,4,5,6,7,8,9]
for i in ord_no:
	if i ==1:
		order = 'st'
	elif i ==2:
		order = 'nd'
	elif i ==3:
		order == 'rd'
	else:
		order = 'th'
	print("\n ",i,order)



