#this program draw a triangle by using  function

import turtle
turtle.speed(1)

arm_length=input("please enter your integer type value:")
arm_length=int(arm_length)

def draw_triangle(arm_length):
	turtle.forward(arm_length)
	turtle.left(120)
	turtle.forward(arm_length)
	turtle.left(120)
	turtle.forward(arm_length)
	turtle.left(120)

draw_triangle()
