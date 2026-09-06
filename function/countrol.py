#countrol with while loop

Number =[1, 2, 3, 4, 5, 6, 7, 8, 9,10, 11, 12,13,14,15,16,17,18]
i = 0
while i < len(Number):
    num = Number[i]
    if num == 3:
        print("This is number 3")
        break
    elif num == 5:
        print("This is number 5")
    print(num)
    i += 1