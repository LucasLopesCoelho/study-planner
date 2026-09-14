from datetime import datetime, timedelta
print("Welcome to Study Planner")

subjects = []
start_time_input = input("What time will you start studying? (HH:MM): ")
start_time = datetime.strptime(start_time_input, "%H:%M")
number_of_subjects = int(input("How many subjects do you want to study today? "))
priority = int(input(f"Priority for {subject} (1 = low, 2 = medium, 3 = high): "))
for i in range(number_of_subjects):
    subject = input(f"Enter subject {i + 1}: ")
    minutes = int(input(f"How many minutes for {subject}? "))

    subjects.append({
    "subject": subject,
    "minutes": minutes,
    "priority": priority
})
    })

subjects.sort(key=lambda item: item["priority"], reverse=True)print()
print("Today's study plan:")

total_minutes = 0
total_breaks = 0

for item in subjects:
    minutes = item["minutes"]
priority = item["priority"]

if priority == 3:
    priority_name = "High"
elif priority == 2:
    priority_name = "Medium"
else:
    priority_name = "Low"
    breaks = minutes // 50

    print(
    "-",
    item["subject"],
    ":",
    minutes,
    "minutes | Priority:",
    priority_name,
    "| Recommended breaks:",
    breaks
)
        

    total_minutes += minutes
    total_breaks += breaks

print()
print("Total study time:", total_minutes, "minutes")
print("Total recommended breaks:", total_breaks)total_break_time = total_breaks * break_duration
total_session_time = total_minutes + total_break_time
end_time = start_time + timedelta(minutes=total_session_time)

print("Start time:", start_time.strftime("%H:%M"))
print("Estimated finish time:", end_time.strftime("%H:%M"))
print("Total break time:", total_break_time, "minutes")
print("Total session time:", total_session_time, "minutes")
break_duration = 10
