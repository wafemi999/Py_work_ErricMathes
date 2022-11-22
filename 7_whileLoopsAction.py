print("counting.py:")
#counting 1-5 with while loops:
current_number = 1
while current_number <=5:
	print(current_number)
	current_number += 1
	
	
	
print("\n parrot.py:")
print("parrot.py")
prompt = "\n Tell me something, and i will repeat it back to you: "
prompt += "\n Enter 'quit' to end program: "
message = ""#is empty so that python has sth to check
while message != 'quit':
	message = input(prompt)
	if message != 'quit':
		print(message)



print("\n parrot.py using a FLAG:")
prompt = "\n Tell me something, and i will repeat it back to you: "
prompt += "\n Enter 'quit' to end program: "
active = True
while active:
	message = input(prompt)
	
	if message == 'quit':
		active = False
	else:
		print(message)



#using break to xit a loop:
print("\ncities.py:")
prompt = "\n please enter the name of the city you have visited"
prompt += "\n (Enter quit when you are finished): "

while True: #this runs forever untill:
	city = input(prompt)
	
	if city == "quit":
		break
	else:
		print("i'd love to visit "+city.title()+" !")


#using continue in a loop:
print("\ncounting odd no btw 1-10.py:")
current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue
	print("\n", current_number)




#Avoiding infinite loop:
print("\n counting.py:")
x = 1
while x <=5:
	print("\n", x)
	x += 1 #omitting this leads to an infinite loop

