age = int(input("Enter your age: "))
gender = input("Enter your gender (male or female): ")

if age > 20:
    if gender == "male":
        print("adult male")
    else:
        print("adult female")

elif age <= 16:
    if gender == "male":
        print("young male")
    else:
        print("young female")
