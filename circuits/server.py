from circuits.web import Controller, Server


class Root(Controller):
    def index(self):
        return "Hello World!"


if __name__ == '__main__':
    app = Server(("0.0.0.0", 8000))
    Root().register(app)
    app.run()
