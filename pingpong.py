from pygame import *

clock = time.Clock()
FPS = 60
game = True

window = display.set_mode((700,500))
display.set_caption('Ping Pong Game')

class ball():
    def update(self):
        self.rect.y += self.speed

        if self.rect.y > 500:
            global missed_counter
            missed_counter += 1
            self.rect.y = 0
            self.rect.x = random.randint(0,625)

class paddles():
    def update(self):
        self.rect.y += self.speed

        if self.rect.y > 500:
            global missed_counter
            missed_counter += 1
            self.rect.y = 0
            self.rect.x = random.randint(0,625)



while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.fill(255,255,255)

    display.update()
    clock.tick(FPS)