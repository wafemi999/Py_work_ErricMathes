import json
def GetStoredUserName():
	'''get stored username if available'''
	filename = 'username.json'
	try:
		with open(filename)as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return none
	else:
		return username
		
def GetNewUsername():
	'''prompts for a new username'''
	username = input("whats your name? ")
	filename = 'username.json'
	with open(filename, 'w')as f_obj:
		json.dump(username, f_obj )
	return username
		
def GreetUser():
	'''greet the user by name from username returned from above'''
	username = GetStoredUserName()
	print("are you", username)
	ans = input("enter 'y' for YES or 'n' for NO: ")
	if ans == 'y':
		print('welcome back', username) 	
	else:
		username = GetNewUsername()
		print("we will remember you when you come back. ")



GreetUser()
