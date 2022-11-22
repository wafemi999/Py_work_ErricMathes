dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

'''dimensions[0] = 250 #proofs tuples dont change unlike list'''

print("\n looping through a tuple")
print("original dimensions:")
for dimension in dimensions:
	print(dimension)

print("\n")
print("Modified Dimensions")
dimensions = (400,100)
for dimension in dimensions:	
	print(dimension) 
print("\n")

#ex4-13 buffet

food_box = ("pie", "rice", "beans", "Suya", "amala")
for food in food_box:
	print(food)

'''
food_box[1] = "fanta"
print(food_box[1])
#proofs you cant assign to a tuple
'''

print("\n Revised food box")
revised_menu = ("pie", "rice", "beans", "yam", "eba")
for i in revised_menu:
	print(i)
	
