#creating empty dictionary
contacts = {}

#adding some contacts to the dictionary
contacts["Bob"] = 2783940189
contacts["Bill"] = 5634901682
contacts["Iancyril"] = 2673846710
contacts["Amadi"] = 7839401893

print(contacts.items())

#Removing contact for "Amadi"
contacts.pop("Amadi")
print(contacts.items())

#Updating Bill's contact in the dictionary
contacts.update({"Bill" : 6738490178})
print(contacts.get("Bill"))

#Searching for Bob's contact is in the dictionary and printing his phone number
bob = contacts.get("Bob")
print(bob)

#Displaying all contacts in the dictionary
for name,number in contacts.items():
  print(name, number)
