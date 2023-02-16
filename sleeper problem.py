def alarm(h, m):
    if h > 23 and m > 59:
        print("NOOOOOOO!!!!")
    if m < 40:
        h -= 1
        m += 60
        m -= 40
    elif m > 40:
        m -= 40
    if h < 0:
        h = 23

    print(h, m)

h= int(input("What hour do you need to get out of bed? "))
m = int(input("Minute to get out of bed? "))
    
alarm(h, m)
