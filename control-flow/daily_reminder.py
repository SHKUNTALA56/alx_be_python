def daily_reminder():
    # Prompt the user to input the task description, level of priority, and if it is time-bound
    print("Welcome to your daily reminder")
    task = input("Enter your task: ")  # Exactly as required
    time_bound = input("Is it time-bound? (yes/no): ").lower()  # Exactly as required with correct spacing and format
    priority = input("Priority (high/medium/low): ").lower()  # Exactly as required

    # Match Case statement for priority
    match priority:
        case "high":
            if time_bound == "yes":
                print(f"Reminder: {task} is a high-priority task that requires immediate attention today!")
            else:
                print(f"Task: {task} is high priority but not time-bound.")
        case "medium":
            if time_bound == "yes":
                print(f"Reminder: {task} is a medium-priority task. Address it soon.")
            else:
                print(f"Task: {task} is medium priority and not time-bound.")
        case "low":
            if time_bound == "no":
                print(f"Note: {task} is a low-priority task. Consider completing it when you have free time.")
            else:
                print(f"Task: {task} is low priority but time-bound.")
        case _:
            print(f"Task: {task} doesn't match predefined conditions. Please review your inputs.")

# Call the function
daily_reminder()
