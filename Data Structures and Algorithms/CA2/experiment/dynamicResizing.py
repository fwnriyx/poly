import turtle
import random
import time

# Function to draw a bar for each element in the list
def draw_bar(height, x, color="blue"):
    turtle.penup()
    turtle.goto(x, -150)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.end_fill()

# Function to redraw the entire list
def draw_list(lst):
    turtle.clear()
    for i, value in enumerate(lst):
        draw_bar(value, i * 30)

# Bubble Sort Algorithm
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                draw_list(lst)
                time.sleep(0.2)  # Adjust the speed of visualization

# Main function
def main():
    turtle.speed(100)  # Set the turtle speed to the maximum
    turtle.hideturtle()

    # Create a random list of heights for bars
    random.seed(42)  # Set seed for reproducibility
    data = [random.randint(10, 150) for _ in range(10)]

    # Draw the initial state of the list
    draw_list(data)

    # Perform Bubble Sort and visualize the process
    bubble_sort(data)

    turtle.done()

if __name__ == "__main__":
    main()
