import pygame
#from Buttons import Button
#import Button
#from Models import Buttons


def main():
  '''
  Creates and initalize the pygame screen. Set the screen width height, and color
  '''
  pygame.init()
  screen_width = 650
  screen_height = 700
  screen = pygame.display.set_mode([screen_width, screen_height])
  screen_color = (210, 231, 214)
  screen.fill(screen_color)
  pygame.display.flip()
  '''
  Makes the text to display on the pygame screen using the title     "Grow Your Garden", text size 56 and centers it
  '''
  text_color = (1,50,32)
  pygame.display.set_caption("Grow Your Garden")
  font = pygame.font.Font(None, 56)
  text = font.render("Grow Your Garden",True,text_color)
  text_rect = text.get_rect(center=(screen_width/2, screen_height/7))
  screen.blit(text,text_rect)
  pygame.display.flip()
  '''
  Inserts image of the flowers to be displayed onto the screen       using the coordinates
  '''
  pygame.display.set_caption("Grow Your Garden")
  flower = pygame.image.load('Flower Icon.png')
  pygame.display.set_icon(flower)
  flower_1 = pygame.image.load('Flower 4.png')
  flower_1x= 180
  flower_1y= 260

  flower_2 = pygame.image.load('Flower 5.png')
  flower_2x=-20
  flower_2y=260

  flower_3 = pygame.image.load('Flower 6.png')
  flower_3x=420
  flower_3y= 260

  

  screen.blit(flower_1, (flower_1x, flower_1y))

  screen.blit(flower_2, (flower_2x, flower_2y))

  screen.blit(flower_3, (flower_3x, flower_3y))

  pygame.display.flip()
  #bee_image = pygame.image.load('Bee.png')
 

  #bee_button = Buttons.Button (100, 200, bee_image,0.5)

  #run = True
  #while run:
  
    #screen.fill((210, 231, 214))
    #if bee_button.draw(screen) == True:
        #print("Bee")
    #for event in pygame.event.get():
        #if event.type == pygame.QUIT:
            #run = False
    #pygame.display.update()
  
  #pygame.quit()
  #pygame.display.update()
  #pygame.time.wait(2000)
  
 # button = Buttons (image, (10,10), push_button_screen)
  screen.exitonclick()

'''
Runs the main.py also called the controller
'''
main() 


  