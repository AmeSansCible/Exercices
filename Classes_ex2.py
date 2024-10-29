class Beverage:
    def __init__(self, name, is_alcoholic):
        self.name = name
        self.is_alcoholic = is_alcoholic

fruity = Beverage("Fruit punch", False)
cocoa = Beverage("Hot chocolate", False)

print(fruity.name)
print(cocoa.is_alcoholic)