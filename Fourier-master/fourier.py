import pygame
import math
from constants import *

pygame.init()

win = pygame.display.set_mode((1500, 800))
pygame.display.set_caption("Fourier Visualization")
PI = math.pi
clock = pygame.time.Clock()
X, Y = WIN_WIDTH // 2, 300
terms2 = None
flag = None


def draw_points(points):
    for index, point in enumerate(points):
        point[0] += 1
        try:
            win.set_at(point, BLACK)  # draws the waveform
            # pygame.draw.line(win, WHITE, point, points[index + 1], 1)
        except:
            continue


def transition(new_center, new_radius):
    global flag
    l = [i for i in range(new_radius)]
    for k in l:
        try:
            pygame.draw.circle(win, RED, new_center, k, 1)
        except ValueError:
            continue
    flag = 1


def draw_circles():
    global Y, flag
    tick = pygame.time.get_ticks() / 1000
    centres = [(250, WIN_HEIGHT // 2)]
    freq = 20
    xx, yy = 0, 0
    for k in range(terms):
        # change values of n ,radius for different functions
        n = 2 * k + 1
        radius = round(100 * (2 / (n * PI)))
        angle = round(2 * PI * freq * tick * n)
        xx = centres[k][0] + math.cos(math.radians(angle)) * radius
        yy = centres[k][1] + math.sin(math.radians(angle)) * radius
        xx = round(xx)
        yy = round(yy)
        if flag == 0:
            transition((xx, yy), radius)
        pygame.draw.circle(win, BLACK, centres[k], radius, 1)  # draws the circle
        pygame.draw.circle(win, RED, centres[k], 3)  # highlights the center
        pygame.draw.line(win, BLACK, centres[k], (xx, yy), 1)  # draws radius
        centres.insert(k + 1, (xx, yy))

    pygame.draw.circle(win, RED, (xx, yy), 3)
    pygame.draw.line(win, BLACK, (xx, yy), (WIN_WIDTH // 2, yy), 1)  # draws the generator axis
    pygame.draw.circle(win, RED, (WIN_WIDTH // 2, yy), 3)
    Y = yy
    pixels.append([X, Y])  # the list of points to generate the waveform


def redraw_game_window():
    win.fill(WHITE)
    text = font.render(f'Terms = {terms}', 1, BLACK)
    win.blit(text, (WIN_WIDTH // 2 - text.get_width() // 2, WIN_HEIGHT - 70))
    draw_circles()

    draw_points(pixels)
    pygame.display.update()

font = pygame.font.SysFont('bahnscrift', 30, True)
msg = pygame.font.SysFont('consolas', 18, True)
terms = 1
pixels = []
presscount = 0

run = True
while run:
    clock.tick(90)
    if presscount > 0:
        presscount += 1
    if presscount > 15:
        presscount = 0

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and terms < 60 and presscount == 0:
        terms += 1
        flag = 0
        presscount += 1
    if keys[pygame.K_DOWN] and terms >= 2 and presscount == 0:
        terms -= 1
        presscount += 1


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    redraw_game_window()

pygame.quit()
