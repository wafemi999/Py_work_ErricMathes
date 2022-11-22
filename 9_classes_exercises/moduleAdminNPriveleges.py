from moduleUser import User

class Admin(User):
	'''this inherits from parent class USER'''
	def __init__(self, f_name, l_name, age, location):
		'''this initialises attributes to admin from USER'''
		
		super().__init__( f_name, l_name, age, location)
		self.priveleges = []
		
		
	def showPriveleges(self):
		'''priveleges for ADMIN users'''
		self.priveleges = ['can add post', 'can delete post', 'can ban user']
		for i in self.priveleges:
			print(i)

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
