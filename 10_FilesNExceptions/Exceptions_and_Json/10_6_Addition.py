
try:
	first_number = int(input("enter first number"))
	sec_number = int(input("enter second number"))
	result = first_number + sec_number
except ValueError:
	print("you entered a letter instead of a number")
else:
	print(result)
		
	
