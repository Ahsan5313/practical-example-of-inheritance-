class shape:
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    def  area(self):
        print("I am area method of shape class")


class trinagle(shape):
    def  area(self):
        area = 0.5 * self.dim1 * self.dim2
        print("Area of trinagle :", area)


class ractangle(shape):
    def  area(self):
        area =  self.dim1 * self.dim2
        print("Area of ractangle :", area)


t1 = trinagle(20, 10)
t1.area()

r1 = ractangle(20, 10)
r1.area()



