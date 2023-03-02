import random

mapgrid = [[0 for i in range(10)] for j in range (10)] #grid to hold a starting point

xpos = int(random.randint(0, 9))
ypos = int(random.randint(0, 9))

bruh = int(random.randint(1,5))#area around me

move = 0
    
mapgrid[xpos][ypos] = 1

balls = input("hi, press q if needing to quit otherwise press enter: ")
#game--------------------
while balls != 'q':

    if mapgrid[xpos][ypos] == 0:
        bruh = int(random.randint(1,5))
    bruh = int(random.randint(1,5))

    for row in mapgrid:
        print(row)
