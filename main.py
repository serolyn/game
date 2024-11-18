import pygame
import sys
import random


pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu Auto-runner")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

hero_width, hero_height = 50, 50
hero_x, hero_y = 100, HEIGHT // 2
hero_speed = 5


obstacles = []
obstacle_width, obstacle_height = 50, 50
obstacle_speed = 5
spawn_timer = 0


clock = pygame.time.Clock()


score = 0
font = pygame.font.Font(None, 36)


def main():
    global hero_x, hero_y, spawn_timer, score

    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

     =
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and hero_y > 0:  # Flèche haut
            hero_y -= hero_speed
        if keys[pygame.K_DOWN] and hero_y < HEIGHT - hero_height:  # Flèche bas
            hero_y += hero_speed
        if keys[pygame.K_LEFT] and hero_x > 0:  # Flèche gauche
            hero_x -= hero_speed
        if keys[pygame.K_RIGHT] and hero_x < WIDTH - hero_width:  # Flèche droite
            hero_x += hero_speed

        =
        spawn_timer += 1
        if spawn_timer > 60:  # Crée un obstacle toutes les secondes
            spawn_timer = 0
            obstacle_x = WIDTH
            obstacle_y = random.randint(0, HEIGHT - obstacle_height)
            obstacles.append(pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height))

        =
        for obstacle in obstacles:
            obstacle.x -= obstacle_speed

      =
        obstacles = [obstacle for obstacle in obstacles if obstacle.x > -obstacle_width]

     =
        hero_rect = pygame.Rect(hero_x, hero_y, hero_width, hero_height)
        for obstacle in obstacles:
            if hero_rect.colliderect(obstacle):
                print("Collision ! Game Over.")
                running = False

        =
        score += 1

       =
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, hero_rect)  # Héros
        for obstacle in obstacles:
            pygame.draw.rect(screen, RED, obstacle)  # Obstacles

       
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        
        pygame.display.flip()
        clock.tick(30)

    
    pygame.quit()
    sys.exit()



if __name__ == "__main__":
    main()

