import json
def GetStoredUserName():
	'''get stored username if available'''
	filename = 'username_1.json'
	try:
		with open(filename)as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return none
	else:
		return username
		
def GreetUser():
	'''greet the user by name from username returned from above'''
	username = GetStoredUserName()
	if username:
		print('welcome back', username) 	
	else:
		username = input("whats your name? ")
		filename = 'username.json'
		with open(filename, 'w')as f_obj:
			json.dump(username, f_obj )
			print("we will remember you when you come back. ")
			
	
