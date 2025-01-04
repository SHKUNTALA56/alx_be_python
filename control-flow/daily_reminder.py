# Prompt the user for task details
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Validate inputs
if priority not in ["high", "medium", "low"]:
    print("Invalid priority level. Please enter high, medium, or low.")
    exit()
if time_bound not in ["yes", "no"]:
    print("Invalid input for time sensitivity. Please enter yes or no.")
    exit()

# Generate a customized reminder using Match Case and conditional logic
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"

# Add time sensitivity information
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Print the customized reminder
print("\nReminder:")
print(reminder)

