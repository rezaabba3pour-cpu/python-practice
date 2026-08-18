num = input("Enter a 4-digit number: ")
while num != "6174":
    big = int("".join(sorted(num, reverse=True)))
    small = int("".join(sorted(num)))

    result = big - small

    print(big, "-", small, "=", result)

    num = str(result).zfill(4)

print("Reached 6174!")
