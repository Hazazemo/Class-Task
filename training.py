class Vehicle():
    def __init__(self, color):
        self.color = color
    def description(self):
        print("I'm a", self.color, "Vehicle")


class Car(Vehicle):
    def __init__(self, color, style):
        super().__init__(color)    
        self.style = style
    def description(self):
        print("I'm a", self.color, self.style)


v = Vehicle('Red')
c = Car('Black', 'SUV')
v.description()
c.description()