
print("parrot.py")
message = input("Tell me something, and i will repeat it back to you: ")
print(message)

print("\ngreeter:")
name = input("please enter your name: ")
print("hello "+name+" !")

print("\ngreeter:")
prompt = "if you tell us who you are we can personalise the messages you see"
prompt += "\n what is your first name? "

name = input(prompt)
print("hello "+name+"!")


print("\nNumerical input:")

age = input("How old are you? ")
print(age)


print("\nROller COASTER.py:")
height = int(input("How tall are you, in inches? "))
# or height = int(height)
print(height)

if height >= 36:
	print("you are tall enough to ride")
else:
	print("You will be able to ride when you are a little older")
	



print("\neven or odd.py:")
number = int(input("tell me a number, and i will tell if it is odd or even: "))
print(number)

if number % 2 == 0:
	print("\n The number "+ str(number)+ " is even.")
else:
	print("\n The number "+ str(number)+ " is odd.")


#ex 7
print("\n execise 7-1 rental cars:")
rentals = input("what kind of rental car would you like: ")
print(rentals)
print("let me see if i can find you a "+rentals)


print("\n execise 7-2 renstaurant seating:")
dinner = "How many people do you have in your dinner group? "
reserve = int(input(dinner))

if reserve > 8:
	print("please wait for a table ")
else:
	print(" your table is ready ")

	
print("\n execise 7-1 multiple of 10:")
multiple_10 = int(input("please enter a number and i will tell you if it's a multiple of 10: "))
print("you entered: ",multiple_10)
a = multiple_10
print("\n a = ",a)

if a % 10 == 0:
	print(a," is  a multiple of ten")
else:
	print(a," is not a multiple of ten ")
