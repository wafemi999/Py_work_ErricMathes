#simple if statement
cars = ['benz','chevrolet','bmw','suv','venza']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())
	
'''#conditional tests (equality==)
car = "bmw"
car == 'bmw'
#prints true
'''


#ignoring case when testing for inequality
car = "BMW"
car.lower == "audi"
#prints true
print("\n\n")
'''checking for inequality'''
requested_toppings = 'mush rooms'
if requested_toppings != 'anchoives':
	print("hold the anchoives")

print("\n\n")
#Numerical comparisons

age = 17
if age !=17:#change number to see the outcome
	print("Thats not the correct answer, try again")
else:
	print("true")
print("\n\n")
	
#NOT IN keyword for checking a list
banned_users = ['andrew', 'carolina', 'david']
user = 'carolina'
if user not in banned_users:
	print(user.title(),"You can post in this forum")
else:
	print(user.title(),"You have been banned from posting here")

print("\n\n")
#5-1 conditional tests 
car = 'subaru'
if car.lower() == 'Subaru':
	print("correct")
else:
	print("false")
	
print("\n\n")
print("\n conditional tests:")
students = ['tope', 'rajah', 'ife', 'femi','dimee', 'funke', 'Jide', 'betty']
if students[0] == 'tope':
	print("\n present")
else:
	print("\n false")

if students[1].lower() == "Rajah":
		print("\n present")
else:
		print("\n false")

if students[2].lower() == 'ife':
	print("\n present")
else:
	print("\n false")
	
if students[3].lower() == 'femi':
	print("\n present")
else:
	print("\n false")
	
if students[4].lower() == 'dimee':
	print("\n present")
else:
	print("\n false")
	
if students[5].lower() == 'funke':
	print("\n present")
else:
	print("\n false")
	

if students[6].lower() == 'jide':
	print("\n present")
else:
	print("\n false")
	
	
if students[7].lower() == 'BETTY':
	print("\n present")
else:
	print("\n false")
	
	print("\n test for equality & inequality:")
#ex5-2 test for equality and ineqality
laptop = 'TOSHIBA'
if laptop.upper() == 'TOSHIBA':
	print('yes')
else:
	print('no')
	
	
if laptop.upper()!='TOSHIBA':
	print("yes")
else:
	print("no")
	
print("\ntest using lower() function:")
deck = 'jiepav'
if deck.lower() =='JIEPAV':
	print('true')
else:
	print('false')

print("\n NUMERICAL TESTS:")
stud1_age = 17
stud2_age = 22

if stud1_age == stud2_age:
	print("pair")
else:
	print("dont pair") 

print("\n")
if stud1_age != stud2_age:
	print('mate')
else:
	print('dont mate')
	
print("\n")

if stud1_age < stud2_age:
	print('donate')
else:
	print("charity")

print("\n")

if stud1_age > stud2_age:
	print('give')
else:
	print('take')
	
print("\n")

if stud1_age >= stud2_age:
	print('good')
else:
	print('bad')

print("\n")
	
if stud1_age <= stud2_age:
	print('good')
else:
	print('bad')
	
print("\n")

if stud1_age<20 and stud2_age>20:
	print('permit')
else:
	print("dont permit")
	
print('\n')

if stud1_age<20 or stud2_age>20:
	print('permit')
else:
	print("dont permit")

print('\n using IN and NOT IN')

LTB5 = ['csc', 'aeb', 'bch']
if 'csc' in LTB5:
	print('proceed')
else:
	print('pause')

	
if 'ebf' not in LTB5:
	print("pause")
else:
	print("proceed")


if 'bch' in LTB5:
	print("proceed")
else:
	print('pause')

print("\n")
print("\n")
#simple IF test
age = 19
if age>=18:
	print("you are old enough to vote")
	print("have you registered to vote yet")


print("\n")
print("\n")
#simple IF-else test
age = 17
if age >=18:
	print("you are old enough to vote")
	print("have you registered to vote yet")
else:
	print("you are too young to vote")
	print("please register to vote as soon as you turn 18")
