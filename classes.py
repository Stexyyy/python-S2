import random
import pygame as py
screen = py.display.set_mode((1000, 800))  # creates game screen
screen.fill((0,0,0))

class chicken:
    def __init__(self, name):
        self.hunger = 0
        self.name = name
        
    def update(self):
        self.hunger += 5
        if self.hunger <= 30:
            ballin = random.randrange(1, 2)
            if ballin == 1:
                print("bok BOK! says", self.name)
                return 1
            else:
                return 0
    def feed(self):
        self.hunger -= 5
        print(self.name, "went peck peck!")
        
    def pet(self):
        print(self. name, "does some happy chicken noises :) ")
        
    def printinfo(self):
        print("my name is: ", self.name)
        
    def draw(self):
        py.draw.rect(screen, (250, 250, 250), (200, 200, 40, 40))

bob = chicken("bob")
bob.update()

sally = chicken("sally")
sally.feed()

marty = chicken("marty")
marty.pet()

while True:       



    
    screen.fill((0,0,0)) #wipe screen so it doesn't smear
    
    bob.draw()
    py.display.flip()#this actually puts the pixel on the screen
py.quit()
