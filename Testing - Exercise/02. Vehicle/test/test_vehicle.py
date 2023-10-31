import unittest

from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(50.5, 150.5)

    def test_check_class_attribute(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_correct_init(self):
        self.assertEqual(50.5, self.vehicle.fuel)
        self.assertEqual(50.5, self.vehicle.capacity)
        self.assertEqual(150.5, self.vehicle.horse_power)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive_with_not_enough_fuel(self):
        self.vehicle.fuel = 0

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_with_enough_fuel_and_decrease(self):
        self.vehicle.drive(1)

        self.assertEqual(49.25, self.vehicle.fuel)

    def test_refuel_with_no_capacity_left(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(60)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_with_enough_capacity(self):
        self.vehicle.fuel -= 1
        self.vehicle.refuel(1)

        self.assertEqual(50.5, self.vehicle.fuel)

    def test_str_method(self):
        result = str(self.vehicle)

        expected = "The vehicle has 150.5 " \
                   "horse power with 50.5 fuel left and 1.25 fuel consumption"

        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()


