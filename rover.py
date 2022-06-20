from position import Position

class Rover(Position):

    def __init__(self, position):
        self._position = position

    def setTurn(self, dir):
        dir_list_r = ['N','E','S','W']
        dir_list_l = ['N', 'W', 'S', 'E']
        temp = (self._position.getPosition())[2]

        if dir == "left":
            indx = dir_list_l.index(temp)
            if indx <3:
                temp = dir_list_l[indx+1]
            else:
                temp = dir_list_l[0]

        else:
            indx = dir_list_r.index(temp)
            if indx < 3:
                temp = dir_list_r[indx + 1]
            else:
                temp = dir_list_r[0]

        self._position.setPositionD(temp)


    def moveRover(self, alist):

        for a in alist:
            if a == 'R':
                self.setTurn("right")

            elif a == 'L':
                self.setTurn("left")

            elif a == 'M' and self._position.getPosition()[2] == 'N':
                self._position.setPositionY(self._position.getPosition()[1]+1)
                #self._position._y += 1

            elif a == 'M' and self._position.getPosition()[2] == 'S':
                self._position.setPositionY(self._position.getPosition()[1] - 1)
                #self._position._y -= 1

            elif a == 'M' and self._position.getPosition()[2] == 'E':
                self._position.setPositionX(self._position.getPosition()[0] + 1)
                #self._position._x += 1

            elif a == 'M' and self._position.getPosition()[2] == 'W':
                self._position.setPositionX(self._position.getPosition()[0] - 1)
                #self._position._x -= 1

    def getRover(self):
        print(self._position.getPosition())
