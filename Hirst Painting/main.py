# import colorgram
# rgb_colors = []
# colors = colorgram.extract('hirst painting.jfif', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print (rgb_colors)
import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
color_list = [(173, 79, 34), (240, 224, 82), (47, 35, 25), (213, 152, 86), (22, 25, 66), (146, 27, 40), (44, 44, 118), (164, 22, 16), (53, 87, 151), (126, 161, 216), (206, 86, 127), (151, 53, 85), (27, 42, 28), (213, 81, 63), (142, 182, 143), (115, 107, 197), (65, 31, 36), (78, 117, 61), (197, 128, 158), (82, 87, 32), (202, 140, 44), (152, 211, 189), (161, 179, 230), (87, 154, 107), (249, 223, 1), (61, 147, 169)]

tim.penup()
tim.hideturtle()
tim.setheading(220)
tim.pensize(0)
tim.speed("fastest")
tim.forward(300)
tim.setheading(0)

number_of_dots = 100

for dot_count in range (1, number_of_dots +1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)





screen = turtle_module.Screen()
screen.exitonclick()
