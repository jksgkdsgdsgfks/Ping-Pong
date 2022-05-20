from pygame import *

window = display.set_mode((700, 500))
display.set_caption("Пинг Понг")
background = transform.scale(image.load("Фон.jpg"), (700, 500))

FPS = 60
clock= time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_weidth, player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_weidth, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):

        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
    
        if keys_pressed[K_s] and self.rect.y < 450:
            self.rect.y += self.speed
    def update_r(self):

        keys_pressed = key.get_pressed()

        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
    
        if keys_pressed[K_DOWN] and self.rect.y < 450:
            self.rect.y += self.speed

raketka_l = Player("Ракетка.png", 50, 250, 10, 15, 30)
raketka_r = Player("Ракетка.png", 650, 250, 10, 15, 30)
game = True
Finish = False
while game:

    if Finish != True:

        for e in event.get():
            if e.type == QUIT:
                game = False
        

        window.blit(background, (0, 0))
        raketka_l.reset()
        raketka_r.reset()
        raketka_l.update_l()
        raketka_r.update_r()




    display.update()
    clock.tick(FPS)
