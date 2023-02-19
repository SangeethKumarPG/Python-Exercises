import colorgram
import random
from turtle import Turtle,Screen

colors = colorgram.extract('lysergic.jpg',50)
list_of_colors_rgb = []
for color in colors:
    # list_of_colors_rgb.append(color.rgb)
    red = color.rgb[0]
    green = color.rgb[1]
    blue = color.rgb[2]
    # if red < 230 and green < 230 and blue < 230: 
    #     list_of_colors_rgb.append((red,green,blue))
    list_of_colors_rgb.append((red,green,blue))

print(list_of_colors_rgb)

# [(196, 9, 68), (212, 155, 90), (19, 117, 174), (168, 169, 27), (107, 180, 209), (218, 131, 166), (163, 74, 30), (5, 35, 87), (26, 139, 72), (124, 181, 142), (219, 76, 122), (82, 17, 80), (175, 47, 90), (9, 59, 35), (12, 166, 213), (126, 33, 21), (9, 44, 130), (52, 164, 114), (4, 104, 63), (4, 88, 99), (142, 209, 220), (100, 31, 13)]

tim = Turtle()
screen = Screen()
screen.colormode(255)
# screen.setup(width = 300, height = 300)
tim.penup()
tim.hideturtle()
# tim.setx(-100)
# tim.sety(-100)
# tim.dot(20,random.choice(list_of_colors_rgb))
# tim.forward(50)

# tim.setx(-8)
# tim.sety(-8)
# tim.dot(20,random.choice(list_of_colors_rgb))
for i in range(-250,250,50):
    tim.sety(i)
    for j in range(-250,250,50):
        tim.penup()
        tim.setx(j)
        tim.dot(20,random.choice(list_of_colors_rgb))
        tim.forward(50)

screen.exitonclick()

