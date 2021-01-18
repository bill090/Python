# import needed modules

import pygame, time, random

# initialize modules

pygame.mixer.pre_init()
pygame.init()

# define needed variables an other pygame stuff

gameDisplay = pygame.display.set_mode((1820, 980))
clock = pygame.time.Clock()
pygame.display.set_caption('Plane Fighting')

# define functions

def frameUpdate():
    pygame.display.update()
    clock.tick(60)

def text_objects(text, font):
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()

def displayMsg(msg, pos, fontSize):
    largeText = pygame.font.Font('freesansbold.ttf', fontSize)
    TextSurf, TextRect = text_objects(msg, largeText)
    TextRect.center = (pos[0], pos[1])
    gameDisplay.blit(TextSurf, TextRect)

def die():
    displayMsg("You died", (int(1820 / 2), int(980 / 2)), 115)
    frameUpdate()
    time.sleep(3)

def playMus(musPath):
    pygame.mixer.music.load(musPath)
    pygame.mixer.music.play()

def playBackMus(backMusPath):
    pygame.mixer.music.load(backMusPath)
    pygame.mixer.music.play(-1)

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def button(activeColor, inactiveColor, buttonX, buttonY, buttonWidth, buttonHeight, msg, fontSize):
    things(buttonX, buttonY, buttonWidth, buttonHeight, inactiveColor)
    if pygame.mouse.get_pos()[0] > buttonX and pygame.mouse.get_pos()[0] < buttonX + buttonWidth and pygame.mouse.get_pos()[1] > buttonY and pygame.mouse.get_pos()[1] < buttonY + buttonHeight:
        things(buttonX, buttonY, buttonWidth, buttonHeight, activeColor)
    displayMsg(msg, (buttonX + int(buttonWidth/2), buttonY + int(buttonHeight/2)), fontSize)

def gameQuit():
    pygame.quit()
    quit()

def plane(x, y, planeImage):
    gameDisplay.blit(planeImage, (x, y))

# define planes and projectiles

enemyPlanes = [pygame.image.load("Python with AI - Level 2/pygame/planeGame/L1.png"), pygame.image.load("Python with AI - Level 2/pygame/planeGame/L2.png"), pygame.image.load("Python with AI - Level 2/pygame/planeGame/L3.png"), pygame.image.load("Python with AI - Level 2/pygame/planeGame/L4.png")]
missile = pygame.image.load("Python with AI - Level 2/pygame/planeGame/misslle.png")
bomb = pygame.image.load("Python with AI - Level 2/pygame/planeGame/B1.png")
player = pygame.image.load("Python with AI - Level 2/pygame/planeGame/RFA Fighter.png")

# define enemy class

class Enemy:
    def __init__(self, x, y, imageNum, shot, respawnWait, x_change, y_change):
        self.x = x
        self.y = y
        self.shot = shot
        self.imageNum = imageNum
        self.respawnWait = respawnWait
        self.x_change = x_change
        self.y_change = y_change
    def move(self):
        self.x += self.x_change
        self.y += self.y_change
        return (x, y)

while True:

    # reset variables

    volume = 100
    menuEnd = False
    dead = False
    x_change = 0
    x = 740
    y_change = 0
    y = 720

    # menu code

    while not menuEnd:
        displayMsg("Plane Fighting", (int(1920 / 2), int(980 / 2)), 115)
        displayMsg("press space to start and q to quit. or the buttons", (int(1920/2), int(980/2) + 100), 20)
        button((255, 40, 0), (255, 0, 0), 1120, 780, 100, 100, "Quit?", 20)
        button((0, 255, 0), (90, 238, 90), 600, 780, 100, 100, "START?", 20)
        button((255, 255, 255), (100, 100, 100), 390, 780, 200, 100, "Change Volume?", 20)
        button((255, 255, 255), (255, 255, 255), 200, 100, 1, 1, f"Volume: {str(volume)}%", 20)
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] > 600 and event.pos[0] < 700 and event.pos[1] > 780 and event.pos[1] < 980 and event.button == 1):
                menuEnd = True
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_q) or (event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] > 1120 and event.pos[0] < 1220 and event.pos[1] > 780 and event.pos[1] < 880 and event.button == 1) or event.type == pygame.QUIT:
                gameQuit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] > 390 and event.pos[0] < 590 and event.pos[1] > 780 and event.pos[1] < 880 and event.button == 1:
                if volume == 100:
                    volume = 0
                else:
                    volume += 10
        frameUpdate()
        gameDisplay.fill((255, 255, 255, 0))
    pygame.mixer.music.set_volume(volume / 100)

    while not dead:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameQuit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x_change = -5
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x_change = 5
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    y_change = -5
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    y_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x_change = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s or event.key == pygame.K_UP or event.key == pygame.K_w:
                    y_change = 0

        x += x_change
        y += y_change

        plane(x, y, player)
        
        frameUpdate()
        
        gameDisplay.fill((255, 255, 255))