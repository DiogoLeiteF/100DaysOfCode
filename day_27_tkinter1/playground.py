def add(*args):
    s = 0
    for i in args:
        s += i
    return s


print(add(1, 2, 3, 4, 5))


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    if kwargs.get("multiply"):
        n *= kwargs.get("multiply")
    print(n)


# .get() to avoid the error

calculate(2, add=3)


class Car():
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")


my_car = Car(make="Nissan")

print(my_car.model)
