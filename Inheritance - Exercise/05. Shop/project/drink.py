from project.product import Product


class Drink(Product):
    def __init__(self, name) -> None:
        super().__init__(name, 10)
        self.name = name
