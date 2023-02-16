def ballin(m, d):
    if m == 5: #may
        return 12 - d
    if m == 4: #april
        return 30 - d + 12
    if m == 3:
        return 31 - d + 12 + 30
    if m == 2:
        return 28 - d + 12 + 30 + 31
#---------------------------------------
print("lets see how many days seniors have left!")
a = int(input("enter todays month as a number: "))
b = int(input("enter todays day: "))
print(ballin(a, b))
        
