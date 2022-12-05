import pygame

class Option:
  '''
  general function description: Creates one of the buttons for the four different habit screens
	args: flower6, x, y, image, scale

  
  '''
  def __init__(flower6, x, y, image, scale):
     width= image.get_width()
     height= image.get_height()
     flower6.image = pygame.transform.scale(image, (int(width * scale ), int(height*scale)))
     flower6.rect= flower6.image.get_rect()
     flower6.rect.topleft = (x,y)
     flower6.clicked=False
      







