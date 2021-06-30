import pygame
import random
import time
pygame.init()


# screen settings
WIDTH=600
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
clock=pygame.time.Clock()
#SCORE
score=0

def scoreMessage():
	myScoreFont=pygame.font.Font("freesansbold.ttf",24)
	textSurface=myScoreFont.render(f"Score : {score}",True,(0,255,255))
	textRect=textSurface.get_rect()
	screen.blit(textSurface,(0,0))


def message():
	myFont=pygame.font.Font("freesansbold.ttf",116)
	textSurface=myFont.render("You Died",True, (255,255,0))
	textRect=textSurface.get_rect()
	textRect.center=((WIDTH/2),(HEIGHT/2))

	screen.blit(textSurface,textRect)
	pygame.display.update()
	time.sleep(2)


#car
carImg=pygame.image.load('car1.png')
carX=WIDTH//2-carImg.get_width()//2
carY=HEIGHT*0.8
carX_change=0
carY_change=0
def car(x,y):
	screen.blit(carImg,(x,y))


#enemy
enemyImg=pygame.image.load('enemy.png')
enemyX=random.randint(0,WIDTH-enemyImg.get_width())
enemyY=random.randint(0,HEIGHT-carImg.get_height()-enemyImg.get_height())
def enemy():
	screen.blit(enemyImg,(enemyX,enemyY))
def enemyPos():
	global enemyX,enemyY
	enemyX=random.randint(0,WIDTH-enemyImg.get_width())
	enemyY=random.randint(0,HEIGHT-carImg.get_height()-enemyImg.get_height())	
distanceTriggerEnemyX=carImg.get_width()//2+enemyImg.get_width()//2	
distanceTriggerEnemyY=carImg.get_height()//2+enemyImg.get_height()//2



#killer
killerImg=pygame.image.load('killer.png')
killerX=random.randint(0,WIDTH-killerImg.get_width())
killerY=random.randint(0,HEIGHT*0.7)
killerX_change=0.9
killerY_change=0.9
def killer(x,y):
	screen.blit(killerImg,(x,y))
distanceTriggerKillerX=carImg.get_width()//2+killerImg.get_width()//2
distanceTriggerKillerY=carImg.get_height()//2+killerImg.get_height()//2


#gameloop
running=True
while running:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			running=False
			pygame.quit()
			quit()

		#CAR X_CHANGE ON KEYSTROKES
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_LEFT:
				carX_change=-0.9
			if event.key==pygame.K_RIGHT:
				carX_change=0.9
			if event.key==pygame.K_UP:
				carY_change=-0.9
			if event.key==pygame.K_DOWN:
				carY_change=0.9
			if event.key==pygame.K_SPACE:
				killerX=random.randint(0,WIDTH-killerImg.get_width())
				killerY=random.randint(0,HEIGHT*0.7)
				
			if event.key==pygame.K_c:
				pass
		if event.type==pygame.KEYUP:
			if event.key==pygame.K_LEFT or \
			event.key==pygame.K_RIGHT or\
			event.key==pygame.K_UP or\
			event.key==pygame.K_DOWN:
				carX_change=0
				carY_change=0


	

	#screen background
	screen.fill((0,0,0))


	# car MOVEMENT
	carX+=carX_change
	carY+=carY_change
	if carX<0 or carX>WIDTH-carImg.get_width():
		carX_change=0
	if carY<0 or carY>HEIGHT-carImg.get_height():
		carY_change=0
	car(carX,carY)
	
	

	#collision detection with enemy
	carMidX=int(carX+carImg.get_width()//2)
	enemyMidX=int(enemyX+enemyImg.get_width()//2)
	carMidY=int(carY+carImg.get_height()//2)
	enemyMidY=int(enemyY+enemyImg.get_height()//2)
	if abs(carMidX-enemyMidX)<=distanceTriggerEnemyX and abs(carMidY-enemyMidY)<=distanceTriggerEnemyY:
		enemyPos()
		score+=1
		print(f"score : {score}")
	
	#collision detection with killer
	killerMidX=int(killerX+killerImg.get_width()//2)
	killerMidY=int(killerY+killerImg.get_height()//2)
	if abs(carMidX-killerMidX)<=distanceTriggerKillerX and abs(carMidY-killerMidY)<=distanceTriggerKillerY:
		print("you died")
		message()

		#car reset
		carX=WIDTH//2-carImg.get_width()//2
		carY=HEIGHT*0.8

		#enemy reset
		enemyPos()

		#killer reset
		killerX=random.randint(0,WIDTH-killerImg.get_width())
		killerY=random.randint(0,HEIGHT*0.7)

		#score reset
		score=0


	#enemy on screen
	enemy()

	#killer
	if killerX<=0:
		killerX_change=0.9
	if killerX>= WIDTH-killerImg.get_width():
		killerX_change=-0.9
	if killerY<= 0:
		killerY_change=0.9
	if killerY>=WIDTH-killerImg.get_height():
		killerY_change=-0.9
	killerX+=killerX_change
	killerY+=killerY_change
	killer(killerX,killerY)




	#score display
	scoreMessage()
	clock.tick(300)
	pygame.display.update()
#pygame quit	
pygame.quit()
quit()
