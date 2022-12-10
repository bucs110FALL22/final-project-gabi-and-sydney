import pygame

class Yes:
  '''
  general function description: Creates the yes button which indicates that the user completed their habit for that given day.
	args: yes1, x, y, image, scale

  '''
  def __init__(yes1, x, y, image, scale):
     width= image.get_width()
     height= image.get_height()
     yes1.image = pygame.transform.scale(image, (int(width * scale ), int(height*scale)))
     yes1.rect= yes1.image.get_rect()
     yes1.rect.topleft = (x,y)
     yes1.clicked=False
      
      
  







