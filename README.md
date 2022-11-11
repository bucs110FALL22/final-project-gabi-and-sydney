:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
# << Habit Tracker>>
## CS 110 Final Project
### << Fall Semester, 2026 >>
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit?usp=sharing)

repl(https://replit.com/@GabriellaVieira/final-project-gabi-and-sydney) 

<< [link to demo presentation slides](#) >>

### Team: Gabi and Sydney
#### Sydney Palmer and Gabriella Vieira

***

## Project Description

<< Give an overview of your project >>

***    

## User Interface Design

- **Initial Concept**
  - << A wireframe or drawing of the user interface concept along with a short description of the interface. You should have one for each screen in your program. For example, if your program has a start screen, game screen, and game over screen, you should include a wireframe / screenshot / drawing of each one and a short description of the components. >>
    
    
- **Final GUI**
  - << You should also have a screenshot of each screen for your final GUI >>

***        

## Program Design
'''
The garden would be a function that creates flowers in random places using coordinates while also have a specific color and shape
Arguments: color, shape, x, y, height, width
'''
Class Garden: 
  def init(self, color, shape, x, y, height, width): 
    self.color = color 
    self.shape = flower 
    self.x = x 
    self.y = y 
    self.height = height 
    self.width = width

Class Homepage:
  '''
  General function: This function creates the homepage screen which is the first thing the viewers will see before using our program 
  Arguments: Self, title, color, shape, x, y, height, and width
  '''
  def init(self, title, color, shape, x, y, height, width):
    self.title = title 
    self.color = color 
    self.shape = flower 
    self.x = x 
    self.y = y 
    self.height = height 
    self.width = width

'''
Function that makes the title page of the program. Allows the user to input their name, the goal they want to achieve and the time frame they want to complete it in.
Aguments: Self, name, date, time, goal, x, y, height, width
'''
Class Introduction: 
  def init(self, name, date, time, goal, x, y, height, width):     self.name = name 
    self.date = date 
    self.time = time 
    self.goal = goal 
    self.x = x 
    self.y = y 
    self.height = height
    self.width = width


Pygame - module used to draw the flowers in the garden class.
URL for Pygame = https://www.pygame.org/docs/

* Non-Standard libraries
    * << You should have a list of any additional libraries or modules used (pygame, request) beyond non-standard python. 
         For each additional module you should include
         - url for the module documentation
         - a short description of the module >>


* Class Interface Design
    * << A simple drawing that shows the class relationships in your code (see below for an example). This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm. >>
        * ![class diagram](assets/class_diagram.jpg) 
* Classes
    * << You should have a list of each of your classes with a description. >>

## Project Structure and File List

The Project is broken down into the following file structure:

* main.py
* src
    * << all of your python files should go here >>
* assets
    * << all of your media, i.e. images, font files, etc, should go here) >>
* etc
    * << This is a catch all folder for things that are not part of your project, but you want to keep with your project >>

***

## Tasks and Responsibilities 

   * Outline the team member roles and who was responsible for each class/method, both individual and collaborative.

## Testing

* << Describe your testing strategy for your project. >>

## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Run Counter Program  |GUI window appears with count = 0  |
|  2                   | click count button   | display changes to count = 1      |
etc...
