# Snake Game!

# small fixes by Rahul
 
# our game imports

import pygame, sys, random, time


pygame.mixer.pre_init(44100,16,2,4096)

print ("Welcome to Snake Baabuuu!!!")
time.sleep(1)
print ("Devloped by RaHuL")
time.sleep(0.5)


def bgmusic():
    
    pygame.mixer.music.load("swift.mp3")
    pygame.mixer.music.set_volume(0.6)
    pygame.mixer.music.play(-1)

def endmusic():
    pygame.mixer.music.load("beat.MP3")
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play()
    
    
 
# check for initializing errors

check_errors = pygame.init()
if check_errors[1] > 0:
    print("(!) Had {0} initializing errors, exiting...".format(check_errors[1]))
    sys.exit([0])
else:
    print("PyGame successfully initialized!")
    bgmusic()
 
# Play surface

playSurface = pygame.display.set_mode((720, 460))



pygame.display.set_caption('Snake BaBuu!!')

     
# Colors

red = pygame.Color(255, 0, 0) 
green = pygame.Color(0, 255, 0) 
black = pygame.Color(0, 0, 0) 
white = pygame.Color(255, 255, 255) 
brown = pygame.Color(165, 42, 42)
magneta = pygame.Color(255,0, 255)
blue = pygame.Color(0,0,139)
gray = pygame.Color(0,128,128)
 
# FPS controller

fpsController = pygame.time.Clock()
 
#varibles

snakePos = [100, 50]
snakeBody = [[100,50], [90,50], [80,50]]
 
foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
foodSpawn = True
 
direction = 'RIGHT'
changeto = direction
 
score = 0
 
# Game over 

def gameOver():
    myFont = pygame.font.SysFont('Helvetica', 85, "bold italic")
    GOsurf = myFont.render('Game over!', True , blue)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360, 20)
    playSurface.blit(GOsurf,GOrect)
    showScore(0)
    time.sleep(1)
    print ("Thank You! Play Again Soon")
    pygame.display.flip()
    endmusic()
    time.sleep(6)
    pygame.quit() 
    sys.exit([0]) 
   
def showScore(choice=1):
    sFont = pygame.font.SysFont('monaco', 35)
    Ssurf = sFont.render('Score : {0}'.format(score) , True, brown)
    Srect = Ssurf.get_rect()
    if choice == 1:
        Srect.midtop = (650,10)
    else:
        Srect.midtop = (360, 120)
       
    playSurface.blit(Ssurf,Srect)

bg_image = pygame.image.load("grass1.jpg").convert()
   
   
# Main Logic 

while True:
    
    for event in pygame.event.get():
         
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeto = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeto = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeto = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
 
    # validation of direction
    
    if changeto == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeto == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeto == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeto == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'
 
    # Update snake position [x,y]
    
    if direction == 'RIGHT':
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] -= 10
    if direction == 'DOWN':
        snakePos[1] += 10
   
   
    # Snake body 
    
    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        score += 5
        foodSpawn = False
        
    else:
        snakeBody.pop()
       
    #Food 
        
    if foodSpawn == False:
        foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
    foodSpawn = True
    
   
    #Background
    
    playSurface.blit(bg_image,[0,0])
    
   
    # Snake
    
    for pos in snakeBody:
        pygame.draw.rect(playSurface, black, pygame.Rect(pos[0],pos[1],10,10))
   
    pygame.draw.rect(playSurface, red, pygame.Rect(foodPos[0],foodPos[1],10,10))

   
    # Bound
    
    if snakePos[0] > 710 or snakePos[0] < 0:
        gameOver()
    if snakePos[1] > 450 or snakePos[1] < 0:
        gameOver()
       
    # Self hit
    
    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[1] == block[1]:
            gameOver()

   
    
    showScore()
    
    pygame.display.flip()
   
    fpsController.tick(15)
