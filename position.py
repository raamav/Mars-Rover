class Position():
    def __init__(self ,x ,y ,d):
        self._x = x
        self._y = y
        self._d = d

    def setPositionD(self,d):
        self._d = d

    def setPositionX(self,x):
        self._x = x

    def setPositionY(self,y):
        self._y = y

    def getPosition(self):
        return(self._x,self._y,self._d)


