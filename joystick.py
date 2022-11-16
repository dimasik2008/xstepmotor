import pygame as pg
pg.init()
pg.display.set_caption("TeraBot")
screen = pg.display.set_mode((500,500),0,32)

pg.joystick.init()
joysticks = [pg.joystick.Joystick(i) for i in range(pg.joystick.get_count())]


while True:
    screen.fill((0,0,0))
    for event in pg.event.get():
        if event.type == pg.JOYBUTTONDOWN:
            print(event)
        if event.type == pg.JOYAXISMOTION:
            if event.axis == 0:
                if event.value > 0.5:
                    print("right")
                elif event.value < -0.5:
                    print("left")
                else:
                    print("stop")
        # if event.type == pg.JOYHATMOTION:
        #     print(event)
        if event.type == pg.QUIT:
            pg.quit()