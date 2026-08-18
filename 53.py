x = int(input("Enter second: "))
y = int(input("Enter minutes: "))
z = int(input("Enter hours: "))
if 0 <= x < 60 and 0 <= y < 59 and 0 <= z < 23:
    print(x, y, z)
else:
    print(False)
