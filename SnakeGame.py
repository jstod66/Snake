from graphics import *
import math
import random
from SnakeClasses import *

def main():
	
    GRID_SIZE = 30
    MS_PER_FRAME = 100
    SCALE = 20
    HEIGHT = GRID_SIZE*SCALE
    WIDTH = HEIGHT

    win = GraphWin("Snake Game - press 'x' to exit", WIDTH,HEIGHT)
    win.setBackground(color_rgb(0,0,0))

    s = Snake(Point(SCALE*math.floor(GRID_SIZE/2),SCALE*math.floor(GRID_SIZE/2)),Point(SCALE*(math.floor(GRID_SIZE/2)+1),SCALE*(math.floor(GRID_SIZE/2)+1)),win)
    f = Food(Point(SCALE*math.floor(GRID_SIZE/4),SCALE*math.floor(GRID_SIZE/4)),Point(SCALE*(math.floor(GRID_SIZE/4)+1),SCALE*(math.floor(GRID_SIZE/4)+1)),win)
    Tail = [];
    
    lastKeyPress = win.checkKey()
    Eaten = False
    
    while(lastKeyPress!='x'):

        #Log time to control frame rate
        start_time = time.time()*1000
        lastKeyPress = win.checkKey()

        #Add first bit of tail as clone of snake
        if(Eaten & (len(Tail)==0)):
            Tail.append(s.clone())
            Tail[0].draw(win)

        #Move tail along if it exists
        if(len(Tail)>0):
            #Add to tail if food eaten in last iteration
            beforeLength = len(Tail)
            if(Eaten):
                Tail.append(Tail[len(Tail)-1].clone())
                Tail[len(Tail)-1].draw(win)
            #Move all the tail segments 
            for i in range(beforeLength,1):
                Tail[i].move(Tail[i-1].getCenter().getX()-Tail[i].getCenter().getX(),Tail[i-1].getCenter().getY()-Tail[i].getCenter().getY())

            Tail[0].move(s.getCenter().getX()-Tail[0].getCenter().getX(),s.getCenter().getY()-Tail[0].getCenter().getY())

        #Update the head of the snake based on key press, speed and location
        s.update(win,lastKeyPress,SCALE,WIDTH)
            

        #Check if food has been eaten, and initialise protocols if so
        Eaten = f.checkEat(s,SCALE)
        if(Eaten):
            del f
            #Fix later to stop food spawning in cells occupied by snake/tail
            fx = random.randint(0,GRID_SIZE-1)
            fy = random.randint(0,GRID_SIZE-1)
            f = Food(Point(SCALE*fx,SCALE*fy),Point(SCALE*(fx+1),SCALE*(fy+1)),win)

        #Simple Reset Functionality
        if(lastKeyPress=='r'):
            s.undraw()
            del s
            s = Snake(Point(SCALE*math.floor(GRID_SIZE/2),SCALE*math.floor(GRID_SIZE/2)),Point(SCALE*(math.floor(GRID_SIZE/2)+1),SCALE*(math.floor(GRID_SIZE/2)+1)),win)

        #Wait until end of frame duration if there is still time left
        end_time = time.time()*1000
        if((end_time-start_time) < MS_PER_FRAME):
            time.sleep((MS_PER_FRAME - (end_time-start_time))/1000)
        #print(end_time-start_time) #Optional print comp time
        
    win.close()
    

main()
