import sys
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu de malade")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

clock = pygame.time.Clock()

# Dimensions hero
hero_width, hero_height = 75, 50
hero_speed = 5

# Dimensions obstacles
obstacle_width, obstacle_height = random.randint(30, 100), random.randint(30, 100)
obstacle_speed = 10

font = pygame.font.Font(None, 36)

score = 0
spawn_timer = 0
obstacles = []

def show_start_screen():
    """Affiche l'écran de début du jeu."""
    screen.fill(WHITE)
    title_text = font.render("Appuyez sur ESPACE pour ne pas commencer", True, BLACK)
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False

def show_game_over_screen(score):
    """Affiche l'écran de fin du jeu."""
    screen.fill(WHITE)
    over_text = font.render("Game Over", True, BLACK)
    score_text = font.render(f"Score: {score}", True, BLACK)
    restart_text = font.render("Appuyez sur ESPACE pour rejouer", True, BLACK)
    
    screen.blit(over_text, (WIDTH // 2 - over_text.get_width() // 2, HEIGHT // 3))
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))
    screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 1.5))
    
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False
                main()  # Redémarre le jeu

def main():
    global spawn_timer, score, obstacles

    # Réinitialisation des variables
    hero_x, hero_y = WIDTH // 4, HEIGHT // 2
    obstacles = []
    score = 0

    running = True
    while running:
        # Gestion des événements (fermer la fenêtre)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Déplacement du héros avec les flèches
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and hero_y > 0:  # Flèche haut
            hero_y -= hero_speed
        if keys[pygame.K_DOWN] and hero_y < HEIGHT - hero_height:  # Flèche bas
            hero_y += hero_speed
        if keys[pygame.K_LEFT] and hero_x > 0:  # Flèche gauche
            hero_x -= hero_speed
        if keys[pygame.K_RIGHT] and hero_x < WIDTH - hero_width:  # Flèche droite
            hero_x += hero_speed

        # Générer obstacle
        spawn_timer += 1
        if spawn_timer > 60:
            spawn_timer = 0
            obstacle_width, obstacle_height = random.randint(30, 100), random.randint(30, 100)
            obstacle_x = WIDTH
            obstacle_y = random.randint(0, HEIGHT - obstacle_height)
            obstacles.append(pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height))

        # Déplacer 
        for obstacle in obstacles:
            obstacle.x -= obstacle_speed

        # Supprimer 
        obstacles = [obstacle for obstacle in obstacles if obstacle.x > -obstacle_width]

        # Vérifier collision 
        hero_rect = pygame.Rect(hero_x, hero_y, hero_width, hero_height)
        for obstacle in obstacles:
            if hero_rect.colliderect(obstacle): 
                running = False

        score += 1

        screen.fill(WHITE)  # Remplir l'écran avec du blanc
        pygame.draw.rect(screen, BLACK, hero_rect)  # Dessiner le héros
        for obstacle in obstacles:
            pygame.draw.rect(screen, RED, obstacle)  # Dessiner les obstacles

        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

        clock.tick(30)
    show_game_over_screen(score)

if __name__ == "__main__":
    show_start_screen()
    main()
