from rover import Rover
from position import Position

# first position
p1 = Position(3,3,"E")

# first rover
r1 = Rover(p1)

r1.getRover() # this works

nav = ['L','M','L','M','L','M','L','M','M']
nav2 = ['M','M','R','M','M','R','M','R','R','M']
# nav = ['R','R']

# moving rover
r1.moveRover(nav2)

r1.getRover()
