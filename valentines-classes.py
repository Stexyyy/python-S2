import pygame #gaming module (aka library) 
pygame.init() #initializes Pygame
pygame.display.set_caption("Valentine's day card") #sets the window title
screen = pygame.display.set_mode((800, 800)) #creates game screen
font = pygame.font.Font('freesansbold.ttf', 32) #load font
img = pygame.image.load("dog.jpg") #make sure this is saved to the same folder as your code

#------------------------------------------------
class heart:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
    def draw(self):
        pygame.draw.circle(screen, (250,0,0), (self.xpos, self.ypos), 20) #top left circle
        pygame.draw.circle(screen, (250,0,0), (self.xpos + 40, self.ypos), 20) #top right circle
        pygame.draw.polygon(screen, (250,0,0), ((self.xpos - 20, self.ypos+5),(self.xpos+59, self.ypos+5), (self.xpos+20, self.ypos+50))) #triangle to form base
    def move(self):
        if self.ypos >= 800:
            self.ypos = 0
        self.ypos+=1

#------------------------------------------------
ballin= heart(200, 200)
ballin2 = heart(400, 400)
h3 = heart(100, 100)
h4 = heart(300, 300)
h5 = heart(500, 500)
h6 = heart(600, 600)
h7 = heart(700, 700)
h8 = heart(800, 800)
h9 = heart(0, 0)



#image
while (True):
    screen.fill((0, 0, 0))
    
    text1 = font.render('I hope you guys break up', True, (250, 100, 100)) #numbers give color
    text3 = font.render('Have a horrible day', True, (250, 100, 100))
    text2 = font.render('Happy Valentines Day (nuh uh)', True, (250, 0, 0), (200,150,150)) #this one includes background color
    screen.blit(text1, (200, 100)) #numbers give position
    screen.blit(text2, (300, 300))
    screen.blit(text3, (150, 200))
    
    
    
    ballin.draw()
    ballin2.draw()
    h3.draw()
    h4.draw()
    h5.draw()
    h6.draw()
    h7.draw()
    h8.draw()
    h9.draw()
    
    
    ballin.move()
    ballin2.move()
    h3.move()
    h4.move()
    h5.move()
    h6.move()
    h7.move()
    h8.move()
    h9.move()


    screen.blit(img, (100, 400))#draw pic
    pygame.display.flip() #this flips all those shapes onto the game screen (needed for every game)


