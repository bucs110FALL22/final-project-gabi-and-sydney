import pygame
import button
import habit
import choice
import option
import choose
import ladybug
import random
import resource
import yes
import no
import butterfly
import json
import sys



def main():
  pygame.init()
  screen_width= 650
  screen_height= 700
  screen = pygame.display.set_mode([screen_width, screen_height])
  screen_color = (210, 231, 214)
  screen.fill(screen_color)
  pygame.display.flip()
  text_color = (1,50,32)
  pygame.display.set_caption("Grow Your Garden")
  font = pygame.font.Font(None, 80)
  text = font.render("Grow Your Garden",True,text_color)
  text_rect = text.get_rect(center=(screen_width/2, screen_height/7))
  screen.blit(text,text_rect)
  pygame.display.flip()

  pygame.display.set_caption("Grow Your Garden")
  flower = pygame.image.load('assets/Flower Icon.png')
  pygame.display.set_icon(flower)

  flower_1 = pygame.image.load('assets/Flower 4.png')
  flower_1x= 200
  flower_1y= 280

  flower_2 = pygame.image.load('assets/Flower 5.png')
  flower_2x=-20
  flower_2y=280

  flower_3 = pygame.image.load('assets/Flower 6.png')
  flower_3x=420
  flower_3y= 280

  screen.blit(flower_1, (flower_1x, flower_1y))

  screen.blit(flower_2, (flower_2x, flower_2y))

  screen.blit(flower_3, (flower_3x, flower_3y))
  pygame.display.update()
  pygame.time.wait(2000)

  start=pygame.image.load('assets/Bee.png').convert_alpha()
  bee = button.Button(260,150 , start, 0.8)



  running= True
  while running:
        for event in pygame.event.get(): 
           
          pos= pygame.mouse.get_pos()
        if bee.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1 and bee.clicked == False:
              bee.clicked= True
              welcome()
            
        if pygame.mouse.get_pressed()[0] ==0:
              bee.clicked= False
        screen.blit(bee.image, (bee.rect.x, bee.rect.y))   
       
  
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
              running = False
        pygame.display.update()
        pygame.display.flip()

  pygame.quit() 

def welcome():
  screen_width= 650
  screen_height= 700
  screen_color= (210, 231, 214)
  screen = pygame.display.set_mode([screen_width, screen_height])

  rect_color= (255,255, 255)
  
  name = str(input("Name:  "))
  goal = str(input("Goal: "))
  text_color = (1,50,32)
  font_1= pygame.font.Font(None, 25)
  text_0= font_1.render(name, True, text_color)
  answer_1= font_1.render(goal, True, text_color)
  
  running= True
  while running:
      screen.fill(screen_color)
      text_color = (1,50,32)
      font_1= pygame.font.Font(None, 25)
      pygame.draw.rect(screen, rect_color, pygame.Rect(0, 130, 650, 350))
      font = pygame.font.Font(None, 80)
      text = font.render("Welcome!",True,text_color)
      screen.blit(text, (180, 0))

      text_2= font_1.render("Please input your name and the habit you are thinking of pursuing: ", True, text_color)
      screen.blit(text_2, (60, 95))

      font_1= pygame.font.Font(None, 25)
      text_2= font_1.render("Name: ", True, text_color)
      screen.blit(text_2, (0, 200))

      font_1= pygame.font.Font(None, 25)
      text_2= font_1.render("Goal: ", True, text_color)
      screen.blit(text_2, (0, 255))

      screen.blit(text_0, (60,200))
      screen.blit(answer_1, (60, 255))

      butterfly_1=pygame.image.load('assets/butterfly.png').convert_alpha()
      butterfly1= butterfly.Butterfly(580,0 , butterfly_1, 0.8)

    
      write1 = pygame.image.load('assets/write.png')
      write_1x=0
      write_1y= 130

      screen.blit(write1, (write_1x, write_1y))




      font_3 = pygame.font.Font(None,30)
      text_3 = font_3.render("Next",True, text_color)
      screen.blit(text_3,(582,55))

     

      for event in pygame.event.get(): 
        pos= pygame.mouse.get_pos()
      if butterfly1.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1 and butterfly1.clicked == False:
              butterfly1.clicked= True
              question()
              
      if pygame.mouse.get_pressed()[0] ==0:
              butterfly1.clicked= False

     
    
      screen.blit(butterfly1.image, (butterfly1.rect.x, butterfly1.rect.y)) 
  
            
      pygame.display.flip()
          
      for event in pygame.event.get():
          if event.type== pygame.QUIT:
             pygame.quit()
      pygame.display.update()
      

def question():
    screen_width= 650
    screen_height= 700
    screen = pygame.display.set_mode([screen_width, screen_height])
    running= True
    while running:
        screen_color= (210, 231, 214)
        screen.fill(screen_color)
        text_color = (1,50,32)
        font = pygame.font.Font(None, 80)
        font_2= pygame.font.Font(None, 41)
        text = font.render("Welcome!",True,text_color)
        text_2= font_2.render("Choose time needed to make the habit flourish", True, text_color)
        font_3 = pygame.font.Font(None,30)
        text_3 = font_3.render("1 month",True, text_color)
        font_4 = pygame.font.Font(None, 30)
        text_4 = font_4.render("3 months", True, text_color)
        font_5 = pygame.font.Font(None,30)
        text_5 = font_5.render("6 months", True, text_color)
        font_6 = pygame.font.Font(None,30)
        text_6 = font_6.render ("12 months",True, text_color)
        font_7 = pygame.font.Font(None,30)
        text_7 = font_7.render ("Extra Resources",True, text_color)
        
      
        
     
      
        screen.blit(text,(190,100))
        screen.blit(text_2, (1, 200))
        screen.blit(text_3,(40,350))
        screen.blit(text_4,(195,350))
        screen.blit(text_5,(350,350))
        screen.blit(text_6,(505,350))
        screen.blit(text_3,(40,350))
        screen.blit(text_4,(195,350))
        screen.blit(text_5,(350,350))
        screen.blit(text_6,(505,350))
        screen.blit(text_7, (185, 435))
        
      
      
        flower_4=pygame.image.load('assets/flowbut1.png').convert_alpha()
        flower4=habit.Habit(50,270 , flower_4, 0.8)

        flower_5=pygame.image.load('assets/lotus .png').convert_alpha()
        flower5=choice.Choice(205,270 , flower_5, 0.8)

        flower_6=pygame.image.load('assets/flowerbut_3.png').convert_alpha()
        flower6=option.Option(360,270 , flower_6, 0.8)

        flower_7=pygame.image.load('assets/rose (1).png').convert_alpha()
        flower7=choose.Choose(515,270 , flower_7, 0.8)

        flower_8=pygame.image.load('assets/flower.resources.png').convert_alpha()
        flower8=resource.Resource(400,400 , flower_8, 0.8)

        action= True
        while action:
          for event in pygame.event.get(): 
           
            pos= pygame.mouse.get_pos()
          if flower4.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1 and flower4.clicked == False:
              flower4.clicked= True
              habit1()
          if pygame.mouse.get_pressed()[0] ==0:
              flower4.clicked= False
            
          elif flower5.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1 and flower5.clicked == False:
              flower5.clicked= True
              habit3()
          if pygame.mouse.get_pressed()[0] ==0:
              flower5.clicked= False

          elif flower6.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1 and flower6.clicked == False:
              flower6.clicked= True
              habit6()
          if pygame.mouse.get_pressed()[0] ==0:
              flower6.clicked= False

          elif flower7.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1 and flower7.clicked == False:
              flower7.clicked= True
              habit12()
          if pygame.mouse.get_pressed()[0] ==0:
              flower7.clicked= False

          elif flower8.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1 and flower8.clicked == False:
              flower8.clicked= True
              links()
          if pygame.mouse.get_pressed()[0] ==0:
              flower8.clicked= False
            
          screen.blit(flower4.image, (flower4.rect.x, flower4.rect.y)) 
          screen.blit(flower5.image, (flower5.rect.x, flower5.rect.y)) 
          screen.blit(flower6.image, (flower6.rect.x, flower6.rect.y)) 
          screen.blit(flower7.image, (flower7.rect.x, flower7.rect.y)) 
          screen.blit(flower8.image, (flower8.rect.x, flower8.rect.y)) 
  
            
          pygame.display.flip()
          
          for event in pygame.event.get():
            if event.type== pygame.QUIT:
              pygame.quit()
          pygame.display.update()
      

      
def habit1():
  screen_width= 650
  screen_height= 700
  screen_color_3 = (143,188,143)
  screen = pygame.display.set_mode([screen_width, screen_height])

  clock =pygame.time.Clock()
  rect_color= (255,255, 255)
  line_color= (0,0,0)

  green= (0,255, 0)
  
  movement=True
  quotes_list= ['Do one thing every day that scares you ― Eleanor Roosevelt', 'Hold the vision, trust the process - Unknown', 'You are doing amazing, sweetie - Kris Jenner','I am alive, motivated and ready to slay the day #MONSLAY - Unknown', 'The hard days are what make you stronger - Aly Raisman', 'Habits form based on frequency, not time - James Clear', 'If you can dream it, you can do it- Walt Disney', 'The future belongs to those who prepare for it today - Malcolm X', 'Nothing will work unless you do - Maya Angelou', 'Successful people are simply those with sucessful habits - Brian Tracy']
  num = random.randint(0,9)
  quote = quotes_list[num]
  print(quote)
  
  data = {'Yes':0 , 
         'No':0,
}
  
  
  try: 
      with open('clicker_score.txt') as score_file:
        data= json.load(score_file)
  except:
    print("No file created")
    
  progress=0
  while movement:
    screen.fill(screen_color_3)

    pygame.draw.rect(screen, rect_color, pygame.Rect(0, 100, 650, 300))
    pygame.draw.line(screen,line_color, (0, 120), (650, 120))
    pygame.draw.line(screen,line_color, (0, 265), (650, 265))
    pygame.draw.line(screen,line_color, (285, 120), (385, 265))


    font_1 = pygame.font.SysFont("bar", 25)
    
    
    text_color = (1,50,32)
    font_7 = pygame.font.Font(None, 55)
    text_7 = font_7.render("One Month",True,text_color)
    screen.blit(text_7, (0,0))
    font_8 = pygame.font.Font(None,30)
    text_8 = font_8.render("Back",True, text_color)
    screen.blit(text_8,(582,60))
    font_6 = pygame.font.Font(None, 25)
    text_6 = font_6.render(quote,True,text_color)
    screen.blit(text_6, (50, 450))

    font_9 = pygame.font.Font(None, 30)
    text_9 = font_9.render("Click Yes or No Button regarding completion of habit for today: ",True,text_color)
    screen.blit(text_9, (0,100))

    font_12 = pygame.font.Font(None, 30)
    text_12 = font_12.render("Progress: ",True,text_color)
    screen.blit(text_12, (0,270))

    yes_button=pygame.image.load('assets/yes(1).png').convert_alpha()
    yes1=yes.Yes(95,135 , yes_button, 0.8)

    font_10 = pygame.font.Font(None, 35)
    text_10 = font_10.render(f'Yes: {data["Yes"]}',True,text_color)
    screen.blit(text_10, (100,240))
    

    no_button=pygame.image.load('assets/no(1).png').convert_alpha()
    no1=no.No(455,135 , no_button, 0.8)

    font_11 = pygame.font.Font(None, 35)
    text_11 = font_11.render(f'No: {data["No"]}',True,text_color)
    screen.blit(text_11, (482,240))

    font_13 = pygame.font.Font(None, 35)
    text_13 = font_13.render("Keep up the goodwork!",True,text_color)

    font_14 = pygame.font.Font(None, 35)
    text_14 = font_14.render("Remember your endgoal! You can do it!",True,text_color)

    
    draw = pygame.image.load('assets/ladybug.png').convert_alpha()
    ladybug1 = ladybug.Ladybug(580, 0, draw, 0.8)
    
  
    for event in pygame.event.get():
            if event.type ==pygame.QUIT:
              with open('clicker_score.txt', 'w') as score_file:
                json.dump(data, score_file)
              pygame.quit()
              sys.exit
    pos= pygame.mouse.get_pos()
    if ladybug1.rect.collidepoint(pos):
           if pygame.mouse.get_pressed()[0]==1 and ladybug1.clicked == False:
              ladybug1.clicked= True
              question()
    if pygame.mouse.get_pressed()[0] ==0:
              ladybug1.clicked= False

    elif yes1.rect.collidepoint(pos):
           if pygame.mouse.get_pressed()[0]==1 and yes1.clicked == False:
              yes1.clicked= True
              data["Yes"] +=1
              yes1=yes.Yes(95,135 , yes_button, 0.8)
              text_10 = font_10.render(f'Yes: {data["Yes"]}',True,text_color)
              screen.blit(text_13, (0,50))
              
              if progress < 31:
                 progress +=1
                
              elif progress==31:  
                pygame.draw.rect(screen, green, (0,300, progress, 100))
                font_15 = pygame.font.Font(None, 35)
                text_15 = font_15.render("Congrats you completed your goal!",True,text_color)
                screen.blit(text_15, (200,315))
              
              text= font_1.render("Loading: "  + str(int(progress)) + "%", True, green)
              
              screen.blit(text, (453, 273))
             
    if pygame.mouse.get_pressed()[0] ==0:
              yes1.clicked= False

    elif no1.rect.collidepoint(pos):
           if pygame.mouse.get_pressed()[0]==1 and no1.clicked == False:
              no1.clicked= True
              data["No"] +=1
              no1=no.No(455,135 , no_button, 0.8)
              text_11 = font_11.render(f'No: {data["No"]}',True,text_color)
              
              
              screen.blit(text_14, (0,50))
              text= font_1.render("Loading: "  + str(int(progress)) + "%", True, green)
             
              pygame.draw.rect(screen, green, (0,300, progress, 100))
              screen.blit(text, (453, 273))
              
              
             
    if pygame.mouse.get_pressed()[0] ==0:
              no1.clicked= False
    pygame.display.flip()
    pygame.draw.rect(screen, green, (0,300, progress, 100))
    screen.blit(ladybug1.image, (ladybug1.rect.x, ladybug1.rect.y))
    screen.blit(yes1.image, (yes1.rect.x, yes1.rect.y))
    screen.blit(no1.image, (no1.rect.x, no1.rect.y))

    
    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)
    
    
    
def habit3():
  screen_width= 650
  screen_height= 700
  screen_color_4 = (230,230,250)
  screen = pygame.display.set_mode([screen_width, screen_height])
  clock =pygame.time.Clock()

  green= (0,255, 0)
  
  rect_color= (255,255, 255)
  line_color= (0,0,0)
  
  action=True
  quotes_list= ['Do one thing every day that scares you ― Eleanor Roosevelt', 'Hold the vision, trust the process - Unknown', 'You are doing amazing, sweetie - Kris Jenner','I am alive, motivated and ready to slay the day #MONSLAY - Unknown', 'The hard days are what make you stronger - Aly Raisman', 'Habits form based on frequency, not time - James Clear', 'If you can dream it, you can do it- Walt Disney', 'The future belongs to those who prepare for it today - Malcolm X', 'Nothing will work unless you do - Maya Angelou', 'Successful people are simply those with sucessful habits - Brian Tracy']
  num = random.randint(0,9)
  quote = quotes_list[num]
  print(quote)

  data = {'Yes':0 , 
         'No':0,
}

  
  try: 
      with open('clicker_score3.txt') as score_file3:
        data= json.load(score_file3)
  except:
    print("No file created")
  
  progress=0
  while action:
    screen.fill(screen_color_4)

    pygame.draw.rect(screen, rect_color, pygame.Rect(0, 100, 650, 300))
    pygame.draw.line(screen,line_color, (0, 120), (650, 120))
    pygame.draw.line(screen,line_color, (0, 265), (650, 265))
    pygame.draw.line(screen,line_color, (285, 120), (385, 265))

    font_1 = pygame.font.SysFont("bar", 25)
    
    text_color = (1,50,32)
    font_7 = pygame.font.Font(None, 55)
    text_7 = font_7.render("Three Months",True,text_color)
    screen.blit(text_7,(0,0))

    font_6 = pygame.font.Font(None, 25)
    text_6 = font_6.render(quote,True,text_color)
    screen.blit(text_6, (50, 450))

    font_8 = pygame.font.Font(None,30)
    text_8 = font_8.render("Back",True, text_color)
    screen.blit(text_8,(582,60))

    font_9 = pygame.font.Font(None, 30)
    text_9 = font_9.render("Click Yes or No Button regarding completion of habit for today: ",True,text_color)
    screen.blit(text_9, (0,100))

    font_12 = pygame.font.Font(None, 30)
    text_12 = font_12.render("Progress: ",True,text_color)
    screen.blit(text_12, (0,270))

    yes_button=pygame.image.load('assets/yes(1).png').convert_alpha()
    yes1=yes.Yes(95,135 , yes_button, 0.8)

    font_10 = pygame.font.Font(None, 35)
    text_10 = font_10.render(f'Yes: {data["Yes"]}',True,text_color)
    screen.blit(text_10, (100,240))
    

    no_button=pygame.image.load('assets/no(1).png').convert_alpha()
    no1=no.No(455,135 , no_button, 0.8)

    font_11 = pygame.font.Font(None, 35)
    text_11 = font_11.render(f'No: {data["No"]}',True,text_color)
    screen.blit(text_11, (482,240))

    font_13 = pygame.font.Font(None, 35)
    text_13 = font_13.render("Keep up the goodwork!",True,text_color)
    

    font_14 = pygame.font.Font(None, 35)
    text_14 = font_14.render("Remember your endgoal! You can do it!",True,text_color)

    
    draw = pygame.image.load('assets/ladybug.png').convert_alpha()
    ladybug1 = ladybug.Ladybug(580, 0, draw, 0.8)
  
  
    for event in pygame.event.get():
          if event.type ==pygame.QUIT:
              with open('clicker_score3.txt', 'w') as score_file3:
                json.dump(data, score_file3)
              pygame.quit()
              sys.exit
  
    pos= pygame.mouse.get_pos()
    if ladybug1.rect.collidepoint(pos):
           if pygame.mouse.get_pressed()[0]==1 and ladybug1.clicked == False:
              ladybug1.clicked= True
              question()
    if pygame.mouse.get_pressed()[0] ==0:
              ladybug1.clicked= False

    elif yes1.rect.collidepoint(pos):
           if pygame.mouse.get_pressed()[0]==1 and yes1.clicked == False:
              yes1.clicked= True
              data["Yes"] +=1
              yes1=yes.Yes(95,135 , yes_button, 0.8)
              text_10 = font_10.render(f'Yes: {data["Yes"]}',True,text_color)
              screen.blit(text_13, (0,50))
              if progress < 90:
                  progress += 1
              elif progress ==90:
                font_15 = pygame.font.Font(None, 35)
                text_15 = font_15.render("Congrats you completed your goal!",True,text_color)
                screen.blit(text_15, (200,315))
              
              text= font_1.render("Loading: "  + str(int(progress)) + "%", True, green)
              
              pygame.draw.rect(screen, green, (0,300, progress, 100))
              screen.blit(text, (453, 273))
              
             
    if pygame.mouse.get_pressed()[0] ==0:
              yes1.clicked= False

    elif no1.rect.collidepoint(pos):
           if pygame.mouse.get_pressed()[0]==1 and no1.clicked == False:
              no1.clicked= True
              data["No"] +=1
              no1=no.No(455,135 , no_button, 0.8)
              text_11 = font_11.render(f'No: {data["No"]}',True,text_color)
              screen.blit(text_14, (0,50))
              text= font_1.render("Loading: "  + str(int(progress)) + "%", True, green)
             
              pygame.draw.rect(screen, green, (0,300, progress, 100))
              screen.blit(text, (453, 273))
              screen.blit(text_14, (0,50))
             
    if pygame.mouse.get_pressed()[0] ==0:
              no1.clicked= False
    screen.blit(ladybug1.image, (ladybug1.rect.x, ladybug1.rect.y))
    screen.blit(yes1.image, (yes1.rect.x, yes1.rect.y))
    screen.blit(no1.image, (no1.rect.x, no1.rect.y))

    pygame.display.flip()
    
  
    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)
    
    
  

def habit6():
  screen_width= 650
  screen_height= 700
  screen_color_5 = (135,206,235)
  screen = pygame.display.set_mode([screen_width, screen_height])

  clock =pygame.time.Clock()

  green= (0,255, 0)

  rect_color= (255,255, 255)
  line_color= (0,0,0)

  action=True
  quotes_list= ['Do one thing every day that scares you ― Eleanor Roosevelt', 'Hold the vision, trust the process - Unknown', 'You are doing amazing, sweetie - Kris Jenner','I am alive, motivated and ready to slay the day #MONSLAY - Unknown', 'The hard days are what make you stronger - Aly Raisman', 'Habits form based on frequency, not time - James Clear', 'If you can dream it, you can do it- Walt Disney', 'The future belongs to those who prepare for it today - Malcolm X', 'Nothing will work unless you do - Maya Angelou', 'Successful people are simply those with sucessful habits - Brian Tracy']
  num = random.randint(0,9)
  quote = quotes_list[num]
  print(quote)

  data = {'Yes':0 , 
         'No':0,
}

  
  try: 
      with open('clicker_score6.txt') as score_file6:
        data= json.load(score_file6)
  except:
    print("No file created")

  progress=0
  while action:
    screen.fill(screen_color_5)

    pygame.draw.rect(screen, rect_color, pygame.Rect(0, 100, 650, 300))
    pygame.draw.line(screen,line_color, (0, 120), (650, 120))
    pygame.draw.line(screen,line_color, (0, 265), (650, 265))
    pygame.draw.line(screen,line_color, (285, 120), (385, 265))
    
    font_1 = pygame.font.SysFont("bar", 25)
    
    
    text_color = (1,50,32)
    font_7 = pygame.font.Font(None, 55)
    text_7 = font_7.render("Six Months",True,text_color)
    screen.blit(text_7,(0,0))

    font_6 = pygame.font.Font(None, 25)
    text_6 = font_6.render(quote,True,text_color)
    screen.blit(text_6, (50, 450))

    font_8 = pygame.font.Font(None,30)
    text_8 = font_8.render("Back",True, text_color)
    screen.blit(text_8,(582,60))

    font_9 = pygame.font.Font(None, 30)
    text_9 = font_9.render("Click Yes or No Button regarding completion of habit for today: ",True,text_color)
    screen.blit(text_9, (0,100))

    font_12 = pygame.font.Font(None, 30)
    text_12 = font_12.render("Progress: ",True,text_color)
    screen.blit(text_12, (0,270))

    yes_button=pygame.image.load('assets/yes(1).png').convert_alpha()
    yes1=yes.Yes(95,135 , yes_button, 0.8)

    font_10 = pygame.font.Font(None, 35)
    text_10 = font_10.render(f'Yes: {data["Yes"]}',True,text_color)
    screen.blit(text_10, (100,240))
    

    no_button=pygame.image.load('assets/no(1).png').convert_alpha()
    no1=no.No(455,135 , no_button, 0.8)

    font_11 = pygame.font.Font(None, 35)
    text_11 = font_11.render(f'No: {data["No"]}',True,text_color)
    screen.blit(text_11, (482,240))

    font_13 = pygame.font.Font(None, 35)
    text_13 = font_13.render("Keep up the goodwork!",True,text_color)
    

    font_14 = pygame.font.Font(None, 35)
    text_14 = font_14.render("Remember your endgoal! You can do it!",True,text_color)
    
    
    draw = pygame.image.load('assets/ladybug.png').convert_alpha()
    ladybug1 = ladybug.Ladybug(580, 0, draw, 0.8)
  
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
              with open('clicker_score6.txt', 'w') as score_file6:
                json.dump(data, score_file6)
              pygame.quit()
              sys.exit
  
    pos= pygame.mouse.get_pos()
    if ladybug1.rect.collidepoint(pos):
           if pygame.mouse.get_pressed()[0]==1 and ladybug1.clicked == False:
              ladybug1.clicked= True
              question()
    if pygame.mouse.get_pressed()[0] ==0:
              ladybug1.clicked= False
    elif yes1.rect.collidepoint(pos):
           if pygame.mouse.get_pressed()[0]==1 and yes1.clicked == False:
              yes1.clicked= True
              data["Yes"] +=1
              yes1=yes.Yes(95,135 , yes_button, 0.8)
              text_10 = font_10.render(f'Yes: {data["Yes"]}',True,text_color)
              screen.blit(text_13, (0,50))

              if progress < 181:
                  progress += 1
              elif progress ==181:
                font_15 = pygame.font.Font(None, 30)
                text_15 = font_15.render("Congrats you completed your goal!",True,text_color)
                screen.blit(text_15, (200,315))
              
              text= font_1.render("Loading: "  + str(int(progress)) + "%", True, green)
              
              pygame.draw.rect(screen, green, (0,300, progress, 100))
              screen.blit(text, (453, 273))
            
             
    if pygame.mouse.get_pressed()[0] ==0:
              yes1.clicked= False

    elif no1.rect.collidepoint(pos):
           if pygame.mouse.get_pressed()[0]==1 and no1.clicked == False:
              no1.clicked= True
              data["No"] +=1
              no1=no.No(455,135 , no_button, 0.8)
              text_11 = font_11.render(f'No: {data["No"]}',True,text_color)
              text= font_1.render("Loading: "  + str(int(progress)) + "%", True, green)
             
              pygame.draw.rect(screen, green, (0,300, progress, 100))
              screen.blit(text, (453, 273))
              
              screen.blit(text_14, (0,50))
              
             
    if pygame.mouse.get_pressed()[0] ==0:
              no1.clicked= False

    pygame.display.flip()
    screen.blit(ladybug1.image, (ladybug1.rect.x, ladybug1.rect.y))
    screen.blit(yes1.image, (yes1.rect.x, yes1.rect.y))
    screen.blit(no1.image, (no1.rect.x, no1.rect.y))

    
    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)
    

def habit12():
  screen_width= 650
  screen_height= 700
  screen_color_6 = (216,191,216)
  screen = pygame.display.set_mode([screen_width, screen_height])

  clock =pygame.time.Clock()

  green= (0,255,0)

  rect_color= (255,255, 255)
  line_color= (0,0,0)
  
  action=True
  
  quotes_list= ['Do one thing every day that scares you ― Eleanor Roosevelt', 'Hold the vision, trust the process - Unknown', 'You are doing amazing, sweetie - Kris Jenner','I am alive, motivated and ready to slay the day #MONSLAY - Unknown', 'The hard days are what make you stronger - Aly Raisman', 'Habits form based on frequency, not time - James Clear', 'If you can dream it, you can do it- Walt Disney', 'The future belongs to those who prepare for it today - Malcolm X', 'Nothing will work unless you do - Maya Angelou', 'Successful people are simply those with sucessful habits - Brian Tracy']
  num = random.randint(0, 9)
  quote = quotes_list[num]
  print(quote)

  data = {'Yes':0 , 
         'No':0,
}

  try: 
      with open('clicker_score12.txt') as score_file12:
        data= json.load(score_file12)
  except:
    print("No file created")
  
  progress=0
  while action:
    screen.fill(screen_color_6)

    pygame.draw.rect(screen, rect_color, pygame.Rect(0, 100, 650, 300))
    pygame.draw.line(screen,line_color, (0, 120), (650, 120))
    pygame.draw.line(screen,line_color, (0, 265), (650, 265))
    pygame.draw.line(screen,line_color, (285, 120), (385, 265))

    font_1 = pygame.font.SysFont("bar", 25)
    
    
    text_color = (1,50,32)
    font_7 = pygame.font.Font(None, 55)
    text_7 = font_7.render("Twelve Months",True,text_color)
    screen.blit(text_7,(0,0))

    font_6 = pygame.font.Font(None, 25)
    text_6 = font_6.render(quote,True,text_color)
    screen.blit(text_6, (50, 450))

    font_8 = pygame.font.Font(None,30)
    text_8 = font_8.render("Back",True, text_color)
    screen.blit(text_8,(582,60))

    font_9 = pygame.font.Font(None, 30)
    text_9 = font_9.render("Click Yes or No Button regarding completion of habit for today: ",True,text_color)
    screen.blit(text_9, (0,100))

    font_12 = pygame.font.Font(None, 30)
    text_12 = font_12.render("Progress: ",True,text_color)
    screen.blit(text_12, (0,270))

    yes_button=pygame.image.load('assets/yes(1).png').convert_alpha()
    yes1=yes.Yes(95,135 , yes_button, 0.8)

    font_10 = pygame.font.Font(None, 35)
    text_10 = font_10.render(f'Yes: {data["Yes"]}',True,text_color)
    screen.blit(text_10, (100,240))
    

    no_button=pygame.image.load('assets/no(1).png').convert_alpha()
    no1=no.No(455,135 , no_button, 0.8)

    font_11 = pygame.font.Font(None, 35)
    text_11 = font_11.render(f'No: {data["No"]}',True,text_color)
    screen.blit(text_11, (482,240))

    font_13 = pygame.font.Font(None, 35)
    text_13 = font_13.render("Keep up the goodwork!",True,text_color)
   

    font_14 = pygame.font.Font(None, 35)
    text_14 = font_14.render("Remember your endgoal! You can do it!",True,text_color)
    
    
    draw = pygame.image.load('assets/ladybug.png').convert_alpha()
    ladybug1 = ladybug.Ladybug(580, 0, draw, 0.8)
  
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
              with open('clicker_score12.txt', 'w') as score_file12:
                json.dump(data, score_file12)
              pygame.quit()
              sys.exit
    pos= pygame.mouse.get_pos()
    if ladybug1.rect.collidepoint(pos):
           if pygame.mouse.get_pressed()[0]==1 and ladybug1.clicked == False:
              ladybug1.clicked= True
              question()
    if pygame.mouse.get_pressed()[0] ==0:
              ladybug1.clicked= False

    elif yes1.rect.collidepoint(pos):
           if pygame.mouse.get_pressed()[0]==1 and yes1.clicked == False:
              yes1.clicked= True
              data["Yes"] +=1
              yes1=yes.Yes(95,135 , yes_button, 0.8)
              text_10 = font_10.render(f'Yes: {data["Yes"]}',True,text_color)
              screen.blit(text_13, (0,50))
              if progress < 365:
                  progress += 1
              elif progress ==365:
                font_15 = pygame.font.Font(None, 25)
                text_15 = font_15.render("Congrats you completed your goal!",True,text_color)
                screen.blit(text_15, (365,315))
              
              text= font_1.render("Loading: "  + str(int(progress)) + "%", True, green)
              
              pygame.draw.rect(screen, green, (0,300, progress, 100))
              screen.blit(text, (453, 273))
              
             
    if pygame.mouse.get_pressed()[0] ==0:
              yes1.clicked= False

    elif no1.rect.collidepoint(pos):
           if pygame.mouse.get_pressed()[0]==1 and no1.clicked == False:
              no1.clicked= True
              data["No"] +=1
              no1=no.No(455,135 , no_button, 0.8)
              text_11 = font_11.render(f'No: {data["No"]}',True,text_color)
              screen.blit(text_14, (0,50))
              text= font_1.render("Loading: "  + str(int(progress)) + "%", True, green)
             
              pygame.draw.rect(screen, green, (0,300, progress, 100))
              screen.blit(text, (453, 273))

             
             
    if pygame.mouse.get_pressed()[0] ==0:
              no1.clicked= False

    pygame.display.flip()
    screen.blit(ladybug1.image, (ladybug1.rect.x, ladybug1.rect.y))
    screen.blit(yes1.image, (yes1.rect.x, yes1.rect.y))
    screen.blit(no1.image, (no1.rect.x, no1.rect.y))

  
    
    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)

def links():
  screen_width= 650
  screen_height= 700
  screen_color_7 = (255,255,255)
  screen = pygame.display.set_mode([screen_width, screen_height])
  movement=True
  quotes_list= ['Do one thing every day that scares you ― Eleanor Roosevelt', 'Hold the vision, trust the process - Unknown', 'You are doing amazing, sweetie - Kris Jenner','I am alive, motivated and ready to slay the day #MONSLAY - Unknown', 'The hard days are what make you stronger - Aly Raisman', 'Habits form based on frequency, not time - James Clear', 'If you can dream it, you can do it- Walt Disney', 'The future belongs to those who prepare for it today - Malcolm X', 'Nothing will work unless you do - Maya Angelou', 'Successful people are simply those with sucessful habits - Brian Tracy']
  num = random.randint(0,9)
  quote = quotes_list[num]
  print(quote)
  
  

  while movement:
    screen.fill(screen_color_7)
    text_color = (1,50,32)
    font_7 = pygame.font.Font(None, 35)
    text_7 = font_7.render("Url's ",True,text_color)
    screen.blit(text_7, (0,0))
    font_8 = pygame.font.Font(None,30)
    text_8 = font_8.render("Back",True, text_color)
    screen.blit(text_8,(582,60))
    font_6 = pygame.font.Font(None, 25)
    text_6 = font_6.render(quote,True,text_color)
    screen.blit(text_6, (50, 450))


    font_8 = pygame.font.Font(None, 15)
    text_8 = font_8.render("https://www.forbes.com/sites/theyec/2020/08/19/tips-and-resources-that-will-help-you-build-better-habits/?sh=330889e1ec83",True,text_color)
    screen.blit(text_8, (0,100))


    font_9 = pygame.font.Font(None, 20)
    text_9 = font_9.render("https://www.youtube.com/watch?v=-moW9jvvMr4&t=1s",True,text_color)
    screen.blit(text_9, (0,200))


    font_10 = pygame.font.Font(None, 20)
    text_10 = font_10.render("https://theartofliving.com/atomic-habits-summary/",True,text_color)
    screen.blit(text_10, (0,300))

    font_11 = pygame.font.Font(None, 20)
    text_11 = font_11.render("https://www.youtube.com/watch?v=AdKUJxjn-R8", True, text_color)
    screen.blit(text_11, (0,400))

    

  
    draw = pygame.image.load('assets/ladybug.png').convert_alpha()
    ladybug1 = ladybug.Ladybug(580, 0, draw, 0.8)
  
    for event in pygame.event.get():
  
      pos= pygame.mouse.get_pos()
    if ladybug1.rect.collidepoint(pos):
           if pygame.mouse.get_pressed()[0]==1 and ladybug1.clicked == False:
              ladybug1.clicked= True
              question()
    if pygame.mouse.get_pressed()[0] ==0:
              ladybug1.clicked= False
    screen.blit(ladybug1.image, (ladybug1.rect.x, ladybug1.rect.y))

    
    for event in pygame.event.get():
            if event.type ==pygame.QUIT:
              pygame.quit()
    pygame.display.update()
    pygame.display.flip()
    
    
    
   
main()
