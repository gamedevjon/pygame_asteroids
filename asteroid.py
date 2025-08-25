import pygame
from constants import *
from circleshape import CircleShape
import random


class Asteroid(CircleShape):        # points 1, 2, 3(small)
    def __init__(self, x, y, radius, points):
        self.__points = points
        super().__init__(x, y, radius)

    def get_points_for_radius(self, radius):
        if radius >= ASTEROID_MIN_RADIUS * 3: 
            return 1
        elif radius >= ASTEROID_MIN_RADIUS * 2:
            return 2
        else:                                  
            return 3
        
    def split(self):
        self.kill()
        #award points (raise event)
        pygame.event.post(pygame.event.Event(
            ASTEROID_DESTROYED,
            {"points": self.__points}
        ))
        random_angle = random.uniform(20, 50)
        new_velocity_1 = self.velocity.rotate(random_angle)
        new_velocity_2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        if new_radius >= ASTEROID_MIN_RADIUS:
            new_points = self.get_points_for_radius(new_radius)

            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius, new_points)
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius, new_points)
            
            asteroid_1.velocity = new_velocity_1 * 1.2
            asteroid_2.velocity = new_velocity_2 * 1.2

       
    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255, 255, 255),
            self.position,
            self.radius,
            2
        )

    def update(self, dt):
        self.position += self.velocity * dt
    

            




    