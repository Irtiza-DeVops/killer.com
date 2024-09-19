# Take input from the user
age = int(input("Enter your age: "))

if age > 99:
    print("You are older than 99!")
elif age > 90:
    print("You are older than 90!")
elif age > 80:
    print("You are older than 80!")
elif age > 70:
    print("You are older than 70!")
elif age > 60:
    print("You are older than 60!")
elif age > 50:
    print("You are older than 50!")
elif age > 40:
    print("You are older than 40!")
elif age > 30:
    print("You are older than 30!")
elif age > 20:
    print("You are older than 20!")
elif age > 10:
    print("You are older than 10!")
else:
    print("You are 10 years old or younger!")
    # Additional conditions for age 10
    if age == 10:
        if (age % 2) == 0:
            print("You are an even number!")
        else:
            print("You are an odd number!")
    elif age == 11:
        print("You are a teenager!")
    elif age == 12:
        print("You are a child!")
    else:
        print("You are a baby!")
        