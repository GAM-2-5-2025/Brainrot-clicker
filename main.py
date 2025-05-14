import pygame
import random



w, h = 1600, 900


color_light = (170, 170, 170)
color_dark = (100, 100, 100)
black=(0,0,0)


screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Brainrot Clicker')



def main():
    pygame.init()
    br = 0
    run = True
    value_1=10
    multiplier=1
    while run:

        mouse = pygame.mouse.get_pos()


        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                run = False




            if ev.type == pygame.MOUSEBUTTONDOWN:

                # if the mouse is the
                # button adds a thing
                if w / 2 <= mouse[0] <= w / 2 + 140 and h / 2 <= mouse[1] <= h / 2 + 40:
                    br+=multiplier
                if 400 <= mouse[0] <= 400 + 140 and 450 <= mouse[1] <= 450 + 40 and br >= value_1:
                    br-= value_1
                    multiplier += 0.2


        screen.fill((255,255, 255))

        # stores the (x,y) coordinates into
        # the variable as a tuple

        # Text through GUI
        myFont = pygame.font.SysFont("Comic Sans", 100)

        randNumLabel = myFont.render("You have clicked button:", 1, black)
        diceDisplay = myFont.render(str(round(br, 2)), 1, black)

        screen.blit(randNumLabel, (100, 20))
        screen.blit(diceDisplay, (520, 145))

        pygame.display.flip()


        # if mouse is hovered on a button it
        # changes to lighter shade
        if w / 2 <= mouse[0] <= w / 2 + 140 and h / 2 <= mouse[1] <= h / 2 + 40:
            pygame.draw.rect(screen, color_light, [w / 2, h / 2, 140, 40])

        else:
            pygame.draw.rect(screen, color_dark, [w / 2, h / 2, 140, 40])


        if 400 <= mouse[0] <= 400 + 140 and 450 <= mouse[1] <= 450 + 40:
            pygame.draw.rect(screen, color_light, [400, 450, 140, 40])

        else:
            pygame.draw.rect(screen, color_dark, [400, 450, 140, 40])


        pygame.display.update()


    print(round(br, 2))

    pygame.quit()


if __name__ == '__main__':
    main()
