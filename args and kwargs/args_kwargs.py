#args - parameter that packs all arguments into a tuple
def sum(num1, num2):
  summed = num1 + num2
  return summed
print(sum(1, 1))

def add(*args):
  sum = 0
  for x in args:
    sum += x
  return sum

print(add(1, 2, 3, 4, 5, 6))


#**kwargs - parameter that will pack all arguments into a dictionary
def hello(**kwargs):
  print("Hello " + kwargs["first"] + " " + kwargs["last"])
  
hello(first="Thomas", middle="Yeye", last="Partey")

def hello(**kwargs):
  print("Hello", end=" ")
  for key,value in kwargs.items():
    print(value, end=" ")
    

hello(first="Thomas", middle="Yeye", last="Partey") #keyword argumemts are used

#The most important thing is using the * for args and ** for kwargs name used doesn't matter
#e.g ** names can be used to name kwargs for various names
