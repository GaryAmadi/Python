while True:
  import time
  
  user_input = input("Please enter a positive number to count up to(enter 'stop' to terminate programme): ")
  
  if user_input.lower()  == "stop":
    break
  
  elif user_input.isdigit():
    maximum_number = int(user_input)
    
    if maximum_number > 0:
      for number in range(1, maximum_number+1):
        if number % 2 == 0:
          continue #skips even numbers 
        else:
          print(number)
          time.sleep(1) #sleep for one second after printing a number
          
    print("Thank you for playing the game today!")
    break
        
  else:
      continue
  