first_name = "Gary"
last_name = "Amadi"
print("Hello, i'm " + first_name + " " + last_name)

#producing same output using string formatting
#method1
print("Hello, i'm {} {}".format("Gary","Amadi"))

#using positional arguments (indexes)
print("Hello, i'm {0} {1}".format("Gary","Amadi")) #Hello i'm Gary Amadi
print("Hello, i'm {1} {0}".format("Gary","Amadi")) #Hello i'm Amadi Gar

#using keyword_arguments
print("Hello, i'm {first_name} {last_name}".format(first_name="Gary",last_name="Amadi"))

#method2
#using same string values initially declared for first_name & last_name
greet = "Hello, i'm {} {}" 
print(greet.format(first_name, last_name))

#method3
print(f"Hello, i'm {first_name} {last_name}") #add f before writing what's to be printed and in the {} refer to what should be prented in the space

#Adding padding(space) when using string formatting
name = "Gary"
print("Hello my name is {:10}.Nice to meet you.".format(name))
print("Hello my name is {:<10}.Nice to meet you.".format(name)) #left align use <
print("Hello my name is {:>10}.Nice to meet you.".format(name)) #right align use >
print("Hello my name is {:^10}.Nice to meet you.".format(name)) #center align use ^

#output
# Hello my name is Gary      .Nice to meet you.
# Hello my name is Gary      .Nice to meet you.
# Hello my name is       Gary.Nice to meet you.
# Hello my name is    Gary   .Nice to meet you.

#adding padding to numbers
number = 3.14285
print("The universally used pi value is {:.3f}".format(number)) #rounds up to 3.143

number = 1000
print("A thousand: {:,}".format(number)) #adds a comma at the thousands place value output:1,000
print(("A thousand: {:b}".format(number))) #representing as a binary 1111101000
print(("A thousand: {:o}".format(number))) #representing in octal format 1750
print(("A thousand: {:X}".format(number))) #representing in hexadecimal format 3E8
print(("A thousand: {:e}".format(number))) #representing using scientific notation 1.000000e+03