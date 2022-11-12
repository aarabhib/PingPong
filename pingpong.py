from pygame import *
import random

#variables
clock = time.Clock()
FPS = 60
game = True
finish = False
counter = 0

#window
window = display.set_mode((700,500))
display.set_caption('Ping Pong Game')
background = transform.scale(image.load("background.jpg"), (700,500))

#classes
class GameSprite(sprite.Sprite):
    def __init__(self, player_img, player_x, player_y, x_speed, y_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_img),(size_x,size_y))
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Ball(GameSprite):
    def update(self):
        self.rect.y += self.y_speed
        self.rect.x += self.x_speed

        if self.x_speed > 0 and self.rect.x > 700-30:
            self.x_speed = -self.x_speed

        if self.x_speed < 0 and self.rect.x < 0:
            self.x_speed = -self.x_speed

        if self.y_speed > 0 and self.rect.y > 500-30:
            self.y_speed = -self.y_speed

        if self.y_speed < 0 and self.rect.y < 0:
            self.y_speed = -self.y_speed


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

class Button():
    def __init__(self, x, y, img):
        self.img = transform.scale(image.load("button.png"), (100,30))
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.img, (self.rect.x, self.rect.y))


#adding sprites
ball = Ball("ball.png", 300, 400, 10, 10, 60, 60)
paddle1 = Paddles("paddle.png", 10, 100, 10, 0, 25, 150)
paddle2 = Paddles("paddle.png", 670, 100, 10, 0, 25, 150)
restart_button = Button(300, 400, "button.png")

#text
font.init()
font1 = font.SysFont('Papyrus', 35, True)
font2 = font.SysFont('Papyrus', 25, True)
lose = font1.render('GAME OVER', True, (250, 250, 250))
restart_text = font2.render('Restart', True, (0,0,0))

#game loop
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == MOUSEBUTTONUP:
            if e.pos[0] > 300 and e.pos[0] < 400 and e.pos[1] > 400 and e.pos[1] < 425:
                finish = False
                ball.rect.x = 350
                ball.rect.y = 250 

    if finish != True:
        window.blit(background, (0,0))

        ball.draw()
        ball.update()

        paddle1.draw()
        paddle2.draw()

        paddle1.update_left()
        paddle2.update_right()

        if sprite.collide_rect(ball, paddle1):
            ball.x_speed = -ball.x_speed

        if sprite.collide_rect(ball, paddle2):
            ball.x_speed = -ball.x_speed

        if ball.rect.x < 10:
            counter += 1

        if ball.rect.x > 670:
            counter += 1

        if counter >= 10:
            finish = True
            window.blit(background, (0,0))
            window.blit(lose, (200,200))
            restart_button.draw()
            counter = 0
            window.blit(restart_text, (300,400))

    display.update()
    clock.tick(FPS)