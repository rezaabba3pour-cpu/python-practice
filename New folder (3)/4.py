positive = 0
negative_sum = 0
for i in range(100):
    num = float(input("Enter a number: "))
    if num > 0:
        positive += 1
    elif num < 0:
        negative_sum += num

print("Positive numbers:", positive)
print("Sum of negative numbers:", negative_sum)

