import pygame
from random import randint
#from map2 import

pygame.init()

FPS = 60
clock = pygame.time.Clock()
#створи вікно гри

wind_w, wind_h = 700, 500
window = pygame.display.set_mode((wind_w, wind_h))
pygame.display.set_caption("Шутер")


#задай фон сцени
background = pygame.image.load("galaxy.jpg")
background = pygame.transform.scale(background, (wind_w, wind_h))

#створи 2 спрайти та розмісти їх на сцені
pygame.mixer.music.load("space.ogg")
pygame.mixer.music.play(-1)


class Sprait:
    def __init__(self, x, y, w, h, image):
        self.rect = pygame.Rect(x, y, w, h)
        image = pygame.transform.scale(image, (w, h))
        self.image = image
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(Sprait):
    def __init__(self, x, y, w, h, image, speed=5):
        self.speed=speed
        super().__init__(x, y, w, h, image)

    def fire(self):
        bullets.append(Bullet(self.rect.x+20,self.rect.y,10,20,bullet_img,15))

    

    def move(self, a, d):
        keys = pygame.key.get_pressed()

        if keys [d]:
            if self.rect.right <= wind_w:
                self.rect.x += self.speed

        if keys [a]:
            if self.rect.x > 0:
                self.rect.x -= self.speed

class Bullet(Sprait):
        def __init__(self, x, y, w, h, image, speed=15):
            self.speed=speed
            super().__init__(x, y, w, h, image)
        def move(self):
            self.rect.y -= self.speed

    

class Enemy(Sprait):
        def __init__(self, x, y, w, h, image, speed=5):
            self.speed=speed
            super().__init__(x, y, w, h, image)
        def move(self):
            self.rect.y += self.speed
            if self.rect.y > wind_h:
                self.rect.y = randint(-200, -50)
                self.rect.x = randint(50, 650) 
                self.rect.y += self.speed



enemys = []
ufo_imp = pygame.image.load("ufo.png")
enemys.append(Enemy(randint(50, 650), randint(-200, -50), 50, 50, ufo_imp))
enemys.append(Enemy(randint(50, 650), randint(-200, -50), 50, 50, ufo_imp))
enemys.append(Enemy(randint(50, 650), randint(-200, -50), 50, 50, ufo_imp))
enemys.append(Enemy(randint(50, 650), randint(-200, -50), 50, 50, ufo_imp))
enemys.append(Enemy(randint(50, 650), randint(-200, -50), 50, 50, ufo_imp))
player1_img = pygame.image.load("rocket.png")
player1 = Player(350, 450, 50, 50, player1_img)

bullet_img = pygame.image.load("bullet.png")
bullets = []

ufo_imp = pygame.image.load("ufo.png")
#оброби подію «клік за кнопкою "Закрити вікно"»
game = True
while game:
    
    window.blit(background, (0, 0))
    player1.draw()
    player1.move(pygame.K_a, pygame.K_d)

    for bullet in bullets:
        bullet.draw()

        bullet.move()

    for enemy in enemys:
        enemy.draw()

        enemy.move() 

    



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            player1.fire()

        
            


    pygame.display.update()
    clock.tick(FPS)
