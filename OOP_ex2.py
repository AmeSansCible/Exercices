class CoffeeMachine:
    def __init__(self):
        self.coffee_options = {"Capuccino", "Espresso"}

    def make_coffee(self, coffee_type):
        is_valid_coffee_type = coffee_type in self.coffee_options
        if is_valid_coffee_type:
            return f"{coffee_type} made!"
        else:
            return f"{coffee_type} is not a valid option!"


machine = CoffeeMachine()
print(machine.make_coffee("Espresso"))
print(machine.make_coffee("Moka"))