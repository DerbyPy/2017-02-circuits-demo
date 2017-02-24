from time import sleep

from circuits import task, Worker
from circuits import Component, Debugger, Event, Timer


def factorial(n):
    x = 1
    for i in range(1, (n + 1)):
        x = x * (i + 1)

        # sleep a bit, or else we'll finish before the first "foo" event
        sleep(0.5)
    return x


class App(Component):

    def init(self, *args, **kwargs):
        Worker(process=True).register(self)

    def foo(self):
        print("Foo!")

    def started(self, component):
        # every second, fire a "foo" event
        Timer(1, Event.create("foo"), persist=True).register(self)

        # wait this method for a task
        x = yield self.call(task(factorial, 10))
        print(x.__class__.__name__)

        # resume execution, and print the result
        print("{0:d}".format(x.value))
        self.stop()


if __name__ == '__main__':
    app = App()
    Debugger().register(app)
    app.run()
