print("passing a list in function:")
#greet_users.py
def greet_users(names):
	'''using list in function'''
	for name in names:
		msg = "hello " + name + "!"
		print(msg)
		
usernames =['magaret', 'ty', 'hannah']
greet_users(usernames)  


print("modifying a list in function:")
#printing models
uncompleted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

while uncompleted_designs:
	current_designs = uncompleted_designs.pop()
	print("\n printing model: ", current_designs.title())
	completed_models.append(current_designs)
	
	#display all model:
print("\n----comoleted models (all):")
print(sorted(completed_models))
	



print("\n modifying printing models using functions a list in function:")
#printing models with functions:

#function 1 simulates printing of the models:
def print_models(ucompleted_designs, completed_models):
	'''simulates the processing of uncompleted designs'''
	while uncompleted_designs:
		current_designs = uncompleted_designs.pop()
		
		print("\n----processing-----")
		print(current_designs+ "")
		completed_models.append(current_designs)

def show_completed_models(completed_models):
	'''show all completed models:'''
	print("-----printing completed models:------")
	for complete in completed_models:
		print(complete)
		
#using the functions:
uncompleted_designs = ['galloo', 'iphone case', 'jet chair']
completed_models = []

print_models(uncompleted_designs[:], completed_models)
show_completed_models(completed_models)		
