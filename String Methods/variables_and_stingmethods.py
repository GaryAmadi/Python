#Introduction
print("Hello there User!")
full_name = input("Please enter your full name: ")
age = input("How old are you? ")
address = input("What is your current address? ")
phone_number = input("What is your phone number?(Please don't start with the country code) ")

#string methods on name
print(full_name.capitalize())
print(full_name.lower())
print(full_name.lower())

#formatting phone number
formatted_phone_number = f"({phone_number[:3]}){phone_number[3:6]}-{phone_number[6:]}"
print(formatted_phone_number)

#Displaying organized information
print("Here is a summary of your information: ")
print(f"Name: {full_name}")
print(f"Age: {age}")
print(f"Address: {address}")
print(f"Phone_number: {formatted_phone_number}")

#Calculating the DOB
dob = 2024 - int(age)
print(f"Your date of birth is {dob}")
