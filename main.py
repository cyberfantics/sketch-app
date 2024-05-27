# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 16:06:00 2023

@author: Mansoor
"""

import turtle as t
tim = t.Turtle()
screen = t.Screen()

def move_farward():
    tim.fd(10)

def move_backward():
    tim.bk(10)

def turn_left():
    tim.setheading(tim.heading()+10)

def turn_right():
    tim.setheading(tim.heading()-10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def hide():
    tim.penup()

def show():
    tim.pendown()
    
screen.listen()
screen.onkey(turn_left,'l')
screen.onkey(turn_right,'r')
screen.onkey(move_backward,'b')
screen.onkey(move_farward,'f')
screen.onkey(hide,'h')
screen.onkey(show,'s')
screen.onkey(clear_screen,'c')
screen.exitonclick()