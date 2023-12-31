import unittest


class WorkerTests(unittest.TestCase):
    def test_init(self):
        worker = Worker("Test", 1000, 50)

        self.assertEqual("Test", worker.name)
        self.assertEqual(1000, worker.salary)
        self.assertEqual(50, worker.energy)

    def test_if_energy_is_incremented_after_rest(self):
        worker = Worker("Test", 1000, 50)

        worker.rest()

        self.assertEqual(51, worker.energy)

    def test_an_error_raised_for_not_valid_energy_equal_to_zero(self):
        worker = Worker("Test", 1000, 0)

        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_an_error_raised_for_negative_energy(self):
        worker = Worker("Test", 1000, -5)

        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_if_money_is_increased_by_salary_after_work_method(self):
        worker = Worker("Test", 1000, 50)

        self.assertEqual(0, worker.money)

        worker.work()

        self.assertEqual(1000, worker.money)

    def test_if_energy_is_decreased_by_one_after_work_method(self):
        worker = Worker("Test", 1000, 50)

        self.assertEqual(50, worker.energy)

        worker.work()

        self.assertEqual(49, worker.energy)

    def test_get_info_method(self):
        worker = Worker("Test", 1000, 50)

        result = worker.get_info()

        self.assertEqual(f'{worker.name} has saved {worker.money} money.', result)


if __name__ == "__main__":
    unittest.main()
