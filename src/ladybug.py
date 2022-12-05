import pygame

class Ladybug:
  '''
  general function description: Creates the ladybug button that is used to go back to the question screen from the four habit screens
	args: ladybug1, x, y, image, scale
  
  '''
  def __init__(ladybug1, x, y, image, scale):
     width= image.get_width()
     height= image.get_height()
     ladybug1.image = pygame.transform.scale(image, (int(width * scale ), int(height*scale)))
     ladybug1.rect= ladybug1.image.get_rect()
     ladybug1.rect.topleft = (x,y)
     ladybug1.clicked=False