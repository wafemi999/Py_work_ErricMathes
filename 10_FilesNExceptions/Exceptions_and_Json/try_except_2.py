prompt = print("give me, two numbers and i will divide them ")
print("enter 'q' to quit")

while True:
	first_number = input("enter first number:")
	if first_number == 'q':
		break
	second_number = input("enter second number:")
	

	try:
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print("you cant divide by 0 \n")
	else:
		print(answer,"\n")
	
	
		
