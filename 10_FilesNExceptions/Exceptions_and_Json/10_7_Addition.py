print("enter two numbers and i will add them:")
print("enter 'q' to quit")
while True:
	first_number = input("enter first number")
	if first_number == 'q':
		break
		
	sec_number = input("enter second number")
	if sec_number == 'q':
		break

	try:
		
		result = int(first_number) + int(sec_number)
	except ValueError:
		print("you entered a letter instead of a number")
	else:
		print(result)
		
	
