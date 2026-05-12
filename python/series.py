# write a program to print the summation of the following series upto n terems : 1-2+3+4+5+6...next
list[]
 even sum
 odd sum = 0
 odd
 n = int(input("enter numberr"))
 for i in range(1,n+1):
    m = int(input("enter your number"))
    list.oppend(m)
print(list)
for i in list:
    if i%2==0:
        evensum +=i
    else:
        odd sum += i

print("sum of even number",even sum)
print("sum of odd number",odd sum)
             