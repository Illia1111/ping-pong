from pygame import *

hight = 500
weight = 700

window = display.set_mode((weight,hight))

game = True






clock = time.Clock()
while game:
    a = event.get()
    for e in a:
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(60)    

