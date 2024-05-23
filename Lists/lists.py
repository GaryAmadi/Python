shopping_list = []

while True:
    import time
    print("Hello there, what would you like to do with yor shopping list today")
    print("1.Add item")
    print("2.Remove item")
    print("3.View list")
    print("4.Exit")

    user_input = int(input("Please select one of the options above: "))

    if user_input == 1:
        print(f"Here is your current shopping list:\n{shopping_list}")
        add_item = input("Please enter the item you would like to add to your shopping list: ").capitalize()
        shopping_list.append(add_item)
        print(f"Here is your updated shopping list:\n{shopping_list}")
        time.sleep(2)

    elif user_input == 2:
      print(f"Here is your shopping list:\n{shopping_list}")
      remove_item = input("Please enter the item you would like to remove from your shopping list: ").capitalize()
      if remove_item in shopping_list:
        shopping_list.remove(remove_item)
        print(f"Here is your updated shopping list:\n{shopping_list}")
      else:
        print(f"{remove_item} is not in the list.")
      time.sleep(2)

    elif user_input == 3:
        if len(shopping_list) != 0:
            print(f"Here is your shopping list:\n{shopping_list}")
        else:
            print("Your shopping list has no items.")
        time.sleep(2)

    elif user_input == 4:
        print("Thank you for using our shopping list software today\nHave a nice one!")
        break
    else:
        print("Invalid input.Please try again.")
        time.sleep(2)

