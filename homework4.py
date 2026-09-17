import math
from graphics import GraphWin, Point, Polygon
def main (_):
# prompt user for input
n=int(input("Enter the number of sides for the polygon: "))
radius=float(input("Enter the radius of the polygon: "))

#open the graphics window (400x400 pixels)
win = GraphWin("Regular Polygon", 400, 400)
win.setCoords(-200, -200, 200, 200) #Center the coordinate system at (0,0)

# calculate the angle between each side in radians
angle_step = (2 * math.pi / n)

#initialize an empty list to store the vertices of the polygon
vertices = []

# Loop to calculate the coordinates of each vertex
for i in range(n):
    angle = i * angle_step

    x = radius * math.cos(angle)
    y = radius * math.sin(angle)

    vertices.append(Point(x, y))

#create a polygon using the calculated vertices
polygon = Polygon(vertices)
poly.set Outline("blue")
poly.seetFill("lightblue")
# draw the polygon in the graphics window

#wait for a mouse click before closing the window
win.getMouse()
win.close()