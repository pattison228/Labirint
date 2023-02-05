#створи гру "Лабіринт"!
from pygame import*


window_w = 700
window_h = 500
clock = time.Clock()
FPS = 60

window = display.set_mode((window_w, window_h))




class GameSprite(sprite.Sprite):
    def __init__(self, image, speed, x, y):
        super().__init__()
        self.image = image 
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        seld.rect.y = y
    def reset(self):
        window.blit(self.image, ())



display.set_caption("Лабіринт")
background = transform.scale(image.load("background.jpg"), (window_w, window_h))
hero = transform.scale(image.load("hero.png"), (50, 50))
cyborg = transform.scale(image.load("cyborg.png"), (50, 50))
treasure = transform.scale(image.load("treasure.png"), (50, 50))


#gromkost = 0.05
#mixer.init()
#mixer.music.load("jungles.ogg")
#mixer.music.set_volume(0.05)
#mixer.music.play()

#game = True
#while game:

    #keys_pressed = key.get_pressed()
    #if keys_pressed[K_o] and gromkost > 0:
        #gromkost -= 0.05
        #mixer.music.set_volume(gromkost)
    #if keys_pressed[K_p] and gromkost < 1:
        #gromkost += 0.05
        #mixer.music.set_volume(gromkost)


walls = [
    Wall(100, 0 ,10 ,350),
    Wall(100, 0, 600, 10),
    Wall(180, 80, 10, 600)
]

clock = time.Clock()
FPS = 60
class Player(GameSprite):
    def update(self):
    x1, y1 = 100,200
    x2, y2 = 200, 300
    speed = 10
    while game:

        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and x1 > 5:
            x1 -= speed
        if keys_pressed[K_RIGHT] and x1 < 595:
            x1 += speed
        if keys_pressed[K_UP] and y1 > 5:
            y1 -= speed
        if keys_pressed[K_DOWN] and y1 < 395:
            y1 += speed

game = True
while True: 
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background, (0, 0))
    window.blit(cyborg, (300, 400))
    window.blit(hero, (100, 200))
    window.blit(treasure, (400, 400))


    display.update()
    clock.tick(FPS)