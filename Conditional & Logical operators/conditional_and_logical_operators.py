age = int(input("Please enter your age: "))
monthly_income = int(input("What is your monthly income? "))
credit_score = int(input("What is your current credit score? "))
existing_debts = int(input("What is the total amount of your current existing debts? "))

debt_to_income_ratio = existing_debts / monthly_income

if age >= 18 and monthly_income >= 2000 and credit_score >= 650 and debt_to_income_ratio < 0.4 :
  print("Congratulations you are eligible for the loan.")
elif age < 18 and monthly_income >= 2000 and credit_score >= 650 and debt_to_income_ratio < 0.4:
  print("Sorry you do not meet the minimum age requirements for loan consideration.")
elif age >= 18 and monthly_income < 2000 and credit_score >= 650 and debt_to_income_ratio < 0.4:
  print("Sorry your monthly income is below the minimum required for loan consideration.")
elif age >= 18 and monthly_income >= 2000 and credit_score < 650 and debt_to_income_ratio < 0.4:
  print("Please improve your credit score in order to be considered for the loan.")
elif age < 18 and monthly_income < 2000 and credit_score < 650 and debt_to_income_ratio < 0.4:
  print("Sorry you do not meet any of the requirements for your loan application to be considered.")


