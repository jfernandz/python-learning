class CoffeeMachine:

    def __init__(self, action):
        self.action = action
        self.money = 550
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.disposable_cups = 9
        self.coffee_type = None

    def take_action(self):
        print("Write action (buy, fill, take, remaining, exit):")
        self.action = input()

    def print_status(self):
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.beans, "of coffee beans")
        print(self.disposable_cups, "of disposable cups")
        print('${}'.format(self.money), "of money")

    def check_if_possible(self, cff_t):
        self.coffee_type = cff_t
        if self.disposable_cups < 1:
            print("Sorry, not enough disposable cups!")
            return False
        if self.coffee_type == "1":
            if self.water < 250:
                print("Sorry, not enough water!")
                return False
            elif self.beans < 16:
                print("Sorry, not enough coffee beans!")
                return False
            else:
                return True
        elif self.coffee_type == "2":
            if self.water < 350:
                print(self.water)
                print("Sorry, not enough water!")
                return False
            elif self.milk < 75:
                print("Sorry, not enough milk!")
                return False
            elif self.beans < 20:
                print("Sorry, not enough coffee beans")
                return False
            else:
                return True
        elif self.coffee_type == "3":
            if self.water < 200:
                print("Sorry, not enough water!")
                return False
            elif self.milk < 100:
                print("Sorry, not enough milk!")
                return False
            elif self.beans < 12:
                print("Sorry, not enough coffee beans!")
                return False
            else:
                return True
        elif self.coffee_type == "back":
            return None

    def buy(self):
        if self.coffee_type == "1":
            self.water -= 250
            self.beans -= 16
            self.money += 4
            self.disposable_cups -= 1
        elif self.coffee_type == "2":
            self.water -= 350
            self.milk -= 75
            self.beans -= 20
            self.money += 7
            self.disposable_cups -= 1
        elif self.coffee_type == "3":
            self.water -= 200
            self.milk -= 100
            self.beans -= 12
            self.money += 6
            self.disposable_cups -= 1
        else:
            print("Not coffee type found.")

    def fill(self):
        print("Write how many ml of water do you want to add:")
        self.water += int(input())
        print("Write how many ml of milk do you want to add:")
        self.milk += int(input())
        print("Write how many grams of coffee beans do you want to add:")
        self.beans += int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        self.disposable_cups += int(input())

    def take(self):
        print("I gave you", '${}'.format(self.money))
        self.money = 0


coffee_machine = CoffeeMachine("Starting")

while coffee_machine.action != "exit":
    coffee_machine.take_action()

    if coffee_machine.action == "buy":
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        coffee_t = str(input())
        coffee_machine.check_if_possible(coffee_t)
        if coffee_machine.coffee_type == "back":
            continue
        else:
            if coffee_machine.check_if_possible(coffee_t):
                print("I have enough resources, making you a coffee!")
                coffee_machine.buy()
    elif coffee_machine.action == "fill":
        coffee_machine.fill()
    elif coffee_machine.action == "take":
        coffee_machine.take()
    elif coffee_machine.action == "remaining":
        coffee_machine.print_status()
    else:
        pass

