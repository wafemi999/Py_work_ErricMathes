age = 22
if age < 4:
	print("your admission fee is $0")
elif age < 18:
	print("your admission fee is $5 ")
else:
	print("your admission fee is $10")
	
print("\n method two:")
#method two with dicount for ages > 65yrs:
age = 65
if age < 4:
	price = 0 

elif age < 18:
	price = 5
 
elif age < 65:
	price = 10
	
else:
	price = 5
	
print("your admission cost is $",str(price),".")

print('\n')
#omitting the ELSE block; using the ELIF @ the end:
age = 65
if age < 4:
	price = 0 

elif age < 18:
	price = 5
 
elif age < 65:
	price = 10
	
elif age >=65:
	price = 5
	
print("your admission cost is $",str(price),".")

print("\n")
#multiple condition testing 

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
	print("adding mushrooms. ")
	
if 'extra cheese' in requested_toppings:
	print("adding extra cheese. ")
	
if 'pepperroni' in requested_toppings:
	print("adding pepperroni. ")
	
print("\nfinished making your pizza")



