#confirmed users
print("\n Confirmed users:")
#start with list of users that need to be verified:

unconfirmed_user = ['alice', 'brian', 'candace',]
confirmed_Users = [] #an empty list to hold the newly verigfied users

#veRifying each user and moving them into the list of confirmed users:
while unconfirmed_user:
	current_user = unconfirmed_user.pop()
	
	#var curent_user stores each popped users from unconfirmed_user:
	#this views the current_user being verified
	print("\nverifying user: "+current_user.title())  
	confirmed_Users.append(current_user)
	
	#displaying all confirmed users:
print("\n\n The following users have been verified:")
for confirmed_User in sorted(confirmed_Users):
	print(confirmed_User.title())
	


#removing pets.py:

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print("\n\n initial pets list:", pets)

while 'cat' in pets:
	pets.remove('cat')
print("\n new 	 pets:",pets)


print("\n\n \n filling a dictionary with user input:")
#create empty dictionary 
responses = {}
#set FLAG to indicae the polling is active:
polling = True
while polling:
	print("\n prompt for the Users name and response:")
	name = input("Whats your name: ")
	response = input("Which mountain would you like to climb someday: ")
	
	#store the responses in the dictionary:
	responses [name] = response
	print(responses)
	
	#this check to see if more want to take the poll:
	repeat = input(" \n let the next person respond? yes/no :")
	if repeat == 'no':
		polling = False
#after polling results:
print("\n----poll results----")
for n, r in sorted(responses.items()):
	print(n+" would like to climb "+r.upper())
	
