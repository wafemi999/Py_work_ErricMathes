from random import randint
class Die():
	'''Modeling a dice '''
	
	def __init__(self):
		'''initiating attribuites'''
		self.sides = 20
		
	def rollDie(self):
		'''simulates rolling a die'''
		
		print("ROLLINIG........")
		print("RESULT: ",randint(1, self.sides+1))
		
		
print("this is a die with 20sides")
prompt = int(input(" HOW many times do you want to roll: "))
p =list(range(1,prompt+1))
for i in p:
	print("\n ROUND",i)	
	x = Die()	
	x.rollDie()
	

