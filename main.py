import pygame
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
    def __init__(self, x, y, w, h, image):
        self.rect = pygame.Rect(x, y, w, h)
        image = pygame.transform.scale(image, (w, h))
        self.image = image
    

    def move(self, a, d):
        keys = pygame.key.get_pressed()
        if keys[d]:
            self.rect.x += 5
        if keys[a]:
            self.rect.x -= 5




player1_img = pygame.image.load("rocket.png")
player1 = Player(350, 450, 50, 50, player1_img)


#оброби подію «клік за кнопкою "Закрити вікно"»
game = True
while game:
    
    window.blit(background, (0, 0))
    player1.draw()
    player1.move(pygame.K_a, pygame.K_d)
    



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    pygame.display.update()
    clock.tick(FPS)