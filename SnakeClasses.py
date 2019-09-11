from graphics import *
import math

class Snake(Rectangle):

    speed = [1,0];

    def __init__(self,point1,point2,win):
        self.speed = [1,0];
        Rectangle.__init__(self,point1,point2)
        self.setFill('white')
        self.draw(win)

    def update(self,win,lastKeyPress,SCALE,WIDTH):
        if(lastKeyPress=='s'):  
            if(self.speed[1]!= -1):
                self.speed = [0,1]
        if(lastKeyPress=='w'):
            if(self.speed[1]!= 1):
                self.speed = [0,-1]
        if(lastKeyPress=='a'):
            if(self.speed[0]!= 1):
                self.speed = [-1,0]
        if(lastKeyPress=='d'):
            if(self.speed[0]!= -1):
                self.speed = [1,0]

        dx = SCALE*self.speed[0]
        dy = SCALE*self.speed[1]
        x = self.getCenter().getX()
        y = self.getCenter().getY()

        canMove = False
        
        if( ((x+dx) > 0) & ((x+dx) < WIDTH)):
            if(((y+dy) > 0) & ((y+dy) < WIDTH)):
                self.move(dx,dy)
                canMove = True

        return canMove
        
class Food(Rectangle):

    def __init__(self,point1,point2,win):
        Rectangle.__init__(self,point1,point2)
        self.setFill('red')
        self.draw(win)

    def checkEat(self,snake,SCALE):
        sx = snake.getCenter().getX()
        sy = snake.getCenter().getY()
        x = self.getCenter().getX()
        y = self.getCenter().getY()
        if(((x-sx)**2<SCALE) & ((y-sy)**2<SCALE)):
            self.undraw()
            return True
        return False
        
        
