import pygame
import random

BACKGROUND_COLOR = (255, 255, 255)
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.randomize()

    def randomize(self):
        self.color = random.choice([(200, 0, 0),(0, 150, 0),(240, 240, 240),(200, 170, 60)])

        # random direction
        self.dx = random.randint(-3,3)
        self.dy = random.randint(-3,3)

        # avoiding 0 --> constantly moving
        while self.dx == 0 and self.dy == 0:
            self.dx = random.randint(-3,3)
            self.dy = random.randint(-3,3)

class Player:
    def __init__(self):
        self.radius = 10
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.color = (0,0,0)
        self.speed = 5


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Balls")

    clock = pygame.time.Clock()

    balls = []
    for i in range(1, 5):
        radius = random.randint(10, 40)
        # balls.append(Ball(100 * i, 100 * i, radius))
        
        min_x = radius
        max_x = SCREEN_WIDTH - radius
        min_y = radius
        max_y = SCREEN_HEIGHT - radius
        x = random.randint(min_x,max_x)
        y = random.randint(min_y,max_y)
        balls.append(Ball(x, y, radius))

    player = Player()

    done = False
    while not done:
        clock.tick(60)

        # Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True

            # randomize random ball
                elif event.key == pygame.K_r:
                    if balls:
                        random.choice(balls).randomize()
            # add a new ball at the same location the player is
                elif event.key == pygame.K_SPACE:
                    radius = random.randint(10,40)
                    x = player.x
                    y = player.y
                    balls.append(Ball(x,y,radius))

        # move, bounce
        for ball in balls:
            ball.x += ball.dx
            ball.y += ball.dy

            # left, right walls
            if ball.x <= ball.radius:
                ball.x = ball.radius
                ball.dx = -ball.dx
            elif ball.x >= SCREEN_WIDTH - ball.radius:
                ball.x = SCREEN_WIDTH - ball.radius
                ball.dx = -ball.dx

            # top, bottom walls
            if ball.y <= ball.radius:
                ball.y = ball.radius
                ball.dy = -ball.dy
            elif ball.y >= SCREEN_HEIGHT - ball.radius:
                ball.y = SCREEN_HEIGHT - ball.radius
                ball.dy = -ball.dy

        keys = pygame.key.get_pressed()
        dx = 0
        dy = 0

        # arrows 
        if keys[pygame.K_LEFT]:
            dx -= player.speed
        if keys[pygame.K_RIGHT]:
            dx += player.speed
        if keys[pygame.K_UP]:
            dy -= player.speed
        if keys[pygame.K_DOWN]:
            dy += player.speed

        player.x += dx
        player.y += dy

        player.x = max(player.radius, min(player.x, SCREEN_WIDTH - player.radius))
        player.y = max(player.radius, min(player.y, SCREEN_HEIGHT - player.radius))


        screen.fill(BACKGROUND_COLOR)

        for ball in balls:
            pygame.draw.circle(screen,ball.color,
                (ball.x, ball.y),ball.radius)
        
        pygame.draw.circle(screen, player.color,
            (player.x, player.y), player.radius)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
