N = int(input("Enter N: "))
s = 0
for digit in str(N):
    s += int(digit)
print("Sum of digits:", s)