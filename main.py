import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
 
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (shots, updatable, drawable)

	player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
	asteroid_field = AsteroidField()

	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
    
		for entity in updatable:
			entity.update(dt)

		for asteroid in asteroids:
			for shot in shots:
				if shot.collides_with(asteroid):
					shot.kill()
					asteroid.split()

			if asteroid.collides_with(player):
				print("Game over!")
				sys.exit()

		screen.fill("black")

		for entity in drawable:
			entity.draw(screen)

		pygame.display.flip()

		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()
