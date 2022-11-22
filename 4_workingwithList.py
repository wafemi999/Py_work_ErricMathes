#simple look at FOR LOOP
magicians = ['carbonaro', 'dynamo', 'troy']
for magician in magicians:
	print(magician)
print("\n")


print("\n")
#Doing more with FOR LOOP
for magician in magicians:
	print(magician.upper(),",  that was great trick")
	print("i cant wait to see your next trick",magician.upper(),".\n")

#doing something after a for loop
for magician in magicians:
	print(magician.upper(),",  that was great trick")
	print("i cant wait to see your next trick",magician.upper(),".\n")

print("thank you everyone , that was a great magic show")


print("\n")

#ex4-3counting to twenty(20)
counting = list(range(1,21))
print(counting)
print("\n")
#counting to twenty(20) method2
for counts in counting:
	print(counts)



print("\n")

#ex4-4 one million

'''million = list(range(1,1000001))
print(million)

for millions in million:
	print(millions)
'''

print("\n")
#ex4-5 summing a million
million = list(range(1,1000001))
print("SUM of a Million:", sum(million))
print("minimum number:", min(million))
print("maximum number :",max(million))


print("\n")

#ex4-6 odd numbers (1 - 20)

odd_no = list(range(1,21,2))
for odds in odd_no:
	print(odds)

print("\n")
print("\n")
#ex4-7 THREES
threes = list(range (3,31,3))
for count_threes in threes:
	print(count_threes)

print("\n")
#ex4-8 cubes
cubes = []
for cube in range(1,11):
	cubes_result = cube**3
	cubes.append(cubes_result) 
print(cubes)
print("\n")

#ex4-9 list comprehension for cubes
cubes = [values**3 for values in range(1,11)]
print(cubes) 


print("\n")

#ex4-9 

cubes = []
for value in range(1,11):
	cubes.append(value**3)
print(cubes)
