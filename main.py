import pygame, sys
from models import Sprite, Mover, win

pygame.init()

player = Mover(0, 0, 30, 30, 5, "man")
house = Sprite(250, 5, 170, 100, "house")
door = Sprite(321, 75, 30, 35, "door")
friend = Mover(50, 50, 30, 30, 5, "friend")

bg = pygame.image.load("images/bg.png")

pygame.display.set_caption("First Game")

while True:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    win.blit(bg, (0, 0))

    player.collide(house)
    friend.moved(player.collide(friend))
    friend.collide(house)
    if friend.collide(door) == "down":
        pygame.quit()
        sys.exit(0)

    player.move()

    house.draw()
    door.draw()
    friend.draw()
    player.draw()

    pygame.display.update()
