num = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
if (num % 2 == 0 and num2 % 2 != 0) or (num % 2 != 0 and num2 % 2 == 0):
    result = num * num2
    print(result)
else:
    print("End")
