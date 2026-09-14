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

for item in subjects:
    print("-", item["subject"], ":", item["minutes"], "minutes")
    total_minutes += item["minutes"]

print()
print("Total study time:", total_minutes, "minutes")
