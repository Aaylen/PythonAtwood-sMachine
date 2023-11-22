import pygame
import time
pygame.init()

screen = pygame.display.set_mode((650, 650))
pygame.display.set_caption("Atwood's Machine")
screen.fill((255,255,255))
pygame.draw.line(screen, (0, 0, 0), (200, 0), (200, 75))
pygame.draw.circle(screen, (200,0,0),(200,75), 30)
pygame.draw.line(screen, (0, 0, 0), (170, 340), (170, 75))
pygame.draw.line(screen, (0, 0, 0), (230, 340), (230, 75))
font = pygame.font.Font(None, 25)
titleA = font.render("Green Block (block A)", True, (0, 0, 0))
massA = font.render(f"Mass: ", True, (0, 0, 0))
velocityA = font.render(f"Velocity:", True, (0, 0, 0))
accelerationA = font.render(f"Acceleration: ", True, (0, 0, 0))
titleB = font.render("Blue Block (block B)", True, (0, 0, 0))
massB = font.render(f"Mass:", True, (0, 0, 0))
velocityB = font.render(f"Velocity:", True, (0, 0, 0))
accelerationB = font.render(f"Acceleration:", True, (0, 0, 0))
timer = font.render(f"Time: ", True, (0, 0, 0))
screen.blit(titleA, (400, 50))
screen.blit(massA, (400, 75))
screen.blit(velocityA, (400, 100))
screen.blit(accelerationA, (400, 125))
screen.blit(titleB, (400, 175))
screen.blit(massB, (400, 200))
screen.blit(velocityB, (400, 225))
screen.blit(accelerationB, (400, 250))
screen.blit(timer, (400, 300))
pygame.draw.rect(screen, (0, 100, 0), (150, 340, 40, 40))
pygame.draw.rect(screen, (0, 0, 100), (210, 340, 40, 40))
pygame.display.flip()
mA = int(input("Mass of block A: "))
mB = int(input("Mass of block B: "))
massA = font.render(f"Mass: {mA} Kg", True, (0, 0, 0))
massB = font.render(f"Mass: {mB} Kg", True, (0, 0, 0))
screen.blit(massA, (400, 75))
screen.blit(massB, (400, 200))
pygame.draw.rect(screen, (255, 255, 255), (150, 340, 40, 40))
pygame.draw.rect(screen, (255, 255, 255), (210, 340, 40, 40))
if mA > mB:
    widthA = 50
    widthB = 34
elif mB > mA:
    widthA = 34
    widthB = 50
else:
    widthA = 40
    widthB = 40
xA = 170 - widthA / 2
xB = 230 - widthB / 2
yA = 340
yB = 340

rectA = pygame.draw.rect(screen, (0, 100, 0), (xA, yA, widthA, widthA))
rectB = pygame.draw.rect(screen, (0, 0, 100), (xB, yB, widthB, widthB))
pygame.display.flip()
# physics
t = 0
g = 9.81
aA = 0
aB = 0
vA = 0
vB = 0
fnet = mA*g - mB*g
m = mA+mB
aA = fnet/m
aB = -fnet/m
pause = False


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                start_time = time.time()
                while True:
                    elapsed_time = time.time() - start_time
                    seconds = round(elapsed_time, 1)
                    t = f"{seconds:.1f}"
                    time.sleep(0.1)

                    yA = 0.5 * aA * float(t)
                    yB = 0.5 * aB * float(t)
                    vA = aA*float(t)
                    vB = aB*float(t)
                    distance = 340 + vA*float(t) + 0.5*aA*float(t)

                    if rectA.y <= 97 or rectB.y <= 97:
                        break
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                    pause = True
                                    time.sleep(4)
                        else:
                            break

                    rectA.move_ip(0, int(yA))
                    rectB.move_ip(0, int(yB))

                    screen.fill((255, 255, 255))
                    titleA = font.render("Green Block (block A)", True, (0, 0, 0))
                    massA = font.render(f"Mass: {mA} Kg", True, (0, 0, 0))
                    velocityA = font.render(f"Velocity: {round(vA, 2)} m/s", True, (0, 0, 0))
                    accelerationA = font.render(f"Acceleration: {round(aA, 2)} m/s/s", True, (0, 0, 0))
                    titleB = font.render("Blue Block (block B)", True, (0, 0, 0))
                    massB = font.render(f"Mass: {mB} Kg", True, (0, 0, 0))
                    velocityB = font.render(f"Velocity: {round(vB,2)} m/s", True, (0, 0, 0))
                    accelerationB = font.render(f"Acceleration: {round(aB,2)} m/s/s", True, (0, 0, 0))
                    timer = font.render(f"Time: {t} seconds", True, (0, 0, 0))
                    d = font.render(f"Distance: {round(distance, 2)} meters", True, (0,0,0))
                    screen.blit(titleA, (400, 50))
                    screen.blit(massA, (400, 75))
                    screen.blit(velocityA, (400, 100))
                    screen.blit(accelerationA, (400, 125))
                    screen.blit(titleB, (400, 175))
                    screen.blit(massB, (400, 200))
                    screen.blit(velocityB, (400, 225))
                    screen.blit(accelerationB, (400, 250))
                    screen.blit(timer, (400, 300))

                    pygame.draw.line(screen, (0, 0, 0), (200, 0), (200, 75))
                    pygame.draw.line(screen, (0, 0, 0), (rectA.x+(widthA/2), rectA.y), (170, 75))
                    pygame.draw.line(screen, (0, 0, 0), (rectB.x+(widthB/2), rectB.y), (230, 75))
                    pygame.draw.circle(screen, (200, 0, 0), (200, 75), 30)
                    pygame.draw.rect(screen, (0, 100, 0), rectA)
                    pygame.draw.rect(screen, (0, 0, 100), rectB)

                    pygame.display.flip()

pygame.quit()

