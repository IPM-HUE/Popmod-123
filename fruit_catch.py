import pygame,random

#Pygame initialisation
pygame.init()
pygame.mixer.init()
pygame.font.init()

start = pygame.time.get_ticks()
#=====Variables=====
#Screen dimensions
screenWidth = 900
screenHeight = 700
#Time control
clock = pygame.time.Clock()
fps = 60 
#text rendering
font1 = pygame.font.SysFont("Arial",30)
font2 = pygame.font.SysFont("Arial",60)
s = 0
#Game over text
lost = font2.render(f"GAME OVER..",1,"white")
lostX = screenWidth  // 2 - lost.get_width() // 2
lostY = screenHeight // 2 - lost.get_height() // 2
#Paddle
padd_img = pygame.transform.scale_by(pygame.image.load("paddle.png"),0.3)
player = padd_img.get_rect()
playerX = screenWidth //2 - player.width // 2
playerY = (screenHeight - player.height) - 2
playerVel = 10
#Fruit 
f = ["apple",
     "avocado",
     "banana",
     "berries",
     "broccoli",
     "carrot",
     "celery",
     "cherry",
     "coconut",
     "corn",
     "cucumber",
     "lemon",
     "mushroom",
     "onion",
     "orange",
     "pear",
     "peas",
     "pepper",
     "pineapple",
     "potato",
     "pumpkin",
     "strawberry",
     "tomato",
     "watermelon",
     "half lemon",
     "half watermelon",
     "half apple",
     "half avocado",
     "half coconut",
     "half corn",
     "half cucumber",
     "half lemon",
     "half onion",
     "half orange",
     "half pear",
     "half pepper",
     "half pineapple",
     "half pumpkin",
     "half strawberry",
     "half tomato",
     "peeled banana"
    ]
i = random.randint(0,len(f)-1)
fruit_img = pygame.transform.scale_by(pygame.image.load(f"Fruits Assets/{f[i]}.png"),0.1)
fruit = fruit_img.get_rect()
fruitX = random.randint(0,screenWidth-fruit.width)
fruitY = -(fruit.height)
fruitSpeed = 2
#Screen 
win = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("FRUIT CATCH ..")
#Background music
pygame.mixer.music.load("bgsound.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.7)
#Game over sound
game_over_sound = pygame.mixer.Sound("end.wav")
game_over_sound.set_volume(1)
#=====Functions=====
#Drawing function
def draw():
    score = font1.render(f"Score:{s}",1,"white")
    win.fill((10,10,30))
    win.blit(score,(screenWidth-105,10))
    win.blit(fruit_img,(fruitX,fruitY))
    win.blit(padd_img,(playerX,playerY))
    pygame.display.update()

#Game function
def runGame():
    #Global varaible (prevent crashes)
    global playerX
    global fruit
    global fruit_img
    global fruitY
    global fruitX
    global s
    global fruitSpeed

    while True:
        i = random.randint(0,len(f)-1)
        player.topleft = (playerX,playerY)
        fruit.topleft = (fruitX,fruitY)
        clock.tick(fps)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                return
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and playerX >= 0 :
            playerX += playerVel
        if keys[pygame.K_LEFT]:
            playerX -= playerVel
        if playerX > screenWidth:
            playerX = 1
        if playerX  < -player.width:
            playerX = screenWidth - player.width
        if fruitY > screenHeight -  fruit.height:
           pygame.mixer.music.stop()
           game_over_sound.play(0)
           pygame.time.delay(500)
           win.blit(lost,(lostX,lostY))
           pygame.display.update()
           pygame.time.delay(3000)
           pygame.quit()
           return
        if player.colliderect(fruit):
            s += 1
            fruit_img = pygame.transform.scale_by(pygame.image.load(f"Fruits Assets/{f[i]}.png"),0.1)
            fruit = fruit_img.get_rect()
            fruitY = -(fruit.height)
            fruitX = random.randint(1,screenWidth-fruit.width)
        elapsed_time = (pygame.time.get_ticks() - start) // 1000
        fruitSpeed = 2 + elapsed_time // 5
        fruitY += fruitSpeed
        draw()
            



if __name__ == "__main__":
    runGame() 

