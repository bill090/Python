import pygame
import time
import random
pygame.mixer.pre_init()
pygame.init()
pygame.mixer.music.set_volume(1)
gameDisplay = pygame.display.set_mode((1820, 980))
clock = pygame.time.Clock()
fireBallImg = pygame.image.load('Python with AI - Level 2/pygame/fireBall.png')
carImg = pygame.image.load('Python with AI - Level 2/pygame/car.png')
pygame.display.set_caption('Box Dodging')
enemyCars = [pygame.image.load('Python with AI - Level 2/pygame/car4.png'), pygame.image.load('Python with AI - Level 2/pygame/car2.png'), pygame.image.load('Python with AI - Level 2/pygame/car3.png')]
enemyCarsWidths = [76, 76, 96]
enemyCarsHeights = [166, 171, 201]

def car(x, y, carImage):
    gameDisplay.blit(carImage, (x, y))

def text_objects(text, font):
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()

def chrash():
    message_display("You crashed")
    pygame.mixer.music.load("Python with AI - Level 2/pygame/Explosion+1.wav")
    pygame.mixer.music.play()
    time.sleep(3)

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (int(1820 / 2), int(980 / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def playMus(musPath):
    pygame.mixer.music.load(musPath)
    pygame.mixer.music.play()

def playBackMus(backMusPath):
    pygame.mixer.music.load(backMusPath)
    pygame.mixer.music.play(-1)

def displayMsg(msg, pos, fontSize):
    largeText = pygame.font.Font('freesansbold.ttf', fontSize)
    TextSurf, TextRect = text_objects(msg, largeText)
    TextRect.center = (pos[0], pos[1])
    gameDisplay.blit(TextSurf, TextRect)

def button(activeColor, inactiveColor, buttonX, buttonY, buttonWidth, buttonHeight, msg):
    things(buttonX, buttonY, buttonWidth, buttonHeight, inactiveColor)
    if pygame.mouse.get_pos()[0] > buttonX and pygame.mouse.get_pos()[0] < buttonX + buttonWidth and pygame.mouse.get_pos()[1] > buttonY and pygame.mouse.get_pos()[1] < buttonY + buttonHeight:
        things(buttonX, buttonY, buttonWidth, buttonHeight, activeColor)
    largeText = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = text_objects(msg, largeText)
    TextRect.center = (buttonX + int(buttonWidth/2), buttonY + int(buttonHeight/2))
    gameDisplay.blit(TextSurf, TextRect)

def gameQuit():
    pygame.quit()
    quit()

def frameUpdate():
    pygame.display.update()
    clock.tick(60)

def fireBall(x, y):
    gameDisplay.blit(fireBallImg, (x, y))

firstZaWarudo = True
volume = 100

while True:
    
    #This is the reset code.

    fireBallCoolDownTime = 60
    fireBallCoolDown = 0
    Ahit = False
    Bhit = False
    fireBallX = 0
    fireBallY = 0
    fireBallLaunched = False
    fireBallSpeed = 5
    firstZaWarudo = True
    Aresetted = False
    Await = 0
    Bresetted = False
    Bwait = 0
    gameDisplay.fill((255, 255, 255, 0))
    frameUpdate()
    menuEnd = False
    AbaseSpeed = random.randint(5, 10)
    BbaseSpeed = random.randint(5, 10)
    thingA_startx = random.randint(0, 600)
    thingA_starty = -600
    thingA_speed = 7
    AcarNum = random.randint(0, len(enemyCars) - 1)
    Acar = enemyCars[AcarNum]
    thingA_height = enemyCarsHeights[AcarNum]
    thingA_width = enemyCarsWidths[AcarNum]
    thingB_startx = random.randint(0, 600)
    thingB_starty = -600
    thingB_speed = 7
    BcarNum = random.randint(0, len(enemyCars) - 1)
    Bcar = enemyCars[BcarNum]
    thingB_height = enemyCarsHeights[BcarNum]
    thingB_width = enemyCarsWidths[BcarNum]
    points = 0
    passedA = False
    passedB = False
    speedIncreaseCounter = 3
    carSpeed = 5
    chrashed = False
    x_change = 0
    x = 400
    y = 980 - 166
    zaWarudoMaxTime = 600
    zaWarudoTime = 600
    zaWarudoEffect = False
    speedChange = 0
    zaWarudoCoolDownTime = 600
    zaWarudoCoolDown = 0

    # This is the start menu

    while not menuEnd:
        displayMsg("Box Dodging", (int(1920 / 2), int(980 / 2)), 115)
        displayMsg("press space to start and q to quit. or the buttons", (int(1920/2), int(980/2) + 100), 20)
        button((255, 40, 0), (255, 0, 0), 1120, 780, 100, 100, "Quit?")
        button((0, 255, 0), (90, 238, 90), 600, 780, 100, 100, "START?")
        button((255, 255, 255), (100, 100, 100), 390, 780, 200, 100, "Change Volume?")
        button((255, 255, 255), (255, 255, 255), 200, 100, 1, 1, str(volume))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameQuit()
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] > 600 and event.pos[0] < 700 and event.pos[1] > 780 and event.pos[1] < 980 and event.button == 1):
                menuEnd = True
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_q) or (event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] > 1120 and event.pos[0] < 1220 and event.pos[1] > 780 and event.pos[1] < 880 and event.button == 1):
                gameQuit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] > 390 and event.pos[0] < 590 and event.pos[1] > 780 and event.pos[1] < 880 and event.button == 1:
                if volume == 100:
                    volume = 0
                else:
                    volume += 10
        frameUpdate()
        gameDisplay.fill((255, 255, 255, 0))
    pygame.mixer.music.set_volume(volume / 100)
    # This line starts the background music

    playBackMus("Python with AI - Level 2/pygame/JoJo's Bizarre Adventure_Golden Wind OST_ _Giorno's Theme_.wav")
    

    # This is the game's loop

    while not chrashed:
        largeText = pygame.font.Font('freesansbold.ttf', 20)
        TextSurf, TextRect = text_objects(f"score: {points}", largeText)
        TextRect.center = (200, 50)
        gameDisplay.blit(TextSurf, TextRect)
        gameEvents = pygame.event.get()

        # This handles the game's functions

        for event in gameEvents:
            if event.type == pygame.QUIT:
                gameQuit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x_change = 0 - carSpeed - speedChange
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x_change = carSpeed + speedChange
                if event.key == pygame.K_UP:
                    speedChange = 5
                elif event.key == pygame.K_w:
                    speedChange = 5
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    speedChange = -2
                if event.key == pygame.K_SPACE and zaWarudoCoolDownOver:
                    zaWarudoEffect = True
                    zaWarudoCoolDownOver = False
                    zaWarudoCoolDown = int(zaWarudoCoolDownTime/1)
                    zaWarudoTime = int(zaWarudoMaxTime/1) 
                    pygame.mixer.music.set_volume(3)
                    playMus("Python with AI - Level 2/pygame/zaWarudo.wav")
                if event.key == pygame.K_LSHIFT and not(fireBallLaunched) and fireBallCoolDown == 0:
                    fireBall(x, y - 148)
                    fireBallX = x
                    fireBallY = 980 - 166 - 148
                    fireBallLaunched = True
                    fireBallCoolDown = fireBallCoolDownTime
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_d or event.key == pygame.K_a:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    speedChange = 0
        x += x_change

        # This area handles collision

        if x > 1820 - 76 or x < 0:
            if not zaWarudoEffect:
                chrash()
                chrashed = True
            else:
                x += 0 - x_change
        if (y < thingA_starty + thingA_height and not(Aresetted)) or (y < thingB_starty + thingB_height and not(Bresetted)):
            if (((x > thingA_startx and x < thingA_startx + thingA_width) or (x + 76 > thingA_startx and x + 76 < thingA_startx + thingA_width)) and not(Aresetted) and y < thingA_starty + thingA_height) or ((x > thingB_startx and x < thingB_startx + thingB_width) or (x + 76 > thingB_startx and x + 76 < thingB_startx + thingB_width)) and not(Bresetted) and y < thingB_starty + thingB_height:
                if not zaWarudoEffect:
                    chrash()
                    chrashed = True
                    break
                else:
                    x += 0 - x_change
            if not(passedA) and (not(x > thingA_startx and x < thingA_startx + thingA_width) or (x + 76 > thingA_startx and x + 76 < thingA_startx + thingA_width) and not(Aresetted)):
                points += 10
                if zaWarudoMaxTime > 540:
                    zaWarudoMaxTime += 10
                if zaWarudoCoolDown < 180:
                    zaWarudoCoolDownTime += -10
                passedA = True
            if not(passedB) and (not(x > thingB_startx and x < thingB_startx + thingB_width) or (x + 76 > thingB_startx and x + 76 < thingB_startx + thingB_width) and not(Bresetted)):
                points += 10
                if zaWarudoMaxTime > 540:
                    zaWarudoMaxTime += 10
                if zaWarudoCoolDown < 180:
                    zaWarudoCoolDownTime += -10
                passedB = True
        if not zaWarudoEffect:
            thingA_starty += AbaseSpeed + speedChange
            thingB_starty += BbaseSpeed + speedChange
            zaWarudoCoolDown += -1

        # This area handles the fireball movement and resetting

        if fireBallLaunched:
            fireBallY += 0 - fireBallSpeed
            fireBall(fireBallX, fireBallY)
        
        if fireBallY <= -148:
            fireBallLaunched = False

        # This area handles the fireball collision

        if fireBallY < thingA_starty + thingA_height and fireBallX + 113 > thingA_startx and fireBallX < thingA_startx + thingA_width and fireBallLaunched:
            Await = 0
            Ahit = True
            fireBallLaunched = False
        if fireBallY < thingB_starty + thingB_height and fireBallX + 113 > thingB_startx and fireBallX < thingB_startx + thingB_width and fireBallLaunched:
            Bwait = 0
            Bhit = True
            fireBallLaunched = False
            
        # This area handles the enemy spawning.

        if thingA_starty < 980 and not(Ahit):
            car(thingA_startx, thingA_starty, Acar)
        elif (Await == 0 and Aresetted) or Ahit:
            if not(Ahit):
                speedIncreaseCounter = speedIncreaseCounter - 1
                passedA = False
            if speedIncreaseCounter == 0:
                speedIncreaseCounter = 3
                AbaseSpeed += 1
                BbaseSpeed += 1
                carSpeed += 1
                fireBallSpeed += 1
            AcarNum = random.randint(0, len(enemyCars) - 1)
            Acar = enemyCars[AcarNum]
            thingA_height = enemyCarsHeights[AcarNum]
            thingA_width = enemyCarsWidths[AcarNum]
            thingA_startx = random.randint(0, 1920 - thingA_width)
            thingA_starty = -100 - thingA_height
            car(thingA_startx, thingA_starty, Acar)
            Aresetted = False
            Ahit = False
        else:
            Aresetted = True
            Await  = random.randint(0, 120)
        if thingB_starty < 980 and not(Bhit):
            car(thingB_startx, thingB_starty, Bcar)
        elif (Bwait == 0 and Bresetted) or Bhit:
            
            if not(Bhit):
                speedIncreaseCounter = speedIncreaseCounter - 1
                passedB = False
            if speedIncreaseCounter == 0:
                speedIncreaseCounter = 3
                AbaseSpeed += 1
                BbaseSpeed += 1
                carSpeed += 1
                fireBallSpeed += 1
            BcarNum = random.randint(0, len(enemyCars) - 1)
            Bcar = enemyCars[BcarNum]
            thingB_height = enemyCarsHeights[BcarNum]
            thingB_width = enemyCarsWidths[BcarNum]
            thingB_startx = random.randint(0, 1920 - thingB_width)
            thingB_starty = -100 - thingB_height
            car(thingB_startx, thingB_starty, Bcar)
            Bresetted = False
            Bhit = False
        else:
            Bresetted = True
            Bwait  = random.randint(0, 120)

        # This handles most of the time stop functions

        if firstZaWarudo and zaWarudoEffect:
            displayMsg("You're DIO?", (400, 300), 20)
        car(x, y, carImg)
        if zaWarudoEffect:
            zaWarudoTime += -1
        if zaWarudoTime == 90:
            playMus("Python with AI - Level 2/pygame/timeResumes.wav")
        if zaWarudoTime <= 0 and zaWarudoEffect:
            zaWarudoEffect = False
            firstZaWarudo = False
            playBackMus("Python with AI - Level 2/pygame/JoJo's Bizarre Adventure_Golden Wind OST_ _Giorno's Theme_.wav")
        if zaWarudoCoolDown <= 0:
            zaWarudoCoolDownOver = True

        # This handles the box respawn delays
        
        if Await > 0:
            Await += -1
        if Bwait > 0:
            Bwait += -1

        # This updates the game

        frameUpdate()

        # This is the fireball cooldown

        if not(fireBallLaunched) and fireBallCoolDown > 0:
            fireBallCoolDown += -1

        # This clears the screen for the next frame

        gameDisplay.fill((255, 255, 255, 0))