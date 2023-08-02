num_of_eating = int(input("How many times a week do you eat at the student cafeteria? "))
price = float(input("The price of a typical student lunch? "))
weekly_spending = float(input("How much money do you spend on groceries in a week? "))
weekly = num_of_eating * price + weekly_spending
daily = weekly / 7
print("Average food expenditure:")
print(f"Daily: {daily} euros")
print(f"Weekly: {weekly} euros")