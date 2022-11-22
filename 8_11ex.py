print("\n ex8_9")
def show_magicians(names):
	'''performing magicians Today:'''
	for name in names:
		print(name)
		
usernames = ['carbanaro','Ineffect', 'dr. Octopus']
show_magicians(usernames)



print("\n ex8_10")
def make_great(names):	
	''''''
	while names:
		greet_magician = names.pop()
		msg = "The Great "+ greet_magician + "."
		print(msg)
	
		

print("GREETINGS")
make_great(usernames)
print("\n")
print("(empty to show modification)PERFORMING MAGICIANS TODAY:")		
show_magicians(usernames)


print("\n \n \n ex8_11 unchanged magicians:")
def make_great(names):	
	'''GREETINGS'''

	while names:
		greet_magician = names.pop()
		print("The Great ", greet_magician , ".")
		
usernames = ['carbanaro','Ineffect', 'dr. Octopus']	
make_great(usernames[:])
new_seperate_list = [usernames]


'''
while usernames:
	seperate_list = usernames.pop()
	new_seperate_list.append(seperate_list)
'''

#re check for better modification
print("\n calling show_magicians with original list:")
show_magicians(usernames)
print("\n calling show_magicians with new list:")
show_magicians(new_seperate_list)
print("\n calling mahe_great magicians with new list:")
make_great(new_seperate_list)




