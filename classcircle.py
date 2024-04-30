import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def cal_area(self):
        return math.pi * (self.radius ** 2)


radius = 5
circle = Circle(radius)
print(get_radius())
print(cal_area())
