class Mario():
    def move(self):
        print("i m moving")

class Mushroom():
    def eat_mushroom(self):
        print("i m big")

class BigMario(Mario,Mushroom):
    pass#prevents errors,whenever we want to write something just for preventing syntax errores just write pass..it dont do anything


b=BigMario()
b.move()
b.eat_mushroom()

