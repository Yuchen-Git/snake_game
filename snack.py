from turtle import Turtle

# Constants for snake's initial state and movement
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]  # Initial positions of the snake's segments
MOVE_DISTANCE = 20  # Distance the snake moves in each step
RIGHT = 0  # Angle for right direction
LEFT = 180  # Angle for left direction
UP = 90  # Angle for up direction
DOWN = 270  # Angle for down direction

# Snake class to control the behavior of the snake
class Snake:
    def __init__(self):
        self.segment_lst = []  # List to store the segments of the snake
        self.create_snake()  # Create the initial snake body
        self.head = self.segment_lst[0]  # The head of the snake is the first segment

    # Method to add a new segment to the snake
    def add_segment(self):
        snake = Turtle(shape='square')  # Create a new square segment
        snake.color('white')  # Set the color of the segment to white
        snake.penup()  # Prevent drawing when the segment moves
        self.segment_lst.append(snake)  # Add the segment to the snake's list of segments

    # Method to create the snake at the start of the game
    def create_snake(self):
        for index, position in enumerate(STARTING_POSITION):
            self.add_segment()  # Add a segment for each initial position
            self.segment_lst[index].goto(position)  # Place the segment at its starting position

    # Method to move the snake forward
    def snake_move(self):
        # Move each segment to the position of the one ahead, starting from the tail
        for segment_index in range(len(self.segment_lst) - 1, 0, -1):
            new_xcor = self.segment_lst[segment_index - 1].xcor()  # Get the x-coordinate of the segment ahead
            new_ycor = self.segment_lst[segment_index - 1].ycor()  # Get the y-coordinate of the segment ahead
            self.segment_lst[segment_index].goto(new_xcor, new_ycor)  # Move the current segment to that position
        self.segment_lst[0].forward(MOVE_DISTANCE)  # Move the head of the snake forward

    # Methods to change the snake's direction
    def up(self):
        if self.head.heading() != DOWN:  # Prevent the snake from moving up if it's heading down
            self.head.setheading(UP)  # Set the snake's heading to up

    def down(self):
        if self.head.heading() != UP:  # Prevent the snake from moving down if it's heading up
            self.head.setheading(DOWN)  # Set the snake's heading to down

    def left(self):
        if self.head.heading() != RIGHT:  # Prevent the snake from moving left if it's heading right
            self.head.setheading(LEFT)  # Set the snake's heading to left

    def right(self):
        if self.head.heading() != LEFT:  # Prevent the snake from moving right if it's heading left
            self.head.setheading(RIGHT)  # Set the snake's heading to right

    # Method to grow the snake when it eats food
    def growth(self):
        new_xcor = self.segment_lst[-1].xcor()  # Get the x-coordinate of the last segment
        new_ycor = self.segment_lst[-1].ycor()  # Get the y-coordinate of the last segment
        self.add_segment()  # Add a new segment to the snake
        self.segment_lst[-1].goto(new_xcor, new_ycor)  # Place the new segment at the position of the last segment