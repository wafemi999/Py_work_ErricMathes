class User():
	'''Modeling info of a user'''
	
	def __init__(self, f_name, l_name, age, location):
		'''initiating attribuites'''
		self.f_name = f_name
		self.l_name = l_name
		self.age = str(age)
		self.location = location
	
	def describe_user(self):
		'''summary info of the user'''
		print("NAME:",self.f_name.title(),"",self.l_name.upper(),".")
		print("AGE:",self.age,".")
		print("LOCATION:",self.location.title(),".")
		
		
	def greet_user(self):
		'''welcome message for the user'''
		print(" ", self.f_name.title(),", it's a honour having you here")
		
		
class Admin(User):
	'''this inherits from parent class USER'''
	def __init__(self, f_name, l_name, age, location):
		'''this initialises attributes to admin from USER'''
		
		super().__init__( f_name, l_name, age, location)
		self.privileges  = Privileges()
		
class Privileges():
	'''shows admin privileges'''
	
	def __init__(self):
		'''lists privileges'''
		self.privileges = []
		
	def showPriveleges(self):
		'''priveleges for ADMIN users'''
		self.priveleges = ['can add post', 'can delete post', 'can ban user']
		for i in self.priveleges:
			print(i)
