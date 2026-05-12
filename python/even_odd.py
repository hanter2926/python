# write a program having a parameterised function that returns true or false depending on wheter the parameter passed is even or odd
def add_even(n):
    if n%2==0:
        return True
    else:
        return False

n = int(input("enter any number"))
result = addeven(n)
print(result)