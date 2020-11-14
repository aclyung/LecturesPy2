class Foo:
    def __init__(self, first=0, second=0):
        self.first = first
        self.second = second
        self.data()

    def data(self):
        print(self.first, self.second)


a = Foo()
b = Foo(4, 4)
