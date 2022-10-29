from pygame import *

clock = time.Clock()
FPS = 60

game = True

window = display.set_mode((700,500))
display.set_caption('Ping Pong Game')
background = transform.scale(image.load("galaxy.jpg"), (700,500))


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background, (0,0))

    display.update()
    clock.tick(FPS)