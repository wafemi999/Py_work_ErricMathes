#dictionary in list line 1-72:
print("\n dictionary in LIST:")
alien_0 = {'color':'green', 'point':5,}
alien_1 = {'color':'yellow', 'point':10,}
alien_2 = {'color':'red', 'point':15,}

aliens = [alien_0,alien_1,alien_2,]
for alien in aliens:
	print(alien)
	
print("\n")
#creating aliens in a realistic way

'''make an empty list'''
aliens = []

'''making 30 green aliens:'''
for alien_number in range(30):
	new_alien = {'color':'green', 'point':5, 'speed':'slow'}
	aliens.append(new_alien)
	
'''showing the first 5 aliens:'''
for alien in aliens[:5]:
	print(alien)
print("....")#this shows you there are more


'''showing how many aliens have been created initially:'''
print("total number of aliens:",str(len(aliens)))


print("\n")

#modifying the first three aliens:
aliens = []

'''making 30 green aliens:'''
for alien_number in range(30):
	new_alien = {'color':'green', 'point':5, 'speed':'slow'}
	aliens.append(new_alien)
	
for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['point'] = 10
	
'''showing the first 5 aliens:'''
for alien in aliens[:5]:
	print(alien)
print("....")#this shows you there are more

print("\n")

	
#creating  red-fast-15ponits moving aliens from the previous code:
for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['point'] = 10
	
	elif alien ['color'] == 'yellow':
		alien ['color'] = 'red'
		alien ['speed'] = 'fast'
		alien ['point'] = 15
	
'''showing the first 5 aliens:'''
for alien in aliens[:5]:
	print(alien)
print("....")#this shows you there are more



print("\n")
#list  in a dictionary i.e list in a dictionary line 74-126:

'''piza.py'''
pizza = {
	'crust':'thick',
	'toppings':['mushrooms', 'extra_cheese']
	}
	
#summarize info abt order:
print("you ordered a "+pizza['crust']+"-crust pizza"+" with the following toppings:")

for topping in pizza['toppings']:
	print("\n", topping)


#list in a dictionary
print("\n favorite languages incorrectformat 1.py1:")

favorite_languages = {
	'jen':['python', 'ruby'],
	'sarah':['C'],
	'edward':['ruby', 'GO'],
	'phil':['python', 'haskell'],
	}
	

for name, languages in favorite_languages.items():
	if len(languages) == 1:
		print("\n"+name.title()+"'s favorite language is:"+str(languages))

	else:
		print("\n"+name.title()+"'s favorite languages are:")

	for language in languages:
		print("\t", language.upper())



print("\n favorite language(2) correct format t0 print appropriate message")

for name, languages in favorite_languages.items():
	if len(languages) > 1 :
		print("\n"+name.title()+"'s favorite languages are:")
	for language in languages:
		if len(languages)>1:
			print("\t", language.upper())
		
		elif len(languages) == 1: #or use if
			print("\n"+name.title()+"'s favorite language is:"+language.upper())
		
	
	

print("\n Dictionary in dictionary ")
#many_users.py
users = {
	'aeinstein':{
	'first':'albert',
	'last':'einstein',
	'location':'princeton',
	},
	
	'mcurie':{
	'first':'marie',
	'last':'curie',
	'location':'paris',
	},
	}
	
for username, user_info in users.items():
	print("\n USERNAME:"+ username)
	full_name = user_info['first'] +" "+ user_info['last']
	location = user_info['location']
	
	print("\t FULLNAME:"+ full_name)
	print("\t LOCATION:"+location)
