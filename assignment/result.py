
age = int(input("Enter your age: "))
qualification = input("Enter your qualification: ")
gpa = float(input("Enter your GPA: "))

if age < 18:
    print("You must be at least 18 years old.")
elif qualification== "matric":
    if gpa < 0 or gpa > 4:
        print("GPA should be between 0 and 4.")
    else:
        print("All inputs are valid.")
elif qualification == "intermediate":
    if gpa < 0 or gpa > 4:
        print("GPA should be between 0 and 4.")
    else:
        print("All inputs are valid.")
elif qualification == "bachelor":
    if gpa < 0 or gpa > 4:
        print("GPA should be between 0 and 4.")
    else:
        print("All inputs are valid.")
elif qualification == "master":
    if gpa < 0 or gpa > 4:
        print("GPA should be between 0 and 4.")
    else:
        print("All inputs are valid.")
else:
    print("Qualification is not valid. Please enter a valid qualification.")