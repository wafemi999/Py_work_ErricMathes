import json
username = input("whats your name? ")
with open("username.json", 'w')as f_obj:
	json.dump(username, f_obj)
	print("we will you when youn come back", username.title())
