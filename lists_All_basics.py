bicycles = ['trek', 'specialized','cannondale', 'redline']

print(bicycles[2].title())
print(bicycles[-1].title()) #[-1] prints out the last element in any list
print("\n")

bicycles[-1] = 'walk' #this modifies an element within a list
print(bicycles)
print("\n")

bicycles.append('suzuki')#this help adds a new element to the list
print(bicycles)
print("\n")

bicycles.insert(1, 'venza')#this help insertes to specific position within a list
print(bicycles)
print("\n")

del bicycles[0]
print(bicycles)#deleting by index from a list
print("\n")

popped_bicycle = bicycles.pop()
print(bicycles)
print(popped_bicycle)#pops the last item in a list and allows usage after
print("\n")
print("the last bicycle i bought was a ",popped_bicycle.title(),".")
print("\n")
del bicycles[0]
print(bicycles)
print("\n")

first_owned = bicycles.pop(0)
print("first bicycle i ever rode was ",first_owned.upper(),".")
print(bicycles)
message = "my first bicycle was "+ bicycles[0].upper()+ "."
print(message)
print("\n")



#appending to an empty list
motorcycles = []
print(motorcycles)
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

print("\n")



#exercises on list(3-1) random friends
print("\n exercise 3-1")
names = ['segun', 'kunle', 'Alex',"phillip"]
print("friend number one name is: ", names[0].upper())
print("friend number two name is: ", names[1].title())
print("friend number three  name is: ", names[2].title())
print("friend number four name is: ", names[-1].upper())
print("friend number four name is: ", names[3].upper())

print("#exercises on list(3-3")
vehicles = ['car','bicycle','aeroplane']
wish_1 = "i would love to own a venza "+ vehicles[0]+ " one day"
wish_2 = "i would love to own a cannondale "+ vehicles[1]+ " one day"
wish_3 = "i would love to own a Boeing "+ vehicles[-1]+ " one day"
print("\n", wish_1,"\n",wish_2,"\n",wish_3)
print("\n")

motorcycles.remove('honda')
print(motorcycles)

too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\n A",too_expensive.title(), "is too cheap for me")
print("\n")

#exrecise 3-4 guest list

guest_list = ['williams', "'Ojo's","Wilsons","Mcmillans"]
guest_message1 = "we welcome the  "+ guest_list[0].upper()+"  to today's event "
guest_message2 = "we welcome the "+ guest_list[1].upper()+" to today's event "
guest_message3 = "we welcome the "+ guest_list[2].upper()+" to today's event "
guest_message4 = "we welcome the "+ guest_list[-1].upper()+" to today's event "
print("\n LIST OF GUESTS")
print("\n\t ",guest_message1)
print("\n\t ",guest_message2)
print("\n\t ",guest_message3)
print("\n\t ",guest_message4)
print("the number guests available is:")
print("\t\t\t",len(guest_list))

#exercise 3-5 edited guest list
print("\n  We are sorry to announce the following guest won't be availabe for todays event") 
print("\n\t", "The",guest_list[2].upper())

print("\n The updated set of guests:")
del guest_list[2]
Edited_guest_list = guest_list
print(Edited_guest_list)
print("the number of guests available is:")
print("\t\t\t",len(Edited_guest_list))

print("\n")
Edited_guest_list.insert(2, "oyewole's") 
print(Edited_guest_list)
print("the number guests  now available is:")
print("\t\t\t",len(Edited_guest_list))
print("\n")
print("\n\t we welcome: ")
guest_message1 = "we welcome the  "+ Edited_guest_list[0].upper()+"  to today's event "
guest_message2 = "we welcome the "+ Edited_guest_list[1].upper()+" to today's event "
guest_message3 = "we welcome the "+Edited_guest_list[2].upper()+" to today's event "
guest_message4 = "we welcome the "+ Edited_guest_list[-1].upper()+" to today's event "

print("\n\t",guest_message1)
print("\n\t",guest_message2)
print("\n\t",guest_message3)
print("\n\t",guest_message4)

#exercise3-6 more guest list  for a bigger dinner table
print("\n\t\t","A bigger Dinner Table Is Available: ")
final_guest_list = Edited_guest_list 
Edited_guest_list.insert(0, "michael's")#added to beginning of the list
Edited_guest_list.insert(2,"leon's")#addded to the middle of the list
Edited_guest_list.append("olushola's")#added to the end of the list
print("\n",final_guest_list)
print("the number final_ guests available is:")
print("\t\t\t",len(final_guest_list))
guest_message1 = "we welcome the  "+ final_guest_list[0].upper()+"  to today's event "
guest_message2 = "we welcome the "+ final_guest_list[1].upper()+" to today's event "
guest_message3 = "we welcome the "+final_guest_list[2].upper()+" to today's event "
guest_message4 = "we welcome the "+final_guest_list[3].upper()+" to today's event "
guest_message5 = "we welcome the "+final_guest_list[4].upper()+" to today's event "
guest_message6 = "we welcome the "+final_guest_list[5].upper()+" to today's event "
guest_message7 = "we welcome the "+final_guest_list[-1].upper()+" to today's event "
print("\n",guest_message1,"\n",guest_message2,"\n",guest_message3,"\n",guest_message4,"\n",guest_message5,"\n",guest_message6,"\n",guest_message7)
print("\n")
print("\n")
print("\n","We are sorry we have just two seats for the guests")
print(final_guest_list)
print("\n")

#exercise 3-7 shrinking the guest list
canceled_guest1 = final_guest_list.pop()
print("\n\t",canceled_guest1,"please accept our apology")
print(final_guest_list)
print("the number guests presently is:")
print("\t\t\t",len(final_guest_list))
print("\n")

canceled_guest2 = final_guest_list.pop()
print("\n\t",canceled_guest2,"please accept our apology")
print(final_guest_list)
print("the number guests available is:")
print("\t\t\t",len(final_guest_list))
print("\n")

canceled_guest3 = final_guest_list.pop()
print("\n\t",canceled_guest3,"please accept our apology")
print(final_guest_list)
print("the number guests available is:")
print("\t\t\t",len(final_guest_list))
print("\n")

canceled_guest4= final_guest_list.pop()
print("\n\t",canceled_guest4,"please accept our apology")
print(final_guest_list)
print("the number guests available is:")
print("\t\t\t",len(final_guest_list))
print("\n")

canceled_guest5 = final_guest_list.pop()
print("\n\t",canceled_guest5,"please accept our apology")
print(final_guest_list)
print("the number guests available is:")
print("\t\t\t",len(final_guest_list))
print("\n")

print("\n", "we have only two guests left:")
print("\n", "The",final_guest_list[0].upper(),"you are still invited")
print("\n")

print("\n", "The",final_guest_list[1].upper(),"you are still invited")
print("the number guests available is:")
print("\t\t\t",len(final_guest_list))
print("\n")

del final_guest_list[:] #deletes the whole content tof the list
print("content of list is now empty:" )
print(final_guest_list)
print("the number guests available is:")
print("\t\t\t",len(final_guest_list))

















