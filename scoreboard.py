from turtle import Turtle

# Scoreboard class to manage the game's score display
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()  # Initialize the Turtle class
        self.score = 0  # Start the score at 0
        self.color('white')  # Set the turtle color to white for visibility
        self.hideturtle()  # Hide the turtle shape, only use it for writing
        self.penup()  # Disable drawing when moving the turtle
        self.goto(0, 270)  # Move the turtle to the top of the screen to display the score
        self.write(f'Score: {self.score}', align='center', font=('Arial', 24, 'normal'))  # Write the initial score

    # Method to update and display the new score
    def update_score(self):
        self.score += 1  # Increment the score
        self.clear()  # Clear the previous score from the screen
        self.write(f'Score: {self.score}', align='center', font=('Arial', 24, 'normal'))  # Write the updated score

    # Method to display "Game Over" when the game ends
    def game_over(self):
        self.goto(0, 0)  # Move the turtle to the center of the screen
        self.write(f"Game Over!!!", align='center', font=('Arial', 24, 'bold'))  # Display the "Game Over" message