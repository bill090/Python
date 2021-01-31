# import needed modules

import pygame, time, random

# initialize modules

pygame.mixer.pre_init()
pygame.init()

# define needed variables and other pygame stuff

screenWidth = 1820
screenHeight = 980
gameDisplay = pygame.display.set_mode((screenWidth, screenHeight))
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
    playMus("Python with AI - Level 2/pygame/planeGame/Explosion+3.wav")
    exitingDeath = False
    gameDisplay.fill((255, 255, 255, 0))
    displayMsg("You died", (int(screenWidth / 2), int(screenHeight / 2)), 115)
    frameUpdate()
    for x in range(0, 180):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    exitingDeath = True
        if exitingDeath:
            break
        frameUpdate()

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

def blitRotate(surf, image, pos, originPos, angle):

    # calcaulate the axis aligned bounding box of the rotated image
    w, h       = image.get_size()
    box        = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
    box_rotate = [p.rotate(angle) for p in box]
    min_box    = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
    max_box    = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

    # calculate the translation of the pivot 
    pivot        = pygame.math.Vector2(originPos[0], -originPos[1])
    pivot_rotate = pivot.rotate(angle)
    pivot_move   = pivot_rotate - pivot

    # calculate the upper left origin of the rotated image
    origin = (int(pos[0] - originPos[0] + min_box[0] - pivot_move[0]), int(pos[1] - originPos[1] - max_box[1] + pivot_move[1]))

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)

    # rotate and blit the image
    surf.blit(rotated_image, origin)

# define planes and projectiles

# Credit to @_ryan_#6862 for image 4 and player image

enemyPlane = pygame.image.load("Python with AI - Level 2/pygame/planeGame/Enemy.png")
enemyHeight = 82
missile = pygame.image.load("Python with AI - Level 2/pygame/planeGame/misslle.png")
bomb = pygame.image.load("Python with AI - Level 2/pygame/planeGame/B1.png")
player = pygame.image.load("Python with AI - Level 2/pygame/planeGame/Player.png")
cloudImage = pygame.image.load("Python with AI - Level 2/pygame/planeGame/Cloud.png")

# define enemy class

class Enemy:
    def __init__(self, x, y, shot, respawnWait, shootWait, x_change, y_change, xMovement, xMovementTime, xMovementTimeMax, yMovement, yMovementTime, yMovementTimeMax, speed, spawning, spawnAnimationTime, spawnSpeed, running, runSpeed, runSpeedWait):
        self.x = x
        self.y = y
        self.shot = shot
        self.respawnWait = respawnWait
        self.x_change = x_change
        self.y_change = y_change
        self.xMovement = xMovement
        self.xMovementTime = xMovementTime
        self.xMovementTimeMax = xMovementTimeMax
        self.yMovement = yMovement
        self.yMovementTime = yMovementTime
        self.yMovementTimeMax = yMovementTimeMax
        self.speed = speed
        self.shootWait = shootWait
        self.spawning = spawning
        self.spawnAnimationTime = spawnAnimationTime
        self.spawnSpeed = spawnSpeed
        self.running = running
        self.runSpeed = runSpeed
        self.runSpeedWait = runSpeedWait
    def move(self):
        self.x += self.x_change
        self.y += self.y_change
        return (int(self.x), int(self.y))
    def calculate(self):
        if self.spawning:
            self.y_change = self.spawnSpeed
            self.spawnAnimationTime += -1
            if self.spawnAnimationTime == 0:
                self.spawning = False
            if self.spawnAnimationTime % 10 == 0:
                self.spawnSpeed += -1
        elif self.running:
            self.y_change = self.runSpeed
            if self.runSpeedWait == 0:
                self.runSpeed += -1
                self.runSpeedWait = 5
            else:
                self.runSpeedWait += -1
            self.x_change = 0
        else:
            if self.xMovement == 1:
                self.angle = -20
            if self.xMovement == -1:
                self.angle = 20
            if self.respawnWait == 0 and self.shot:
                self.shot = False
                self.x = random.randint(0, 1710)
                self.shootWait = 60
                self.y = -100
                self.spawning = True
                self.spawnAnimationTime = 50
                self.spawnSpeed = 5
                self.runSpeedWait = 0
            if self.shot:
                self.respawnWait += -1
            self.yMovementTime += 1
            if self.yMovementTime == self.yMovementTimeMax:
                self.yMovement = self.yMovement * -1
                self.yMovementTime = 0
                self.yMovementTimeMax = random.randint(21, 41)
            self.y_change = self.speed * self.yMovement
            self.xMovementTime += 1
            if self.xMovementTime == self.xMovementTimeMax:
                self.xMovement = self.xMovement * -1
                self.xMovementTime = 0
                self.xMovementTimeMax = random.randint(41, 61)
            self.x_change = self.speed * self.xMovement
            self.shootWait += -1
    def spawnBomb(self):
        bombs.append(Bomb(self.x - 5, self.y + enemyHeight, 5))
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
    def __init__(self, x, y, direction, xSpeed, ySpeed, x_change, rotation):
        self.x = x
        self.y = y
        self.direction = direction
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.x_change = x_change
        self.rotation = rotation
    def move(self):
        self.x_change += self.xSpeed * self.direction
        self.y += 0 - self.ySpeed
        return (int(self.x + self.x_change), int(self.y))

# define cloud class

class Cloud:
    def __init__(self, x, y, x_change, y_change, xMovement, yMovement, xMovementTimeMax, yMovementTimeMax, xMovementTime, yMovementTime, speed):
        self.x = x
        self.y = y
        self.x_change = x_change
        self.y_change = y_change
        self.xMovement = xMovement
        self.yMovement = yMovement
        self.xMovementTimeMax = xMovementTimeMax
        self.yMovementTimeMax = yMovementTimeMax
        self.xMovementTime = xMovementTime
        self.yMovementTime = yMovementTime
        self.speed = speed
    def calculate(self):
        self.yMovementTime += 1
        if self.yMovementTime == self.yMovementTimeMax:
            self.yMovement = self.yMovement * -1
            self.yMovementTime = 0
            self.yMovementTimeMax = random.randint(21, 41)
        self.y_change = self.speed * self.yMovement
        self.xMovementTime += 1
        if self.xMovementTime == self.xMovementTimeMax:
            self.xMovement = self.xMovement * -1
            self.xMovementTime = 0
            self.xMovementTimeMax = random.randint(21, 41)
        self.x_change = self.speed * self.xMovement
    def move(self):
        self.x += self.x_change
        self.y += self.y_change
        return((self.x, self.y))
    def reset(self):
        self.x = random.randint(0, screenWidth - 100)
        self.y = random.randint(0, screenHeight - 100)
        self.xMovement = 1
        self.yMovement = 1
        self.xMovementTimeMax = random.randint(41, 81)
        self.yMovementTimeMax = random.randint(41, 81)
        self.xMovementTime = 0
        self.yMovementTime = 0

# define other variables

clouds = []
for x in range(0, 15):
    clouds.append(Cloud(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1))
for cloud in clouds:
    cloud.reset()
    
healthBarx = 810
healthBary = 920

volume = 100

while True:

    # reset variables

    playBackMusWait = 0
    soundPlaying = False
    menuEnd = False
    dead = False
    x_change = 0
    x = 740
    y_change = 0
    y = 720
    enemies = [Enemy(1700, -100, False, 0, 1, 0, 0, 1, 0, random.randint(21, 41), 1, 0, random.randint(21, 41), 1, True, 50, 5, False, 1, 5)]
    bombs = []
    missiles = []
    shooting = False
    shootDelay = 5
    shootingDelay = 0
    maxShoot = 5
    canShoot = True
    lives = 5
    invincibility = False
    invincibilityFrames = 0
    for cloud in clouds:
        cloud.reset()
    player = pygame.image.load("Python with AI - Level 2/pygame/planeGame/Player.png")
    playerRotation = 0
    playerAngle = 0


    # menu code

    while not menuEnd:
        displayMsg("Plane Fighting", (int(1920 / 2), int(screenHeight / 2)), 115)
        displayMsg("press space to start and q to quit. or the buttons", (int(1920/2), int(screenHeight/2) + 100), 20)
        button((255, 40, 0), (255, 0, 0), 1120, 780, 100, 100, "Quit?", 20)
        button((0, 255, 0), (90, 238, 90), 600, 780, 100, 100, "START?", 20)
        button((255, 255, 255), (100, 100, 100), 390, 780, 200, 100, "Change Volume?", 20)
        button((255, 255, 255), (255, 255, 255), 200, 100, 1, 1, f"Volume: {str(volume)}%", 20)
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] > 600 and event.pos[0] < 700 and event.pos[1] > 780 and event.pos[1] < screenHeight and event.button == 1):
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
    
    # play background music

    playBackMus("Python with AI - Level 2/pygame/planeGame/background.wav")

    # start game loop

    while not dead:
        # events code

        if lives == 0:
            die()
            dead = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameQuit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x_change = -5
                    playerRotation = 20                    
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x_change = 5
                    playerRotation = -20
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
                    playerRotation = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s or event.key == pygame.K_UP or event.key == pygame.K_w:
                    y_change = 0
                elif event.key == pygame.K_SPACE:
                    shooting = False
                    soundPlaying = True
                    playBackMusWait = 80

        # movement code

        x += x_change
        y += y_change
        x = int(x)
        y = int(y)
        if playerAngle > playerRotation:
            playerAngle += -1
        if playerAngle < playerRotation:
            playerAngle += 1

        # health bar code:

        things(healthBarx, healthBary, 10, 30, (255, 0, 0))
        if lives > 1:
            things(healthBarx + 20, healthBary, 10, 30, (255, 165, 0))
        if lives > 2:
            things(healthBarx + 40, healthBary, 10, 30, (255, 255, 0))
        if lives > 3:
            things(healthBarx + 60, healthBary, 10, 30, (90, 238, 90))
        if lives > 4:
            things(healthBarx + 80, healthBary, 10, 30, (0, 255, 0))

        # Collision detection

        if y - 80 < 0 or y + 80 > screenHeight or x - 55 < 0 or x + 55 > screenWidth:
            die()
            dead = True

        for mine in bombs:
            if ((mine.x + 10) > x - 55 and mine.x < (x + 55)) and ((mine.y + 30) > y - 80 and mine.y < (y + 80)):
                if not(invincibility):
                    lives += -1
                    invincibility = True
                    invincibilityFrames = 60
                bombs.remove(mine)

        for bullet in missiles:
            for enemy in enemies:
                if ((bullet.x + bullet.x_change + 25) > enemy.x - 55 and (bullet.x + bullet.x_change - 25) < (enemy.x + 55)) and ((bullet.y + 25) > enemy.y - int(enemyHeight / 2) and bullet.y - 25 < (enemy.y + int(enemyHeight / 2))) and not(enemy.shot) and bullet in missiles:
                    enemy.die()
                    enemy.spawnSpeed = -1
                    enemies.append(Enemy(random.randint(0, 1710), -100, False, 0, 1, 0, 0, 1, 0, random.randint(21, 41), 1, 0, random.randint(21, 41), 1, True, 50, 5, False, 1, 5))
                    for enemy2 in enemies:
                        if enemy2.x + 110 > enemy.x - 100 and enemy2.x < enemy.x + 10 + 110 and not(enemy.spawning) and not(enemy2.shot) and not(enemy2 == enemy) and not enemy2.running and not enemy2.spawning:
                            enemy2.running = True
                            enemy2.runSpeed = 1
                    enemy.running = False
                    missiles.remove(bullet)
                    soundPlaying = True
            for mine in bombs:
                if mine in bombs and bullet in missiles:
                    if ((mine.x + 50) > bullet.x and mine.x < (bullet.x + 10)) and ((mine.y + 50) > bullet.y and mine.y < (bullet.y + 30)):
                        bombs.remove(mine)
                        missiles.remove(bullet)

        for enemy in enemies:
            if ((x + 55 > enemy.x - 55 and x - 55 < (enemy.x + 55)) and ((y + 80) > enemy.y - int(enemyHeight / 2) and y - 80 < (enemy.y + int(enemyHeight / 2))) and not(enemy.shot)): 
                die()
                dead = True

        # cloud management

        for cloud in clouds:
            cloud.calculate()
            draw(cloud.move(), cloudImage)

        # missile management

        if shootingDelay > 0 and not(shooting):
            shootingDelay += -1
        if shootingDelay == 0:
            maxShoot = 5
            canShoot = True
        if shootDelay > 0:
            shootDelay += -1
        if shooting and shootDelay == 0 and maxShoot != 0:
            missiles.append(Missile(x - 5, y - 30, x_change / 5, 10, 10, 1, playerRotation))
            shootDelay = 10
            maxShoot += -1
            playMus("Python with AI - Level 2/pygame/planeGame/gunfire.wav")
        if maxShoot == 0 and shooting:
            shooting = False
            soundPlaying = True
            playBackMusWait = 80
        for bullet in missiles:
            if bullet.y > screenHeight or bullet.x > screenWidth or bullet.x < 0:
                missiles.remove(bullet)
            blitRotate(gameDisplay, missile, bullet.move(), (int(missile.get_size()[0] / 2), int(missile.get_size()[1] / 2)), bullet.rotation)

        # Enemy code

        for enemy in enemies:
            enemy.calculate()
            if not(enemy.shot):
                blitRotate(gameDisplay, enemyPlane, enemy.move(), (int(enemyPlane.get_size()[0] / 2), int(enemyPlane.get_size()[1] / 2)), 0)
                if enemy.shootWait == 0:
                    enemy.spawnBomb()
                    enemy.shootWait = 360
            if enemy.y > 0 - enemyHeight and enemy.running:
                enemy.spawning = True
                enemy.running = False
            
        for mine in bombs:
            if mine.move()[1] > screenHeight:
                bombs.remove(mine)
            draw(mine.move(), bomb)

        # player management

        if invincibility:
            invincibilityFrames += -1
        if invincibilityFrames % 2 == 0 or not(invincibility):
            blitRotate(gameDisplay, player, (x, y), (int(player.get_size()[0] / 2), int(player.get_size()[1] / 2)), playerAngle)
        if invincibilityFrames == 0:
            invincibility = False
        
        # sound management

        if playBackMusWait > 0:
            playBackMusWait += -1
        if playBackMusWait == 0 and soundPlaying:
            playBackMus("Python with AI - Level 2/pygame/planeGame/background.wav")
            soundPlaying = False
        
        frameUpdate()
        
        gameDisplay.fill((255, 255, 255))