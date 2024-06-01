def add(*args):
    s = 0
    for n in args:
        s += n
    return s

print(add(29, 2, 100, 4))

def calculate(n, **kwargs):
    # for key, value in kwargs.items():
        # print(key)
        # print(value)
    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        # self.make = kw["make"]
        # self.model = kw["model"]

        #kw.get does not error if kw arg is missing
         self.make = kw.get("make")
         self.model = kw.get("model")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)