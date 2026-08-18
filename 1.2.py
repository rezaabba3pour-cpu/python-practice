average = float(input("Enter your average: "))
num = int(input("Enter how many courses passed: "))
num1 = input("Did you pass the prerequisite? ")
num2 = input("Are you conditional? ")

if average >= 12 and num >= 60 and num1 == "yes" and num2 == "no":
    print("You can continue")
else:
    print("Fail")
