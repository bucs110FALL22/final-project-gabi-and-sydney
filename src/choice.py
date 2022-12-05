import pygame

class Choice:
  '''
  general function description: Creates the button for one of the 4 different habits.
	args: flower5, x, y, image, scale

  '''
  def __init__(flower5, x, y, image, scale):
     width= image.get_width()
     height= image.get_height()
     flower5.image = pygame.transform.scale(image, (int(width * scale ), int(height*scale)))
     flower5.rect= flower5.image.get_rect()
     flower5.rect.topleft = (x,y)
     flower5.clicked=False







