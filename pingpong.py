from pygame import *
import random

#time variables
clock = time.Clock()
FPS = 60
game = True

#window
window = display.set_mode((700,500))
display.set_caption('Ping Pong Game')
background = transform.scale(image.load("background.jpg"), (700,500))

#classes
class GameSprite(sprite.Sprite):
    def __init__(self, player_img, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_img),(size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Ball(GameSprite):
    def update(self):
        self.rect.y += self.speed

        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = random.randint(0,625)

class Paddles(GameSprite):
    def update(self):
        self.rect.y += self.speed

        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = random.randint(0,625)

    def update_left(self):
        keys_pressed = key.get_pressed()
        #WSkeys
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= 10
        if keys_pressed[K_s] and self.rect.y < 350:
            self.rect.y += 10

    def update_right(self):
        keys_pressed = key.get_pressed()
        #UDkeys
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= 10
        if keys_pressed[K_DOWN] and self.rect.y < 350:
            self.rect.y += 10


#adding sprites
ball = Ball("ball.png", 300, 400, 10, 65, 65)
paddle1 = Paddles("paddle.png", 100, 100, 10, 25, 150)
paddle2 = Paddles("paddle.png", 600, 100, 10, 25, 150)

#game loop
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background, (0,0))

    ball.draw()
    paddle1.draw()
    paddle2.draw()

    paddle1.update_left()
    paddle2.update_right()

    display.update()
    clock.tick(FPS)