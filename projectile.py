"""
A simple class to encapsulate moving projectiles
"""

from math import sin, cos, radians

class Projectile:
    """ General class for a cannonball and other projectiles """
    
    def __init__(self):
        self.x = 0
        self.y = 0
        self.vx = 0
        self.vy = 0
        
    def __init__(self, angle, velocity, height):
        self.x = 0
        self.y = height
        theta = radians(angle)
        self.vx = velocity * cos(theta)
        self.vy = velocity * sin(theta)
    
    def update(self, dt):
        """Update position and velocity of projectile every dt seconds """
        self.x = self.x + dt * self.vx
        vy1 = self.vy - 9.8 * dt
        self.y = self.y + dt * (self.vy + vy1) / 2.0
        self.vy = vy1
        return self.x, self.y