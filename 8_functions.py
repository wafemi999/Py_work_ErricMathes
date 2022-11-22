print("defining a function:")

def greet_user():
	"""display a simple greeting"""
	print("hello")
greet_user()

print("\npassing information to a function:")

def greet_user(username):
	"""display a simple greeting"""
	print("hello "+ username.title()+"!")
greet_user('jesse')




#positional arguments
print("\n positional arguments describe_pets:")
def describe_pets(animal_type, pet_name):
	'''display informaion about a pet:'''
	print("\n i have "+ animal_type.title()+ '.')
	print("my "+ animal_type+ "'s name is "+pet_name)
describe_pets('hamster', 'harry') 



print("\n multiple function calls describe_pets:")

def describe_pets(animal_type, pet_name):
	'''display informaion about a pet:'''
	print("\n i have a "+ animal_type.title()+ '.')
	print("my "+ animal_type+ "'s name is "+pet_name)
describe_pets('hamster', 'harry') 
describe_pets('bird','linny')



print("\n using keyword arguments describe_pets:")

def describe_pets(animal_type, pet_name):
	'''display informaion about a pet:'''
	print("\n i have a "+ animal_type.title()+ '.')
	print("my "+ animal_type+ "'s name is "+pet_name)
describe_pets(animal_type = 'hamster', pet_name = 'harry') 
describe_pets(animal_type = 'bird',pet_name = 'linny')


print("\n using default values arguments describe_pets:")

def describe_pets(pet_name, animal_type = 'dog'):
	'''display informaion about a pet:'''
	print("\n i have a "+ animal_type.title()+ '.')
	print("my "+ animal_type+ "'s name is "+pet_name)
describe_pets(pet_name = 'harry') 
describe_pets('linny')
describe_pets(pet_name = 'jane',animal_type = 'snake',)
#equivalent function calls
describe_pets('chucky', 'hamster')
describe_pets(pet_name = 'chucky', animal_type = 'hamster')
describe_pets( animal_type = 'hamster', pet_name = 'chucky',)





print("\n\n get_formatted_name:")
def  get_formatted_name(first_name, last_name):
	'''neatly formatted names'''
	full_name = first_name.upper() + " " + last_name.title()
	return full_name
musician = get_formatted_name('oyelola', 'manuel')
print (musician)



print("\n\n get_formatted_name middle name:")
def  get_formatted_name(first_name, middle_name, last_name):
	'''neatly formatted names, middle name'''
	full_name = first_name.upper() + " " + middle_name.title() + " " + last_name.title()
	return full_name
musician = get_formatted_name('oyelola', 'manuel', 'femi')
print (musician)



print("\n\n get_formatted_name optional middle name:")
def  get_formatted_name(first_name, last_name, middle_name = ''):
	'''neatly formatted names, optional middle name'''
	if middle_name:
		full_name = first_name.upper() + " " + middle_name.title() + " " + last_name.title()
	
	else:
		full_name = first_name.upper() +  " " + last_name.title()
	return full_name
musician = get_formatted_name('oyelola', 'manuel', 'femi')
print (musician)

musician =  get_formatted_name('oyelola', 'manuel')
print(musician)


print("\n\n returning value to a dictionary:")
#build_person
def build_person(first_name, last_name):
	'''Returning value to a dictionary'''
	person = {'first':first_name.title(), 'last':last_name.upper()}
	return person
rapper = build_person('kendrick', 'lamar')
print(rapper)




print("\n\n extended build_person:")
#extended_build_person
def build_person(first_name, last_name, age='', occupation = ''):
	'''Returning value to a dictionary'''
	person = {'first':first_name.title(), 'last':last_name.upper()}
	if age:
		person['age'] = int(age)

	if occupation:
		person['occupation'] = occupation
	return person
rapper = build_person('kendrick', 'lamar', age = 31, occupation = 'student' )
print(rapper)


'''
#greeter.py without quit condition
print("\n\n using function with while loop:")
def  get_formatted_name(first_name, last_name):
''''''
	full_name = first_name.upper() + " " + last_name.title()
	return full_name
#for user input:
while True:
	print("please enter your name:")
	f_name = input("first name: ")
	l_name = input("last name: ")		
	formatted_name = get_formatted_name(f_name, l_name)
	print("\n Hello, ", formatted_name + ".")
'''


#greeter.py with quit condition
print("\n\n using function with while loop:")
def  get_formatted_name(first_name, last_name):
	'''neatly formatted names'''
	full_name = first_name.upper() + " " + last_name.title()
	return full_name
#for user input:
while True:
	print("please enter your name:")
	print("(enter 'q' to quit:")
	f_name = input("first name: ")
	
	if f_name == 'q':
		break
		
	l_name = input("last name: ")
	if l_name == 'q':
		break
				
	formatted_name = get_formatted_name(f_name, l_name)
	print("\n Hello, ", formatted_name + ".", "\n")
	
