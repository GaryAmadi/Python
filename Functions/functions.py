#creating the function that prints out a phone number without any parameter

def my_contactinfo():
  print("My name is Gary")
  print("My phone number is 0756342890")

my_contactinfo()

#adding parameters to the function
def my_contact_info(name, phone_number):
  print("My name is " + name + ".")
  print("Here is my phone_number: " + phone_number)

my_contact_info("Gary", "0745367289") 
#Now the function only prints out the desired output when two arguments are passed to the parameters when calling the function.
