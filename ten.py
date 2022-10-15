n = int(input("Enter number "))             #Question no :- 10
s = ""
if n == 0:
    print("0")
else:
    while n:
        r = n % 8
        s = s + str(r)
        n = n // 8
    a = s[::-1]
    print(int(a))