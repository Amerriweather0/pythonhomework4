from graphics import *
import math

# Logistic function
def logistic(x, k):
    return k * x * (1 - x)

# Create graphics window
win = GraphWin("Logistic Function", 700, 500)

# Draw x-axis
x_axis = Line(Point(50, 450), Point(650, 450))
x_axis.draw(win)

# Draw y-axis
y_axis = Line(Point(50, 50), Point(50, 450))
y_axis.draw(win)

# Starting value
x = 0.1

# Value of k
k = 3.9

# Plot 100 points
for i in range(100):
    y = logistic(x, k)

    # Convert values to screen coordinates
    screen_x = 50 + i * 6
    screen_y = 450 - y * 400

    point = Point(screen_x, screen_y)
    point.draw(win)

    # Calculate next value
    x = y

# Wait for mouse click
win.getMouse()

# Close window
win.close()