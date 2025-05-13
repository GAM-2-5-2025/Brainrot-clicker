import pygame

w, h = 750, 750
screen = pygame.display.set_mode((w, h))

def main():

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill((0, 0, 0))
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
