import unittest


class CatTests(unittest.TestCase):
    def test_init(self):
        cat = Cat("Mac")

        self.assertEqual("Mac", cat.name)
        self.assertFalse(cat.fed)
        self.assertFalse(cat.sleepy)
        self.assertEqual(0, cat.size)

    def test_if_cat_size_is_increased_after_eating(self):
        cat = Cat("Mac")

        cat.eat()

        self.assertEqual(1, cat.size)

    def test_if_the_cat_is_fed_after_eating(self):
        cat = Cat("Mac")

        cat.eat()

        self.assertTrue(cat.fed)

    def test_cat_cannot_eat_if_already_fed(self):
        cat = Cat("Mac")

        cat.eat()

        with self.assertRaises(Exception) as ex:
            cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

        self.assertTrue(cat.fed)
        self.assertTrue(cat.sleepy)

    def test_cat_cannot_sleep_if_not_fed(self):
        cat = Cat("Mac")

        self.assertFalse(cat.fed)
        self.assertFalse(cat.sleepy)

        with self.assertRaises(Exception) as ex:
            cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))
        self.assertFalse(cat.fed)
        self.assertFalse(cat.sleepy)

    def test_cat_is_not_sleepy_after_sleeping(self):
        cat = Cat("Mac")

        cat.eat()
        self.assertTrue(cat.fed)
        self.assertTrue(cat.sleepy)

        cat.sleep()

        self.assertFalse(cat.sleepy)


if __name__ == "__main__":
    unittest.main()
