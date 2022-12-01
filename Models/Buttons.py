import pygame
pygame.init()
pygame.init()
screen_width = 700
screen_height = 700
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption('Growing Your Garden')
bee_image = pygame.image.load('Bee.png')

class Button():
    def __init__ (self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale),(int(height*scale))))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
    def draw(self,surface):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True 
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        surface.blit(self.image,(self.rect.x, self.rect.y))
        return action

bee_button = Button(100, 200, bee_image, 0.5)

run = True
while run:
  
  screen.fill((210, 231, 214))
  if bee_button.draw(screen) == True:
    print("Bee")
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        run = False
    pygame.display.update()
  
pygame.quit()

bee_button = Button(100, 200, bee_image, 0.5)



      

