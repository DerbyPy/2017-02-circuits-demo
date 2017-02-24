from circuits import BaseComponent, Debugger, Event, handler


class hello(Event):
    pass


class Bob(BaseComponent):

    @handler('started')
    def started(self, component):
        print("Hello, World, from Bob!")


class Fred(BaseComponent):

    @handler('started')
    def started(self, component):
        print("Hello, World, from Fred!")


if __name__ == '__main__':
    (Bob() + Fred() + Debugger()).run()
