def checkCollision(s,Tail,SCALE):

    if(len(Tail)>3):
        sx = s.getCenter().getX()
        sy = s.getCenter().getY()
        for t in Tail:
            tx = t.getCenter().getX()
            ty = t.getCenter().getY()
            if(((tx-sx)**2<SCALE)&((ty-sy)**2<SCALE)):
                return True
    
    return False

