from turtle import Turtle

FONT = ("Italic", 15, "bold")
ALIGN = "center"
WATER = 300
MILK = 100
COFFEE = 100
TEA_BAG = 2


class Database(Turtle):

    def __init__(self):
        super().__init__()
        self.resources = {
            "water": 1000,
            "milk": 1000,
            "coffee": 1000,
            "tea_bag": 100,
            "profit": 0,
        }
        self.menu = ["espresso", "latte", "tea", "cappuccino"]
        self.ingredient = {
            "espresso": {
                "ingredients": {
                    "water": 50,
                    "coffee": 18,
                },
                "cost": 1.5,
            },
            "latte": {
                "ingredients": {
                    "water": 200,
                    "milk": 150,
                    "coffee": 24,
                },
                "cost": 2.5,
            },
            "cappuccino": {
                "ingredients": {
                    "water": 250,
                    "milk": 100,
                    "coffee": 24,
                },
                "cost": 3.0,
            },
            "tea": {
                "ingredients": {
                    "water": 250,
                    "tea_bag": 1,
                },
                "cost": 1.5,
            }
        }
        self.color("white")
        self.penup()
        self.hideturtle()
        self.x = 0
        self.y = 50

    def information(self):
        self.goto(self.x, self.y)
        for i in self.menu:
            self.write(i, align=ALIGN, font=FONT)
            self.goto(self.xcor(), self.ycor() - 20)
            self.write("£" + str(self.ingredient[i]["cost"]), align=ALIGN, font=FONT)
            self.goto(self.xcor(), self.ycor() - 20)



    def resource(self):
        self.goto(0, -200)
        self.clear()
        self.write(self.resources, align=ALIGN, font=FONT)
