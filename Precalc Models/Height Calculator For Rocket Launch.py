# 1.4 

def height_calculator(t):
    if 0 <= t <= 20:
        height = -5 * t**2 + 100 * t
        print("Height is " + str(height))
    if t > 20:
        height = 0
        print("Rocket has returned to land already as height is " + str(height))
