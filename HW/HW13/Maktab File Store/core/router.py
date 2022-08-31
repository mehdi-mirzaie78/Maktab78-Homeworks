from core.utils import clear
from importlib import import_module


class CallBack:
    """
        ...
    """

    def __init__(self, package, function, *args, **kwargs):
        self.function = getattr(import_module(package), function)
        self.args = args
        self.kwargs = kwargs

    def call(self):
        self.function(*self.args, **self.kwargs)


class Route:
    """
        ...
    """

    def __init__(self, name, description=None, callback: CallBack = None, children=None, parent=None) -> None:
        self.name = name
        self.description = description
        self.callback = callback
        self.children = children
        self.parent = parent

    def run(self):
        print(self.description) if self.description is not None else print()

        if self.parent:
            control = input('[C]: Continue\n[B]: Back\n[E]: Exit\n => ').upper()
            if control == 'C':
                pass
            elif control == 'B':
                self.parent.run()
            elif control == 'E':
                exit()
            else:
                print('Invalid Input')

        if self.callback:
            self.callback: CallBack
            self.callback.call()

        if children := self.children:
            for child in children:
                child: Route
                print(f"{children.index(child) + 1}. {child.name}")

            index = int(input("\n =>> ")) - 1
            # ...

            children[index]: Route
            children[index].run()

        if self.parent:
            control = input('[B]: Back\n[E]: Exit\n => ').upper()
            if control == 'B':
                self.parent.run()
            elif control == 'E':
                exit()
            else:
                print('Invalid Input')


class Router:
    """
        ...
    """

    def __init__(self, name: str, route: Route) -> None:
        self.name = name
        self.route = route
        if route.children:
            for child in route.children:
                child.parent = self.route

    def generate(self) -> None:
        clear()
        self.route.run()
