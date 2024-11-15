import pygame
from constants import *
from player import *

def main():
	pygame.init
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
	while True:
		screen.fill((0,0,0))
		pygame.display.flip()
		dt = clock.tick(60) / 1000
		player.draw(screen)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

if __name__ == "__main__":
	main()
