from core.utils import clear
from importlib import import_module
from core.utils import logger


class CallBack:
    """
        ...
    """

    def __init__(self, package, function, *args, **kwargs):
        self.function = getattr(import_module(package), function)
        self.args = args
        self.kwargs = kwargs

    def call(self):
        return self.function(*self.args, **self.kwargs)


class Route:
    """
        ...
    """

    def __init__(self, name, description=None, callback: CallBack = None, children=None, parent=None,
                 result=(None,)) -> None:
        self.name = name
        self.description = description
        self.callback = callback
        self.children = children
        self.parent = parent
        self.result = result

    def run(self):
        try:
            clear()
            print(f'-> {self.description}') if self.description is not None else print()

            if self.parent:
                print(f'--> {self.name}\n')
                print(f'[P]: Proceed to {self.name}\n[B]: Back to {self.parent.name}\n[E]: Exit')
                control = input('\n => ').upper()
                print('---------------------------')
                if control == 'P':
                    pass
                elif control == 'B':
                    self.parent.run()
                elif control == 'E':
                    exit()
                else:
                    raise ValueError('Invalid Input')
                clear()
            if self.callback:
                clear()
                self.callback: CallBack
                self.result = self.callback.call()

            if children := self.children:
                print(f'-> {self.name}\n')
                for child in children:
                    child.parent = self
                    if child.callback:
                        child.callback.args = (self.result,)
                    child: Route
                    print(f"{children.index(child) + 1}. {child.name}")
                print("[B]: Back") if self.name != 'Main Menu' else None
                index = input("\n =>> ").upper()
                # ...
                if index == 'B' and self.name != 'Main Menu':
                    self.parent.run()
                elif not index.isnumeric():
                    raise ValueError("Invalid Input In Main Menu")
                index = int(index) - 1
                children[index]: Route
                children[index].run()

            if self.parent:
                control = input(f'[B]: Back to {self.parent.name}\n[E]: Exit\n => ').upper()
                if control == 'B':
                    self.parent.run()
                elif control == 'E':
                    exit()
                else:
                    raise ValueError('Invalid Input')
        except Exception as error:
            print(f'\nERROR: {error}\n')
            logger.error(error)

            self.run()


class Router:

    def __init__(self, name: str, route: Route) -> None:
        self.name = name
        self.route = route
        if route.children:
            for child in route.children:
                child.parent = self.route

    def generate(self) -> None:
        clear()
        self.route.run()
