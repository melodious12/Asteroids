import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import *

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (updatable)
	player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
	asteroid_field = AsteroidField()
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
    
		for entity in updatable:
			entity.update(dt)

		screen.fill("black")

		for entity in drawable:
			entity.draw(screen)

		pygame.display.flip()

		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()
