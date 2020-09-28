class Person:
    def __init__(self, name, age):  # constructor
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


if __name__ == "__main__":
    p1 = Person("John", 36)
    p1.myfunc()
