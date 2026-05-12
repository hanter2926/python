# whitw a program to find whether a number is a prme number

num = int(input("Enter your number: "))
prime = 1

for x in range(2, num):
    if num % x == 0:
        prime = 0
        break

if prime == 1 and num > 1:
    print("Prime number")
else:
    print("Not prime number")