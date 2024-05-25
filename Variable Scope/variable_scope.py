#A variable is only recognized inside the region it is created

def print_name():
  name = "GARY" #local scope
  print(name)

print_name()

#Global scope
name = "Gary Amadi" #variable is declared outside the function
def my_name():
  print(name)
  
my_name()

#Order of priotity used in python
#L-Local
#E-Enclosed
#G-Global
#B-Built in variables
