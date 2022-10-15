n = int(input("Enter number in decimal = "))       # Question no :-9
a,i,count=n,n,0
while i >= 0:
    if count == 0:
        print(n,"in binary are written below")
        print("0 b",end = " ")
        count += 1
    if n  == 0:
        print("0")
    if 2**i <= n:
        if 2**i <= a:
            a = a-2**i
            print("1",end = " ")
        else:
            print("0",end = " ")
    i -= 1
print()
print()