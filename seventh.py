N = int(input("Enter number "))   # Question no :- 7
b = str(N)
count = 0
for a in b:
    if 0 <= int(a) < 100:
        count += 1
print("digits are",count)
print()

