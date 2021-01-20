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

def draw(pos, image):
    gameDisplay.blit(image, pos)

# define planes and projectiles

enemyPlanes = [pygame.image.load("Python with AI - Level 2/pygame/planeGame/L1.png"), pygame.image.load("Python with AI - Level 2/pygame/planeGame/L2.png"), pygame.image.load("Python with AI - Level 2/pygame/planeGame/L3.png"), pygame.image.load("Python with AI - Level 2/pygame/planeGame/L4.png")]
enemyHeights = [78, 65, 58, 49]
missile = pygame.image.load("Python with AI - Level 2/pygame/planeGame/misslle.png")
bomb = pygame.image.load("Python with AI - Level 2/pygame/planeGame/B1.png")
player = pygame.image.load("Python with AI - Level 2/pygame/planeGame/RFA Fighter.png")

# define enemy class

class Enemy:
    def __init__(self, x, y, imageNum, shot, respawnWait, shootWait, x_change, y_change, xMovement, xMovementTime, yMovement, yMovementTime, speed):
        self.x = x
        self.y = y
        self.shot = shot
        self.imageNum = imageNum
        self.respawnWait = respawnWait
        self.x_change = x_change
        self.y_change = y_change
        self.xMovement = xMovement
        self.xMovementTime = xMovementTime
        self.yMovement = yMovement
        self.yMovementTime = yMovementTime
        self.speed = speed
        self.shootWait = shootWait
    def move(self):
        self.x += self.x_change
        self.y += self.y_change
        return (int(self.x), int(self.y))
    def calculate(self):
        if self.respawnWait == 0 and self.shot:
            self.imageNum = random.randint(0, 3)
            self.shot = False
            self.x = random.randint(0, 1820)
            self.shootWait = 60
        if self.shot:
            self.respawnWait += -1
        self.yMovementTime += 1
        if self.yMovementTime == 21:
            self.yMovement = self.yMovement * -1
            self.yMovementTime = 0
        self.y_change = self.speed * self.yMovement
        self.xMovementTime += 1
        if self.xMovementTime == 41:
            self.xMovement = self.xMovement * -1
            self.xMovementTime = 0
        self.x_change = self.speed * self.xMovement
        self.shootWait += -1
    def spawnBomb(self):
        bombs.append(Bomb(self.x + 30, self.y + 200, 5))
    def die(self):
        self.shot = True
        self.respawnWait = 30

# define bomb class

class Bomb:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
    def move(self):
        self.y += self.speed
        return (int(self.x), int(self.y))

# define missile class

class Missile:
    def __init__(self, x, y, direction, speed, x_change):
        self.x = x
        self.y = y
        self.direction = direction
        self.speed = speed
        self.x_change = x_change
    def move(self):
        self.x_change += self.speed * self.direction
        self.y += 0 - self.speed
        return (int(self.x + self.x_change), int(self.y))


while True:

    # reset variables

    volume = 100
    menuEnd = False
    dead = False
    x_change = 0
    x = 740
    y_change = 0
    y = 720
    enemies = [Enemy(100, 100, 2, False, 0, 1, 0, 0, 1, 0, 1, 0, 1), Enemy(300, 100, 2, False, 0, 1, 0, 0, 1, 0, 1, 0, 1), Enemy(500, 100, 2, False, 0, 1, 0, 0, 1, 0, 1, 0, 1), Enemy(900, 100, 2, False, 0, 1, 0, 0, 1, 0, 1, 0, 1), Enemy(1100, 100, 2, False, 0, 1, 0, 0, 1, 0, 1, 0, 1), Enemy(1300, 100, 2, False, 0, 1, 0, 0, 1, 0, 1, 0, 1), Enemy(1500, 100, 2, False, 0, 1, 0, 0, 1, 0, 1, 0, 1), Enemy(1700, 100, 2, False, 0, 1, 0, 0, 1, 0, 1, 0, 1)]
    bombs = []
    missiles = []
    shooting = False
    shootDelay = 5
    shootingDelay = 0
    maxShoot = 5
    canShoot = True

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
        # events code

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
                elif event.key == pygame.K_SPACE and canShoot:
                    shooting = True
                    maxShoot = 5
                    shootingDelay = 60
                    canShoot = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x_change = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s or event.key == pygame.K_UP or event.key == pygame.K_w:
                    y_change = 0
                elif event.key == pygame.K_SPACE:
                    shooting = False

        # movement code

        x += x_change
        y += y_change
        x = int(x)
        y = int(y)

        # missile management

        if shootingDelay > 0 and not(shooting):
            shootingDelay += -1
        if shootingDelay == 0:
            maxShoot = 5
            canShoot = True
        if shootDelay > 0:
            shootDelay += -1
        if shooting and shootDelay == 0 and maxShoot != 0:
            missiles.append(Missile(x + 42, y - 76, x_change / 5, 10, 1))
            shootDelay = 10
            maxShoot += -1
        if maxShoot == 0:
            shooting = False
        for bullet in missiles:
            if bullet.y > 980 or bullet.x > 1820 or bullet.x < 0:
                missiles.remove(bullet)
            draw(bullet.move(), missile)

        # Collision detection

        if y < 400 or y + 160 > 980 or x < 0 or x + 110 > 1820:
            die()
            dead = True

        for mine in bombs:
            if ((mine.x + 50) > x and mine.x < (x + 110)) and ((mine.y + 50) > y and mine.y < (y + 160)):
                die()
                dead = True

        for bullet in missiles:
            for enemy in enemies:
                if ((bullet.x + bullet.x_change + 50) > enemy.x and (bullet.x + bullet.x_change) < (enemy.x + 110)) and ((bullet.y + 50) > enemy.y and bullet.y < (enemy.y + enemyHeights[enemy.imageNum])):
                    enemy.die()

        # Enemy code

        for enemy in enemies:
            enemy.calculate()
            if not(enemy.shot):
                draw(enemy.move(), enemyPlanes[enemy.imageNum])
            if enemy.shootWait == 0:
                enemy.spawnBomb()
                enemy.shootWait = 360

        for mine in bombs:
            if mine.move()[1] > 980:
                bombs.remove(mine)
            draw(mine.move(), bomb)

        draw((x, y), player)
        
        frameUpdate()
        
        gameDisplay.fill((255, 255, 255))