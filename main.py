import pygame
import time
import random

pygame.init()

display_width = 1200
display_height = 800

car_width = 86
car_heigth = 205

black = (0,0,0)
white = (255,255,255)
red = (255,0,0,)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Gra wyscigi')
clock = pygame.time.Clock()

carImg = pygame.image.load('car1.png')

def things_dodged(count):
	font = pygame.font.SysFont(None, 25)
	text = font.render("Pykniete: "+str(count), True, black)
	gameDisplay.blit(text,(10,10))
	

def things( thingx, thingy, thingw, thingh, color):
	pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
	

def text_objects(text, font):
	textSurface = font.render(text, True, red)
	return textSurface, textSurface.get_rect()

def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf', 115)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((display_width / 2),(display_height /2))
	gameDisplay.blit(TextSurf, TextRect)
	pygame.display.update()
	time.sleep(3)
	game_loop()
	

def car(x,y):
	gameDisplay.blit(carImg,(x,y))
	
def crash():
	message_display('You Crashed, Idiot !')



def game_loop():

	x = (display_width * 0.45)
	y = (display_height * 0.70)
	x_change = 0
	y_change = 0
	
	thing_startx = random.randrange(0, display_width)
	thing_starty = -600
	thing_speed = 7
	thing_width = 100
	thing_height = 100
	
	dodged = 0
	

	gameExit = False

	while not gameExit:
	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -5
				elif event.key == pygame.K_RIGHT:
					x_change = 5
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					y_change = -5
				elif event.key == pygame.K_DOWN:
					y_change = 5
		
		
		
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					x_change = 0
					y_change = 0
				
		x += x_change
		y += y_change
			
			
		gameDisplay.fill(white)
		things(thing_startx, thing_starty, thing_width, thing_height, black)
		thing_starty += thing_speed
		
		car(x,y)
	#	things_dodged(dodged)	
	
	
		if x > display_width - car_width or x < 0 or y > display_height - car_heigth or y< 0:
			crash()
			
		if thing_starty > display_height:
			thing_starty = 0 - thing_height
			thing_startx = random.randrange(0, display_width)
			dodged += 1
			thing_speed += 1
			thing_width += (dodged * 1.5)
			
		if y < thing_starty + thing_height:
			
			if x > thing_startx and x < thing_startx+thing_width or x+car_width > thing_startx and x+car_width < thing_startx+thing_width:
				crash()
			
	
	
		pygame.display.update()
		clock.tick(60)

game_loop()	
pygame.quit()
quit()

		


