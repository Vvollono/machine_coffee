from turtle import Screen
from new_database import Database
from machine_function import Function

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Coffe Machine")
screen.tracer(0)
menu = Database()
function = Function()
is_on = True

menu.information()
function.order()













screen.exitonclick()
