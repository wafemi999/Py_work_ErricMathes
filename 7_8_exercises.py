print("ex7-8 DELI:")
sandwich_orders =['french dip', 'small bread', 'egg salad','caprese']
finished_sandwich = []

while sandwich_orders:
	i = sandwich_orders.pop()
	print("\n i made your ",i," sandwich")
	finished_sandwich.append(i)
	print(finished_sandwich)
	
print("\n\n the following sandwiches were made:")
for i in finished_sandwich:
	print("\n",i)
	


print("\n\nex7-9 pastrami:")
sandwich_orders =['french dip', 'pastrami','pastrami', 'small bread', 'pastrami', 'egg salad','caprese']
finished_sandwich = []

print(" The deli has ran out of pastrami, available for order are:")
while 'pastrami' in sandwich_orders:
	 sandwich_orders.remove('pastrami')
	 print("\n",sandwich_orders)
print("\n finished_sandwich:") 
finished_sandwich.append(sandwich_orders)
print(finished_sandwich)



print("\n\\n nex7-10 dream vacation polling:")

responses = {}

active = True
while active:
	#this prompts thee users for inputs
	name = input("Whats your name: ")
	response = input("where would you like to have your dream vacation: ")
	
	#this stores the user name and response to dict(responses)
	responses[name] = response
	print(response)
	
	#check for continuity of the poll:
	repeat = input("Allow the next person for the poll(yes/no): ")
	
	if repeat == 'no':
		active = False
	
print("\n\t ----------poll results---------")
for i, j in responses.items():
	print(i+" would love to travel to "+ j)
	
