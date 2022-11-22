#simple dictionary
alien_0 = {'color':'green', 'points':5}
print(alien_0['color'],"\n")
print(alien_0['points'])

#accesing key-values
new_points = alien_0['points'] #accesing key-values
print("you just earned ",str(new_points)," points")
print(alien_0)


print("\n Adding new key-value pairs:")
alien_0['x_position']= 0
alien_0['y_position']= 25
print(alien_0)


print("\n starting with an empty dictionary:")
alien_1 = {}
alien_1['color']='green'
alien_1['points']= 5
print(alien_1)


print("\n modifying values in a dictionary:")
print("The alien is ", alien_0['color'])

alien_0['color'] = 'orange'

print("the alien is now ", alien_0['color'])


#modifying alien position

print(alien_0)
alien_0['y_position'] = 25
alien_0['speed'] = 'fast'
print(alien_0)
print("\n alien_0 original x_position = ", str(alien_0['x_position']))

#moving the alien to the right of the screen depending on the current speed
if alien_0['speed'] == 'slow':
	x_increment = 1
	
elif alien_0['speed'] == 'medium':
	x_increment = 2

#these must be a fast alien
else:
	x_increment = 3
	
#the new position is old position + x_increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("\n New X_position = ",str(alien_0['x_position']))

print("\n deleting a key:")
# deleting a key ina dictionary (permanent)
print("\n")
print(alien_0)
print("\n")
del alien_0['points']
print(alien_0)



#dictionary of similar obejecs and many info
print("\n Dictionary of similar objects:")

favorite_languages = {
	'jen':'python',
	'sarah':'C',
	'edward':'ruby',
	'phil':'python',
	}

print("sarah's favourite language is :", favorite_languages['sarah'].upper())
