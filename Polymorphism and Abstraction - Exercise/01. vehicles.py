from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: int, fuel_consumption: int) -> None:
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: int) -> None:
        pass

    @abstractmethod
    def refuel(self, fuel: int) -> None:
        pass


class Car(Vehicle):
    CAR_AIR_CONDITIONER_CONSUMPTION = 0.9

    def drive(self, distance: int) -> None:
        consumption = (self.fuel_consumption + Car.CAR_AIR_CONDITIONER_CONSUMPTION) * distance

        if self.fuel_quantity >= consumption:
            self.fuel_quantity -= consumption

    def refuel(self, fuel: int) -> None:
        self.fuel_quantity += fuel


class Truck(Vehicle):
    TRUCK_AIR_CONDITIONER_CONSUMPTION = 1.6
    TRUCK_HOLE = 0.95

    def drive(self, distance: int) -> None:
        consumption = (self.fuel_consumption + Truck.TRUCK_AIR_CONDITIONER_CONSUMPTION) * distance

        if self.fuel_quantity >= consumption:
            self.fuel_quantity -= consumption

    def refuel(self, fuel: int) -> None:
        self.fuel_quantity += fuel * Truck.TRUCK_HOLE


# truck = Truck(100, 15)
# truck.drive(5)
# 
# print(truck.fuel_quantity)
# truck.refuel(50)
# print(truck.fuel_quantity)
