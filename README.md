# CS110 Project Proposal
# Habit Tracker
## CS 110 Final Project
### Fall Semester, 2026 
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit?usp=sharing)

repl(https://replit.com/@GabriellaVieira/final-project-gabi-and-sydney) 

Presentation: [https://docs.google.com/presentation/d/15KbRcQrtEqM7g_V8eK6M_wJjn4QZH6hoAgVqLtRXM90/edit#slide=id.p]


### Team: Gabi and Sydney
#### Sydney Palmer and Gabriella Vieira

***

## Project Description

Additional Modules = json, sys
Data Permanence Feature = json files

A habit tracker that tracks the habits the user inputs with the ability to track the habit with the set times of: one month, 3 months, 6 months, 12 months. Along with the feature of randomized quotes presented on the various screens to motivate the users. The user can update the progress bar to see their progress towards their goal. Once the habit is completed, the user will get a celebratory message.

***    

## User Interface Design
All pictures of the final designs and original concept are in the etc folder
- **Initial Concept**
-First screen: The interface has a background with flowers, a start button to get to the next screen, and the title Habit Tracker. 
-Second screen: This interface has a welcoming message along with three different places for the user to input information regarding their name, goal, and how long they want to do the goal for.
-Third screen: This interface asks the user whether or not they completed their goal which will be shown by them clicking the yes or no button. Finally after the user logs their progress if it was yes a new flower will appear in a garden to show their progress.
-Fourth screen: This interface has links provided that the user can copy into another tab to then learn more on how to build better routines to sucessfully create habits.


-**Final Concept**
- First Screen: This interface is our first screen that viewers see when using our program. It consists of our title/caption of our project, flower graphics, and a bee button that makes the user then be inclined to write their name and goal.
- Second Screen: This interface is our second screen that viewers see after writing down their name and goal. This page has a welcome screen along with a message indicating to write down their name and goal. The graphics of the screen include a pen and a butterfly which is a button that allows user to move on the next page.
- Third Screen: This interface is our third screen that includes another welcome message and a phrase indicating how long do they wish to practice their habit for. After these messages there are 5 buttons to choose consisting of the 1, 3, 6, and 12 months where users are then taken to that specific habit tracker. Or they can click the extra resources button which gives them useful links that they can manually type in the Internet to learn more about creating sucessful routines for habits.
- Url Screen: This interface is our url screen that contains a couple of links a user can use and manually type in the Internet to learn more about habits and creating benefical routines. Along with a motivating quote on the bottom of the page so that users are consistently feeling empowered. Finally there is a ladybug button which takes user back to the third screen.
- Habit 1 Screen: This interface is our habit 1 screen. Here it has a title of One Month on the top left along with a white screen in the middle and the ladybug button on the top which users can click to take them back to the third screen. This section contains a message asking if the user completed their habit, a yes and no button, which both are on top the progress bar. When clicked on the yes button it will increase the progress bar by 1% and give the user a specific message that tells them to keep up the good work. The no button shows the progress bar as well but it does not increase the progress as this button indicates that the user did not complete their habit for the given day. Along with giving the users a motivating message to basically not give up. The progress bar goes to 31% which then gives the user a congratulator message. Finally there is a motivating quote on the botton.
  
- Habit 3 Screen:This interface is our habit 3 screen. Here it has a title of Three Months on the top left along with a white screen in the middle and the ladybug button on the top which users can click to take them back to the third screen. This section contains a message asking if the user completed their habit, a yes and no button, which both are on top the progress bar. When clicked on the yes button it will increase the progress bar by 1% and give the user a specific message that tells them to keep up the good work. The no button shows the progress bar as well but it does not increase the progress as this button indicates that the user did not complete their habit for the given day. Along with giving the users a motivating message to basically not give up. The progress bar goes to 90% which then gives the user a congratulator message. Finally there is a motivating quote on the botton.
  
- Habit 6 Screen:  This interface is our habit 6 screen. Here it has a title of Six Months on the top left along with a white screen in the middle and the ladybug button on the top which users can click to take them back to the third screen. This section contains a message asking if the user completed their habit, a yes and no button, which both are on top the progress bar. When clicked on the yes button it will increase the progress bar by 1% and give the user a specific message that tells them to keep up the good work. The no button shows the progress bar as well but it does not increase the progress as this button indicates that the user did not complete their habit for the given day. Along with giving the users a motivating message to basically not give up. The progress bar goes to 181% which then gives the user a congratulator message. Finally there is a motivating quote on the botton.
  
- Habit 12 Screen: This interface is our habit 12 screen. Here it has a title of Twelve Months on the top left along with a white screen in the middle and the ladybug button on the top which users can click to take them back to the third screen. This section contains a message asking if the user completed their habit, a yes and no button, which both are on top the progress bar. When clicked on the yes button it will increase the progress bar by 1% and give the user a specific message that tells them to keep up the good work. The no button shows the progress bar as well but it does not increase the progress as this button indicates that the user did not complete their habit for the given day. Along with giving the users a motivating message to basically not give up. The progress bar goes to 365% which then gives the user a congratulator message. Finally there is a motivating quote on the botton.
    
    
- **Final GUI**
- Google doc of GUI photos and Inital Concept 
 (https://docs.google.com/document/d/1-Yiqk-x1TNsRsXSY7Rc2G1nXIbWjH4xQZvJ7_r4Zf14/edit)
-also found in the etc folder
   
***        

## Program Design
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
class Button:
  '''
  general function description: Creates the bee button which is the first screen that allows user to begin using our program.
	args: bee, x, y, image, scale
	
  '''
  def __init__(bee, x, y, image, scale):
     width= image.get_width()
     height= image.get_height()
     bee.image = pygame.transform.scale(image, (int(width * scale ), int(height*scale)))
     bee.rect= bee.image.get_rect()
     bee.rect.topleft = (x,y)
     bee.clicked=False
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
class Choose:
  '''
  general function description: Creates one of the buttons for the four different habits
	args: flower7, x, y, image, scale

  '''
  def __init__(flower7, x, y, image, scale):
     width= image.get_width()
     height= image.get_height()
     flower7.image = pygame.transform.scale(image, (int(width * scale ), int(height*scale)))
     flower7.rect= flower7.image.get_rect()
     flower7.rect.topleft = (x,y)
     flower7.clicked=False
class Habit:
  '''
  general function description: Creates one of the buttons for the 4 different habits.
	args: flower4, x, y, image, scale
  '''
  def __init__(flower4, x, y, image, scale):
     width= image.get_width()
     height= image.get_height()
     flower4.image = pygame.transform.scale(image, (int(width * scale ), int(height*scale)))
     flower4.rect= flower4.image.get_rect()
     flower4.rect.topleft = (x,y)
     flower4.clicked=False
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
class No:
  '''
  general function description: Creates the no button that indicates that the user did not complete their habit for that given day.
	args: no1, x, y, image, scale
	
  '''
  def __init__(no1, x, y, image, scale):
     width= image.get_width()
     height= image.get_height()
     no1.image = pygame.transform.scale(image, (int(width * scale ), int(height*scale)))
     no1.rect= no1.image.get_rect()
     no1.rect.topleft = (x,y)
     no1.clicked=False
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

  


Pygame - module used to draw the flowers in the garden class.
URL for Pygame = https://www.pygame.org/docs/

* Non-Standard libraries
    * json and sys
         - json: https://docs.python.org/3/library/json.html, sys: https://docs.python.org/3/library/sys.html
         - json: stores information which in our case is the amount of times the user clicks the yes or no button in each of the 4 different habit features., sys: allows user to manipulate the screen which in our case they can exit the program in the four different habit features where there data is then saved due to our json feature.
         


* Class Interface Design
   Link: https://docs.google.com/document/d/13W1iGgsFNQafHnFafasPPniPEsFmq6QGY2nJSGMw2S4/edit
  Picture is also in the etc folder
  
* Classes
    butterfly.py = creates butterfly button used on welcome page as a next button
    button.py = creates bee button used on home page
    choice.py = creates flower button to take user to 3 month screen
    choose.py = creates flower button to take user to 12 month screen
    habit.py = creates flower button that takes user to 1 month screen
    ladybug.py = creates ladybug button so user can go back to previous screen
    main.py = controls all the classes and function
    no.py = creates no flower button to give encouragement to keep striving towards goal
    option.py = creates button to take user to 6 month screen
    resource.py = creates button to take user to extra resources page
    yes.py  = creates yes flower button to say you've completed the habit for the day

## Project Structure and File List

The Project is broken down into the following file structure:

* main.py
* src
    butterfly.py
    button.py
    choice.py
    choose.py
    habit.py
    ladybug.py
    main.py
    no.py
    option.py
    progressbar.py
    resource.py
    save.py
    yes.py
* assets
    Bee.png
    butterfly.png
    class_diagram.jpg
    flowbut1.png
    Flower 4.png
    Flower 5.png
    Flower 6.png
    Flower Icon.png
    flower.resources.png
    flowerbut_3.png
    ladybug.png
    lotus.png
    no(1).png
    rose(1).png
    yes(1).png
* etc
  First screen.png
  Habit 1.png
  Habit 3.png
  Habit 6.png
  Habit 12.png
  Original Concept.jpeg
  Second screen.png
  Third Screen.png
  Url.png

***

## Tasks and Responsibilities 

Sydney = Worked on the interfaces of the screens, creative design, research, helped with classes, cleaned up code
Gabriella = Created modules, research, made buttons and classes, found the website for the images, creative design

## Testing

Our strategy for testing our code was coding small sections/functions and then debugged that section. We utilized the print function in order to find and get rid of bugs. Working in smaller sections makes it easier to spot bugs and avoid being overwhelmed. 
Ex: Testing after each button, each image, progress bar, and drawing/text.
## ATP

| Step                 |Procedure                                   |Expected Results                                      |
|----------------------|:------------------------------------------ |-----------------------------------------------------:|             
|  1                   |Type python3 main.py into shell             |Program starts to run and pygame screen is initalized          
|  2                   |Use cursor in screen to click bee           |The console asks you to insert name and habit
|  3                   |Type your name and habit in the console     |Name and habit is displayed on screen 
|  4                   |Cursor clicks the area of next button       |The screen fills with green color, with flower images that act as buttons   
|  5                   |Cursor clicks the area of flower button 1   |Screen fills with darker green color and displays inspirational quote and two images (buttons) 
|  6                   |Cursor clicks area of the potted flower     |Progress, clicks and loading % increases until 31% (number of days in one month)
|  7                   |Cursor clicks area of right flower          |Progress, clicks and loading % stay the same and a message appears
|  8                   |Cursor clicks area of the ladybug           |Screen fills with green and same flowers(buttons) in previous screen 
|  9                   |Cursor clicks the area of flower button 2   |Screen fills with darker green color and displays inspirational quote and two images (buttons)
| 10                   |Cursor clicks area of the potted flower     |Progress and loading % increases until 90% (number of days in 3 months)
| 11                   |Cursor clicks area of right flower          |Progress and loading % stay the same and a message appears
| 12                   |Cursor clicks area of the ladybug           |Screen fills with green and same flowers(buttons) in previous screen 
| 13                   |Cursor clicks the area of flower button 3   |Screen fills with darker green color and displays inspirational quote and two images (buttons)
| 14                   |Cursor clicks area of the potted flower     |Progress and loading % increases until 181% (number of days in 6 months) 
| 15                   |Cursor clicks area of right flower          |Progress and loading % stay the same and a message appears
| 16                   |Cursor clicks area of the ladybug           |Screen fills with green and same flowers(buttons) in previous screen 
| 17                   |Cursor clicks the area of flower button 4   |Screen fills with darker green color and displays inspirational quote and two images (buttons)
| 18                   |Cursor clicks area of the potted flower     |Progress and loading % increases until 365% (number of days in 12 months) 
| 19                   |Cursor clicks area of right flower          |Progress and loading % stay the same and a message appears
| 20                   |Cursor clicks area of the ladybug           |Screen fills with green and same flowers(buttons) in previous screen 
| 21                   |Cursor clicks the exit button of pygame     |The data of numbers of clicks for "yes" and "no" are saved    

