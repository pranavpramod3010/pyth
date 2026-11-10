class Vehicle:
    def __init__(self, name, speed, mileage):
        self.name = name
        self.max_speed = speed
        self.mileage = mileage

vehicle1 = Vehicle("BMW",320, 10)
print(Vehicle Name: {vehicle1.name}, Speed: {vehicle1.speed}, Mileage: {vehicle1.mileage})





class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(self.length * self.width)

    def perimeter(self):
        print(2*(self.length+self.width))

Rectangle1=Rectangle(10,5)    
Rectangle1.area()
Rectangle1.perimeter()







