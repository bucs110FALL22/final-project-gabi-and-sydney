import pygame

class Butterfly:
  '''
  general function description: Creates the Butterfly button that is used to go from the welcome screen to the question screen.
	args: butterfly1, x, y, image, and scale
  '''
  def __init__(butterfly1, x, y, image, scale):
     width= image.get_width()
     height= image.get_height()
     butterfly1.image = pygame.transform.scale(image, (int(width * scale ), int(height*scale)))
     butterfly1.rect= butterfly1.image.get_rect()
     butterfly1.rect.topleft = (x,y)
     butterfly1.clicked=False
      

