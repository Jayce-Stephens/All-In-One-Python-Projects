
def main():
    print("Welcome to the Daily Habit Tracker!")
    habit = input("Enter the habit you want to track: ")
    hours = float(input(f"Enter the number of hours you spent on {habit} today: "))
    
    print("Great! Let's try and decrease the time spent on this habit by '10%' each day.")
    if hours >= 1:
        reduced_hours = hours - (hours * 0.10)
        print(f"To reduce your time spent on {habit}, aim for {reduced_hours:.2f} hours tomorrow.")
    else:
        print(f"Your time spent on {habit} is already low.")




if __name__ == "__main__":
    main()