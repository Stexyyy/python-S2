import pygame as py
import random

py.init()
py.display.set_caption("game of life!")
screen = py.display.set_mode((800, 800))
clock = py.time.Clock()

map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0],
       [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

map = [[random.randrange(0,2)]*16 for i in range(16)]
print(map)

#game loop #############################################
while True:
    clock.tick(60)
    event = py.event.get()
    
    #input section ---------------------------
    for event in py.event.get():
        break
    #update section---------------------------
    
    for i in range(16):
        for j in range(16):
            counter = 0
            if i <15 and map [i+1][j] == 1:#check above
                counter+=1
            if j <15 and map [i][j+1] == 1: #check right
                counter+=1
            if i <15 and j<15 and map [i+1][j+1] == 1:#check top corner
                counter+=1
            if i <15 and j>=0 and map [i+1][j-1] == 1:#check top left corner
                counter+=1
            if i <15 and map [i-1][j] == 0:#check below
                counter+=1
            if j <15 and map [i][j-1] == 1: #check left
                counter+=1
            if i <15 and j<15 and map [i+1][j+1] == 1:#check bottom corner
                counter+=1
            if i <15 and j>=0 and map [i+1][j-1] == 1:#check bottom left corner
                counter+=1
                
                
            #kill,live, or grow cells
            if map[i][j]==1 and counter <=1:
                map[i][j]=0
                print("I died from lonliness")
            if map[i][j]==1 and counter ==3 or counter ==2:
                map[i][j] =1
                print("cell lives")
            if map[i][j]==1 and counter >=4:
                map[i][j]=0
                print("cell dies, too crowded")
            if map[i][j]==1 and counter ==3:
                map[i][j] =1
                print("cell lives, reproductions")
            
    
    py.time.wait(200)
    
    #render section--------------------------------------
    screen.fill((0, 0, 0))
    
    for i in range (16):
        for j in range (16):
            if map[i][j]==0:
                py.draw.rect(screen, (0,0,0),(j*50, i*50, 50, 50))
                py.draw.rect(screen, (255,255,255),(j*50, i*50, 50, 50), 1)
            if map[i][j]==1:
                py.draw.rect(screen, (0,200,200),(j*50, i*50, 50, 50))
                
    
    #stuff gets drawn here
    
    py.display.flip()
    
#end game loop ###################################################
    
py.quit()
