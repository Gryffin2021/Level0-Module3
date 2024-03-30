def setup():
    # Set the size of your sketch
    size(1000, 1000)
    
    pass
    
def draw():
    # Starting with the largest ellipse, use a for loop to draw a bullseye with ellipses
    num = 800
    for i in range(8):
        if(i % 2 == 0):
            fill(255, 0, 0)
        else:
            fill(0, 0, 0)
        ellipse(500, 500, num, num)
        num -= 100
    # Use an if statement and modulo to alternate the color of your rings
    
    
    pass
