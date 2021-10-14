from new_database import Database
from turtle import Turtle, Screen

menu = Database()
FONT = ("Italic", 15, "bold")
ALIGN = "center"
screen = Screen()


class Function(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.is_on = True
        self.credit = 0
        self.change = 0

    def order(self):
        while self.is_on:
            self.choice = screen.textinput(title="Order", prompt="What drink do you like? ")
            if self.choice == "off":
                self.is_on = False
                self.is_enough = False
            elif self.choice == "report":
                menu.resource()
            else:
                self.resource_check()

    def display(self):
        self.clear()
        self.goto(0, 250)
        self.write(f"Enjoy your {self.choice}, Here is your change {self.change}", align=ALIGN, font=FONT)
        self.order()


    def empty(self, i):
        self.clear()
        self.goto(0, 250)
        self.write(f"Sorry not enough {i}", align=ALIGN, font=FONT)

    def money(self):
        self.insert = float(screen.textinput(title="Order", prompt="Please insert money "))
        self.insert += self.credit
        if self.insert >= menu.ingredient[self.choice]["cost"]:
            menu.resources["profit"] += self.insert

            if self.insert > menu.ingredient[self.choice]["cost"]:
                self.change = self.insert - menu.ingredient[self.choice]["cost"]
                menu.resources["profit"] -= self.change

            self.display()


        elif self.insert < menu.ingredient[self.choice]["cost"]:
            self.clear()
            self.goto(0, 250)
            self.write(f"{self.insert} £ not enough money", align=ALIGN, font=FONT)
            self.credit = self.insert

    def resource_check(self):
        self.is_enough = True
        for i in menu.menu:
            if self.choice == i:

                while self.is_enough:
                    for i in menu.resources:
                        if i in menu.ingredient[self.choice]["ingredients"]:
                            if menu.resources[i] < menu.ingredient[self.choice]["ingredients"][i]:
                                self.empty(i)
                                self.is_enough = False
                                self.order()
                            elif menu.resources[i] >= menu.ingredient[self.choice]["ingredients"][i]:
                                menu.resources[i] -= menu.ingredient[self.choice]["ingredients"][i]
                    self.money()
