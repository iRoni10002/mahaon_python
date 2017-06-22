import math

class Triangle:

    def __init__(self, name, color, point1, point2, point3):

        self.__name = name
        self.__color = color
        self.__point1 = point1
        self.__point2 = point2
        self.__point3 = point3

    def get_parametrs(self):
        return self.__name, self.__color, self.__point1, self.__point2, self.__point3

    def set_parametrs(self, value_name, value_color):
        self.__name = value_name
        self.__color = value_color

    def info(self):
        print('Имя:', self.__name,
              '\nЦвет:', self.__color,
              '\nТочка1:', self.__point1,
              '\nТочка2:', self.__point2,
              '\nТочка3:', self.__point3)

    def square(self):
        xy = math.sqrt(((y[0] - x[0]) * (y[0] - x[0])) + ((y[1] - x[1]) * (y[1] - x[1])))
        yz = math.sqrt(((z[0] - y[0]) * (z[0] - y[0])) + ((z[1] - y[1]) * (z[1] - y[1])))
        xz = math.sqrt(((z[0] - x[0]) * (z[0] - x[0])) + ((z[1] - x[1]) * (z[1] - x[1])))
        p = (xy + yz + xz) / 2
        return math.sqrt(p * (p - xy) * (p - yz) * (p - xz))


x = (0, 0)
y = (0, 3)
z = (3, 0)
print(x, y, z)

t1 = Triangle('tre', 'red', x, y, z)

t1.info()
print(t1.get_parametrs())
print(t1.square())
t1.set_parametrs('treugl', 'blue')
t1.info()


