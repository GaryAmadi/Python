#importing the math module
import math

temperatures = [10.6, 10.5, 45.8, 89.5, 67.3, 54.2, 8.1, 10, 90.9, 33.3]
print(temperatures)

#calculating the average temperature
average_temperature = sum(temperatures)/len(temperatures)
#rounded average
rounded_up_average = math.ceil(average_temperature)
rounded_down_average = math.floor(average_temperature)

#Printing out summary of the temperature data
print(f"The maximum temperature was {max(temperatures)}")
print(f"The minimum temperature was {min(temperatures)}")
print(f"The average temperature was {average_temperature}")
print(f"The rounded up average is {rounded_up_average}")
print(f"The rounded down average is {rounded_down_average}")