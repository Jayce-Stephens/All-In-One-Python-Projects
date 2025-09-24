
def main():
    print("Welcome to the Personal Finance Tracker!")
    income = float(input("Enter your total monthly income: ")) #Take user input and convert to float
    expenses = float(input("Enter your total monthly expenses: "))

    savings = income - expenses
    if savings > 0:
        print(f"Great! You are saving ${savings:.2f} this month.")
    elif savings < 0:
        print(f"Warning! You are overspending by ${-savings:.2f} this month.")
    else:
        print("You are breaking even this month.")

