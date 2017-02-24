""" Thanks to the Circuits tutorial for this example"""
from circuits import Component, Debugger, Event


class woof(Event):
    pass


class Pound(Component):
    def init(self):

        self.bob = Bob().register(self)
        self.fred = Fred().register(self)

    def started(self, *args):
        self.fire(woof(), 'bob')
        self.stop()


class Dog(Component):
    def woof(self):
        print("Woof! I'm {}!".format(self.name))


class Bob(Dog):
    channel = 'bob'


class Fred(Dog):
    channel = 'fred'


if __name__ == '__main__':
    (Pound() + Debugger()).run()
