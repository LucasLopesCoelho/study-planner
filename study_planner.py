print("Welcome to Study Planner")

subject = input("What subject do you want to study today? ")
minutes = int(input("How many minutes do you want to study? "))

if minutes <= 30:
    breaks = 0
elif minutes <= 60:
    breaks = 1
else:
    breaks = 2

print()
print("Today's study plan:")
print("Subject:", subject)
print("Study time:", minutes, "minutes")
print("Recommended breaks:", breaks)
