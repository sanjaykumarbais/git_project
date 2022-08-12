n = int(input("Please enter an integer: "))
a = 0
for i in range(1, n+1):
    if i<=n:
        a = a + i
print("The sum of entered integer is: " + str(a))
