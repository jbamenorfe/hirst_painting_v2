import turtle as t
import random

color_list = [(181, 171, 162), (208, 195, 163), (164, 177, 184), (186, 176, 179), (151, 81, 55), (157, 179, 162), (46, 106, 127), (56, 122, 92), (216, 180, 174), (171, 150, 53), (133, 73, 82), (132, 33, 26), (210, 180, 185), (146, 23, 30), (197, 96, 74), (69, 45, 34), (17, 94, 73), (177, 200, 186), (102, 146, 109), (75, 148, 166), (23, 60, 79), (186, 190, 199), (60, 41, 47), (15, 87, 99), (191, 81, 89), (171, 200, 206)]

tim = t.Turtle()
t.colormode(255)
x_position = -200.00
y_position = -200.00
tim.penup()     # Ensure that tim doesn't draw any line while positioning it
tim.setpos((x_position,y_position))     # Position tim on the first row
for dot_x in range(10):
    for dot_y in range (10):
        chosen_color = random.choices(color_list)
        tim.color(chosen_color)
        tim.pensize(10)
        tim.dot()
        tim.penup()
        tim.forward(50)
        y_position += 5     # Send the turtle to next row (above the previous row)
    tim.setpos(x_position, y_position)

screen = t.Screen()
screen.exitonclick()