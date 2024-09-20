age = int(input("Enter your age: "))
if age < 18:
    print("🚫 You must be at least 18 years old to proceed. Access denied!")
    exit()

print('''*****************************************************
                 🎓 Please select your qualification: 🎓
*****************************************************''')

qualification_list = [
    '1: Matric',
    '2: Intermediate',
    '3: Bachelor',
    '4: Master',
]

for values in qualification_list:
    print(values)

qualification = input("Enter your qualification : ")
gpa = float(input("Enter your GPA (0.0 - 4.0): "))

if qualification == '1' or qualification == "Matric":
    if gpa < 0 or gpa > 4:
        print("⚠️ GPA should be between 0 and 4. Please enter a valid GPA.")
    else:
        print("🎉 All inputs are valid. You're on the right path!")
        exit()

elif qualification == '2' or qualification == "Intermediate":
    if gpa < 0 or gpa > 4:
        print("⚠️ GPA should be between 0 and 4. Please enter a valid GPA.")
    else:
        print("🎉 All inputs are valid. Keep up the great work!")
        exit()

elif qualification == '3' or qualification == "Bachelor":
    if gpa < 0 or gpa > 4:
        print("⚠️ GPA should be between 0 and 4. Please enter a valid GPA.")
    else:
        print("🎉 All inputs are valid. You're doing awesome!")
        exit()

elif qualification == '4' or qualification == "Master":
    if gpa < 0 or gpa > 4:
        print("⚠️ GPA should be between 0 and 4. Please enter a valid GPA.")
    else:
        print("🎉 All inputs are valid. You're at the top of your game!")
        exit()

else:
    print("❌ Invalid qualification. Please enter a valid option from the list.")
