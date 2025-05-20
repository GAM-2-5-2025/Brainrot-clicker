import pygame
import time

w, h = 1600, 900

color_light = (170, 170, 170)
color_dark = (100, 100, 100)
black=(0,0,0)
white = (255, 255, 255)

screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Brainrot Clicker')
color = (0, 0, 255)


def main():
    buy_1 = 0
    buy_2 = 0
    buy_3 = 0


    bought_multiplier_1 = 1.5
    bought_multiplier_2 = 10
    bought_multiplier_3 = 150
    pygame.init()
    br = 0
    click_timestamps = []
    max_cps_allowed = 20
    run = True
    multiplier=1
    clock = pygame.time.Clock()
    while run:
        
        dt = clock.tick(60) / 1000.0  # Convert milliseconds to seconds
        value_1= 10 + buy_1 * bought_multiplier_1
        value_2 = 100 + buy_2 * bought_multiplier_2
        value_3 = 1000 + buy_3 * bought_multiplier_3
        mouse = pygame.mouse.get_pos()


        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                run = False

            if ev.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                now = time.time()

                click_timestamps = [t for t in click_timestamps if now - t <= 1]

                if len(click_timestamps) >= max_cps_allowed:
                    print(f"Too many clicks! CPS = {len(click_timestamps)}")
                    br = 0  # Reset clicks as penalty
                    click_timestamps = []
                else:
                    if 750 <= mouse[0] <= 750 + 200 and 350 <= mouse[1] <= 350 + 200:
                        br += multiplier
                        click_timestamps.append(now)


                if 1400 <= mouse[0] <= 1400 + 150 and 450 <= mouse[1] <= 450 + 40 and br >= value_1:
                    br -= value_1
                    multiplier += 1
                    buy_1 += 1

                if 1400 <= mouse[0] <= 1400 + 150 and 650 <= mouse[1] <= 650 + 40 and br >= value_3:
                    br -= value_3
                    buy_3 += 1

                if 1400 <= mouse[0] <= 1400 + 150 and 550 <= mouse[1] <= 550 + 40 and br >= value_2:
                    br -= value_2
                    buy_2 += 1

        # Passive income
        if buy_2 > 0:
            br += buy_2 * 0.5 * dt

        if buy_3 > 0:
            br += buy_3 * 15 * dt

        screen.fill(color)


        screen.fill((255, 255, 255))

        # Text through GUI
        myFont1 = pygame.font.SysFont("Comic Sans", 100)
        myFont2 = pygame.font.SysFont("Comic Sans", 20)

        NumLabel = myFont1.render(f"Brainrot: {str(round(br, 1))}", 1, black)
        touch = myFont2.render(f"The Mouse: {multiplier}", 1, white)
        cursor = myFont2.render(f"The Cursor: {buy_2}", 1, white)
        skibidi_toilet = myFont2.render(f"The Skibidi: {buy_3}", 1, white)


        screen.blit(NumLabel, (100, 20))




        # if mouse is hovered on a button it
        # changes to lighter shade
        if 750 <= mouse[0] <= 750 + 200 and 350 <= mouse[1] <= 350 + 200:
            pygame.draw.rect(screen, color_light, [750, 350, 200, 200])

        else:
            pygame.draw.rect(screen, color_dark, [750, 350, 200, 200])


        if 1400 <= mouse[0] <= 1400 + 150 and 450 <= mouse[1] <= 450 + 40:
            pygame.draw.rect(screen, color_light, [1400, 450, 150, 40])

        else:
            pygame.draw.rect(screen, color_dark, [1400, 450, 150, 40])

        if 1400 <= mouse[0] <= 1400 + 150 and 550 <= mouse[1] <= 550 + 40:
                pygame.draw.rect(screen, color_light, [1400, 550, 150, 40])

        else:
            pygame.draw.rect(screen, color_dark, [1400, 550, 150, 40])

        if 1400 <= mouse[0] <= 1400 + 150 and 650 <= mouse[1] <= 650 + 40:
                pygame.draw.rect(screen, color_light, [1400, 650, 150, 40])

        else:
            pygame.draw.rect(screen, color_dark, [1400, 650, 150, 40])




        screen.blit(touch, (1400, 450))
        screen.blit(cursor, (1400, 550))
        screen.blit(skibidi_toilet, (1400, 650))


        pygame.display.update()


    print(round(br, 2))
    print(buy_1, buy_2, buy_3)

    pygame.quit()


if __name__ == '__main__':
    main()
