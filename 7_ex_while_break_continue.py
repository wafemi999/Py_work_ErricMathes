'''print("\n Ex 7-4 pizza toppings using an active FLAG:")
prompt = "\n please enter toppings you want on your pizza"
prompt += "\n Enter 'quit' when true: "
active = True
while active:
	a = input(prompt)
	
	if a == 'quit':
		active = False
	else:
		print("\n",a.upper()," will be added")
'''

'''print("\n \n \n EX7-5  movie tickets:")

prompt = "\n Please enter your age here: "

a = int(input(prompt))

if a < 3:
	print("ticket is free")
elif a < 12:
	print("ticket cost is $10 ")
else:
	print("ticket cost is $15")


print("\n \n\nex 7-6 Three exits:")
print(" pizza toppings using condition in while:")
prompt = "\n please enter toppings you want on your pizza"
prompt += "\n Enter 'quit' when true: "

while a != 'quit':
	a = input(prompt)
	
	if a != 'quit':
		print("\n",a.upper()," will be added")
		
		
		
		
print("\n \n\npizza toppings using continue in a loop:")
prompt = "\n please enter toppings you want on your pizza"
prompt += "\n Enter 'quit' when through: "

while True:
	a = input(prompt)
	
	if a == 'quit':
		break
	else:
		print("\n",a.upper()," will be added")
		
		
		
'''		
print("\n \n \n EX7-6  movie tickets conditional while And break ")
prompt = "\n Please enter your age here: "

a = int(input(prompt))
while a != "":
	
	if a < 3:
		p = '$5'
	elif a < 12:
		p = '$10'
	else:
		p = '$15'
	print("ticket cost is: ",p)
	break
	
print("\n \n \n EX7-6 movie tickets ACTIVE variable while")
prompt = "\n Please enter your age here: "

active = True
a = int(input(prompt))	
while active:
	
	if a < 3:
		p = '$5'
	elif a < 12:
		p = '$10'
	else:
		p = '$15'
	print("ticket cost is: ",p)
		active =False
	
	
	
print("\n \n \n EX7-7 infinite loop")
prompt = "\n Please enter your Y for 'yes' or N for 'NO' to see an infinite loop: "
x = input(prompt)	
while x == 'y' or 'n':
	print("jbiviwurgbfuworbgfirgugiwrbgirwgfiwrgfirwgoirwgfrwgfowrgouwrgfurwgfuorwgfwrugfuwrogourwg")

