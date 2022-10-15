                   # Question no :- 5
N = int(input("Enter number "))
even = 0
i = 1
while i<=2*N:
    if i % 2 == 0:
        even = even+i 
    i += 1
print(even)
print()