#5_3alien colors
alien_color = 'green'
alien_color2 = 'yellow'
alien_color3 = 'red'



#5_3 ALIEN COLORS pass
if alien_color =='green':
	print("you just earned 5 points")
	
#5_3 ALIEN COLORS fail
if alien_color !='greek':
	print("\n")



#5-4 alien colors pass
if alien_color =='green':
	print("you just earned 5 points")
else:
	print("you just earned 10 points")

#5-4 alien colors fail
if alien_color != 'green':
	print("you just earned 5 points")
else:
	print("you just earned 10 points")


print("\n")
#5_5 alien colors #3
if alien_color == 'green':
	print("player earned 5 points")
elif alien_color != 'green':
	print("0 point earned")
else:
	print("\n")
	
print("\n")	
if alien_color2 == "yellow":
	print("player earned 10 points")
elif alien_color2 != 'yellow':
	print("0 points earned")
else:
	print("\n")
	
print("\n")

if alien_color3 == "red":
	print("player earned 15 points")
elif alien_color3 != "red":
	print("0 points earned")
else:
	print("\n")
	
print("\n")


#5-6 stages of life

age = 35
if age < 2:
	print("you are still a baby")
elif age <4:
	print("you are still a toddler")
elif age < 13:
	print("you are still a kid")
elif age < 20:
	print("you are still a teenager")
elif age < 65 :
	print("you are still an adult")
else:
	print("you are an elder")

print("\n")
#5-7 favourite_fruits
favourite_fruits = ['water melon','cucumber','garden egg']
if 'bananas' in favourite_fruits:
	print("you really like babanas")
if 'water melon' in favourite_fruits:
	print("you really like water melon")
if 'cucumber' in favourite_fruits:
	print("you really like cucumber")
if 'apple' in favourite_fruits:
	print("you really like apple")
if 'garden egg' in favourite_fruits:
	print("you really like garden egg")
