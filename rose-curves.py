from math import sin 
from math import cos 
from math import radians 
  
import pygame 
 
(width, height) = (800, 600)

n = 0
  
# setup window and init the screen surface 
screen = pygame.display.set_mode((width, height)) 
  
pygame.display.set_caption('rose curves :)') 
  
# background
screen.fill((150, 150, 250))

# rose with n petals  of radius of size
def drawRhodoneaCurve(n, size):
    points =[] 
    for i in range(0, 361): 
        # equation of a rhodonea curve 
        r = size * sin(radians(n * i)) 
  
        # cartesian conversion
        x = r * cos(radians(i)) 
        y = r * sin(radians(i)) 
  
        list.append(points, (width / 2 + x, height / 2 + y))
    # draws a set of line segments connected by set of vertices points 
    pygame.draw.lines(screen, (255, 255, 255), False, points, 2)


# maurer rose with value n and d, size of size
def drawMaurerRose(n, d, size): 
    points =[] 
    for i in range(0, 361): 
        # equation of a maurer rose 
        k = i * d 
        r = size * sin(radians(n * k)) 
  
        # cartesian conversion
        x = r * cos(radians(k)) 
        y = r * sin(radians(k)) 
  
        list.append(points, (width / 2 + x, height / 2 + y)) 
  
    pygame.draw.lines(screen, (210, 255, 255), False, points, 1) 

def redraw():
    pygame.display.update()
    screen.fill((150, 150, 250))
    drawRhodoneaCurve(n,200)


  
#drawMaurerRose(6, 73, 200) 




  
# flip the drawn canvas with new canvas
pygame.display.flip() 

run = True
while True :  
    # Poll the events in the event queue 
    for event in pygame.event.get() :
        # if the user closed the window  
        if event.type == pygame.QUIT :  
            pygame.quit()
            quit()
        n = n + 0.01
        redraw()
        #pygame.display.update()
