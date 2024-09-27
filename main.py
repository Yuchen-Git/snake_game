from turtle import Screen, Turtle
import time
from turtledemo.penrose import start

from food import Food  # Import the Food class from another file
from scoreboard import Scoreboard  # Import the Scoreboard class from another file
from snack import Snake  # Import the Snake class from another file

# Game constants
SPEED = 0.5  # Speed of the snake's movement (time delay between each move)
WIDTH = 600  # Screen width
HEIGHT = 600  # Screen height

# Set up the screen
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)  # Set screen size
screen.bgcolor('black')  # Set the background color of the screen to black
screen.title('Snake Game')  # Set the title of the window
screen.tracer(0)  # Disable automatic screen updates (manual control)

# Create instances of Snake, Food, and Scoreboard
snake = Snake()  # Create the snake instance
food = Food()  # Create the food instance
score = Scoreboard()  # Create the scoreboard instance

# Set up key listeners for controlling the snake
screen.listen()  # Enable the screen to listen for keypresses
screen.onkey(snake.up, "Up")  # Move the snake up when the 'Up' arrow key is pressed
screen.onkey(snake.down, "Down")  # Move the snake down when the 'Down' arrow key is pressed
screen.onkey(snake.left, "Left")  # Move the snake left when the 'Left' arrow key is pressed
screen.onkey(snake.right, "Right")  # Move the snake right when the 'Right' arrow key is pressed





# Main game loop

game_over = False  # Variable to track if the game is over
while not game_over:
    snake.snake_move()  # Move the snake
    time.sleep(SPEED)  # Pause the game to control the speed
    screen.update()  # Update the screen with the latest changes

    # Check if the snake has collided with the food
    if snake.head.distance(food) < 15:  # If the distance between snake's head and food is less than 15
        food.rand_location()  # Move the food to a random location
        snake.growth()  # Grow the snake
        score.update_score()  # Update the score

    # Check if the snake has collided with the wall
    if WIDTH/2-abs(snake.head.xcor())  < 10 or HEIGHT/2 - abs(snake.head.ycor()) < 10:  # If the snake's head is too close to the wall
        score.game_over()  # Display "Game Over" on the screen
        game_over = True  # End the game

    # Check if the snake has collided with its own body
    for sk in snake.segment_lst[1:]:  # Loop through all snake segments except the head
        if snake.head.distance(sk) < 10:  # If the distance between the snake's head and any segment is less than 10
            score.game_over()  # Display "Game Over" on the screen
            game_over = True  # End the game








# Keep the window open until clicked
screen.exitonclick()  # Wait for the user to click on the screen to close the game window