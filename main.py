import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def update_score(score):
    font = pygame.font.SysFont(None, 48) 
    score_text = font.render(f"Score: {score}", True, (255, 255, 255)) 
    rect = score_text.get_rect(center=(SCREEN_WIDTH /2, SCREEN_HEIGHT/6))
    return score_text, rect

def main():
    print("Starting Asteroids!")
    print("Screen width: " + str(SCREEN_WIDTH))
    print("Screen height: " + str(SCREEN_HEIGHT))

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    #updatable group
    updatable = pygame.sprite.Group()
    #drawable group
    drawable = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)

    #instantiate player
    player_x = SCREEN_WIDTH / 2
    player_y = SCREEN_HEIGHT / 2
    player = Player(player_x, player_y)

    #astroid group
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    #init the asteroid field
    asteroid_field = AsteroidField()

    #shot group
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    score = 0
    pygame.font.init()
    
    score_text, score_text_rect = update_score(0)
                             
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == ASTEROID_DESTROYED:
                score += event.points
                score_text, score_text_rect = update_score(score)

        updatable.update(dt)   
        
        for ast in asteroids:
            hit_player = ast.check_collisions(player)
            if hit_player == True:
                raise SystemExit()
            for bullet in shots:
                bullet_check = bullet.check_collisions(ast)
                if bullet_check == True:
                    ast.split()
                    bullet.kill()

        screen.fill((0, 0, 0))
        #draw score
        screen.blit(score_text, score_text_rect)
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
