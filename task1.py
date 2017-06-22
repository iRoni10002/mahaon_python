import math

a = int(input())
b = int(input())
c = int(input())


def korni():
    D= int()
    D= b*b - (4* a * c)
    print(D)
    if(D< 0):
        print("kornei net")
    if(D== 0):
        d = math.sqrt(D)

        print((b * (-1)) / 2 * a)
    if(D> 0):
        d = math.sqrt(D)
        print((b * (-1) + d) / (2 * a), (b * (-1) - d) / (2 * a))

korni()
