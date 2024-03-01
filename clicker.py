# Example file showing a circle moving on screen
import pygame
from random import randrange, choice

def get_rand_pos(width, height, r):
    return [randrange(0 + r, width - r - 1),randrange(0 + r, height - r - 1)]

def get_rand_color():
    return (randrange(0,200),randrange(0,200),randrange(0,200))



# pygame setup
pygame.init()
pygame.font.init()

width = 1280
height = 720

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

screen_color = "black"
circle_color = "red"
circle_width = 40

speed = 300
max_speed = 1000
min_speed = speed
speed_list = [speed, speed]
score = 0

running = True


font = pygame.font.Font('freesansbold.ttf', 32)

circle_pos = [width//2, height//2]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            # if mouse is on the circle
            if mouse_pos[0] > (circle_pos[0] - (circle_width)) and mouse_pos[0] < (circle_pos[0] + (circle_width)):
                if mouse_pos[1] > (circle_pos[1] - (circle_width)) and mouse_pos[1] < (circle_pos[1] + (circle_width)):

                    # random choice of direction and speed
                    circle_pos = get_rand_pos(width, height, circle_width)
                    speed_list[1] *= choice((-1, 1)) * randrange(min_speed, max_speed, 20)
                    speed_list[0] *= choice((-1, 1)) * randrange(min_speed, max_speed, 20)
                    # clamping speed to min and max
                    if speed_list[0] > max_speed or speed_list[0] < min_speed:
                        speed_list[0] = speed * choice((-1, 1))
                    if speed_list[1] > max_speed or speed_list[1] < min_speed:
                        speed_list[1] = speed * choice((-1, 1))
                    score += 1
        

            

    screen.fill(screen_color)

    #text
    text = font.render(f'score = {score}', True, "white")
    textRect = text.get_rect()
    textRect.center = (width // 2, 32)
    screen.blit(text, textRect)

    dt = clock.tick(60) / 1000

    circle_pos[0] += speed_list[0]*dt
    circle_pos[1] += speed_list[1]*dt

    if circle_pos[0] < (0 + circle_width) or circle_pos[0] > (width - circle_width):
        speed_list[0] = -speed_list[0]
    if circle_pos[1] < (0 + circle_width) or circle_pos[1] > (height - circle_width):
        speed_list[1] = -speed_list[1]

    pygame.draw.circle(screen, circle_color, circle_pos, circle_width)
    pygame.display.flip()

pygame.quit()