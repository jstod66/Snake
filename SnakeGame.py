from graphics import *
import math
import random
from SnakeClasses import *
from checkCollision import *

def main():
	
    GRID_SIZE = 20
    MS_PER_FRAME = 90
    SCALE = 20
    HEIGHT = GRID_SIZE*SCALE
    WIDTH = HEIGHT

    win = GraphWin("Snake Game", WIDTH,HEIGHT)
    win.setBackground(color_rgb(0,0,0))

    Exit = WelcomeScreen(win,WIDTH)

    s = Snake(Point(SCALE*math.floor(GRID_SIZE/2),SCALE*math.floor(GRID_SIZE/2)),Point(SCALE*(math.floor(GRID_SIZE/2)+1),SCALE*(math.floor(GRID_SIZE/2)+1)),win)
    f = Food(Point(SCALE*math.floor(GRID_SIZE/4),SCALE*math.floor(GRID_SIZE/4)),Point(SCALE*(math.floor(GRID_SIZE/4)+1),SCALE*(math.floor(GRID_SIZE/4)+1)),win)
    Tail = [];

    FPS = Text(Point(SCALE/2,SCALE/2),'0')
    FPS.setSize(6)
    FPS.setTextColor('white')
    FPS.draw(win)
    start_time = 0
    
    lastKeyPress = win.checkKey()
    Eaten = False
    
    while(lastKeyPress!='x'):

        if(Exit):
            break

        #Log time to control (and display) frame rate
        end_time = time.time()*1000
        FPS.setText("%.1f" %(1000/(end_time-start_time)))
        start_time = time.time()*1000
        lastKeyPress = win.checkKey()


        #Move tail along
        #Add to tail if food eaten in last iteration
        beforeLength = len(Tail)
        if(Eaten):
            if(len(Tail)>0):
                Tail.append(Tail[len(Tail)-1].clone())
                Tail[len(Tail)-1].draw(win)
            else:
                Tail.append(s.clone())
                Tail[0].draw(win)

        if(beforeLength!=0):      
        #Move all the tail segments 
            for i in range(beforeLength-1,0,-1):
                Tail[i].move(Tail[i-1].getCenter().getX()-Tail[i].getCenter().getX(),Tail[i-1].getCenter().getY()-Tail[i].getCenter().getY())

            Tail[0].move(s.getCenter().getX()-Tail[0].getCenter().getX(),s.getCenter().getY()-Tail[0].getCenter().getY())

        #Update the head of the snake based on key press, speed and location
        canMove = s.update(win,lastKeyPress,SCALE,WIDTH)

        #Check if food has been eaten, and initialise protocols if so
        Eaten = f.checkEat(s,SCALE)
        if(Eaten):
            del f
            #Fix later to stop food spawning in cells occupied by snake/tail
            fx = random.randint(0,GRID_SIZE-1)
            fy = random.randint(0,GRID_SIZE-1)
            f = Food(Point(SCALE*fx,SCALE*fy),Point(SCALE*(fx+1),SCALE*(fy+1)),win)

        Collided = checkCollision(s,Tail,SCALE)

        #Simple Reset Functionality
        if(( not canMove)|(Collided)):
            s.undraw()
            del s
            f.undraw()
            del f
            for t in Tail:
                t.undraw()
            del Tail
            FPS.undraw()

            Exit = ResetScreen(win,WIDTH)
            if(Exit):
                break
            
            Tail = []
            s = Snake(Point(SCALE*math.floor(GRID_SIZE/2),SCALE*math.floor(GRID_SIZE/2)),Point(SCALE*(math.floor(GRID_SIZE/2)+1),SCALE*(math.floor(GRID_SIZE/2)+1)),win)
            f = Food(Point(SCALE*math.floor(GRID_SIZE/4),SCALE*math.floor(GRID_SIZE/4)),Point(SCALE*(math.floor(GRID_SIZE/4)+1),SCALE*(math.floor(GRID_SIZE/4)+1)),win)
            Eaten = False
            FPS.draw(win)

        #Wait until end of frame duration if there is still time left
        end_time = time.time()*1000
        if((end_time-start_time) < MS_PER_FRAME):
            time.sleep((MS_PER_FRAME - (end_time-start_time))/1000)
        
    win.close()  

def ResetScreen(win,WIDTH):

    ResetMessage = Text(Point(WIDTH/2,WIDTH/2),"YOU DIED! \n PRESS 'r' TO RESET OR 'x' TO EXIT")
    ResetMessage.setSize(16)
    ResetMessage.setTextColor('white')
    ResetMessage.draw(win) 

    lastKeyPress = win.checkKey()
    while((lastKeyPress!='r')&(lastKeyPress!='x')):
        lastKeyPress = win.checkKey()

    ResetMessage.undraw()
    del ResetMessage

    if(lastKeyPress=='r'):
        return False
    else:
        return True

def WelcomeScreen(win,WIDTH):

    WelcomeMessage = Text(Point(WIDTH/2,WIDTH/2),"WELCOME TO SNAKE! \n USE 'w','a','s','d' TO MOVE \n PRESS 'x' AT ANY TIME TO EXIT \n PRESS 'e' to GET STARTED!")
    WelcomeMessage.setSize(16)
    WelcomeMessage.setTextColor('white')
    WelcomeMessage.draw(win) 

    lastKeyPress = win.checkKey()
    while((lastKeyPress!='e')&(lastKeyPress!='x')):
        lastKeyPress = win.checkKey()

    WelcomeMessage.undraw()
    del WelcomeMessage

    if(lastKeyPress=='e'):
        return False
    else:
        return True

main()
