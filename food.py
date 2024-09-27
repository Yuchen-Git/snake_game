from turtle import Turtle
import random

# Constants for food size
STRETCH_WID = 1  # Width stretch factor for the food
STRETCH_LEN = 1  # Length stretch factor for the food

# Food class to create food for the snake game
class Food(Turtle):
    def __init__(self):
        super().__init__()  # Initialize the Turtle class
        self.shape('circle')  # Set the shape of the food to a circle
        self.penup()  # Lift the pen to avoid drawing lines when moving
        self.shapesize(stretch_wid=STRETCH_WID, stretch_len=STRETCH_LEN)  # Set the size of the food
        self.color("green")  # Set the color of the food to green
        self.rand_location()  # Randomize the initial location of the food

    # Method to move the food to a random location on the screen
    def rand_location(self):
        rand_x = random.randint(-280, 280)  # Generate a random x-coordinate within the screen bounds
        rand_y = random.randint(-280, 280)  # Generate a random y-coordinate within the screen bounds
        self.goto(rand_x, rand_y)  # Move the food to the generated coordinates