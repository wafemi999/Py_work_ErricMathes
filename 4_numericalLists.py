for value in range(1,11):
	print(value,")")

#converting a range() 0f numbers into a list()
print("\n")
numbers = list(range(0,11))
print(numbers)


print("\n")
#even numbers
even_numbers = list(range(2,21,2))
print(even_numbers)

print("\n")

#first 10 square number 
print("the square of each integer between 1 and 10 :")
squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)
print(squares)

print("\n")
#method2 first 10 square number 
print("the square of each integer between 1 and 10 :")
squares = []
for value in range(1,11):
	squares.append(value**2)
print(squares)

#making your code more concise:
print("\n")
print("list comprehension:")
sqaures = [values**2 for values in range(1,11)]
print(squares)


print("\n")
#simple statistics with numbers
print("min, max, sum :")
digits = list(range(1,10))
print("sum = ",sum(digits))
print("minimum digit  = ", min(digits))
print("maximum digit = ", max(digits))



