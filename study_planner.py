print("Welcome to Study Planner")

subjects = []

number_of_subjects = int(input("How many subjects do you want to study today? "))

for i in range(number_of_subjects):
    subject = input(f"Enter subject {i + 1}: ")
    minutes = int(input(f"How many minutes for {subject}? "))

    subjects.append({
        "subject": subject,
        "minutes": minutes
    })

print()
print("Today's study plan:")

total_minutes = 0
total_breaks = 0

for item in subjects:
    minutes = item["minutes"]

    breaks = minutes // 50

    print(
        "-",
        item["subject"],
        ":",
        minutes,
        "minutes | Recommended breaks:",
        breaks
    )

    total_minutes += minutes
    total_breaks += breaks

print()
print("Total study time:", total_minutes, "minutes")
print("Total recommended breaks:", total_breaks)
