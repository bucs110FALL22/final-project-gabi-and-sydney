import pygame

class Resource:
  '''
  general function description: Creates the button for the extra resources links
	args: flower8, x, y, image, scale

  
  '''
  def __init__(flower8, x, y, image, scale):
     width= image.get_width()
     height= image.get_height()
     flower8.image = pygame.transform.scale(image, (int(width * scale ), int(height*scale)))
     flower8.rect= flower8.image.get_rect()
     flower8.rect.topleft = (x,y)
     flower8.clicked=False
      
  







