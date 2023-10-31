import unittest

from project.mammal import Mammal


class TestMammal(unittest.TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal(
            "name",
            "type",
            "sound"
        )

    def test_correct_init(self):
        self.assertEqual("name", self.mammal.name)
        self.assertEqual("type", self.mammal.type)
        self.assertEqual("sound", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        result = self.mammal.make_sound()

        self.assertEqual("name makes sound", result)

    def test_get_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info(self):
        self.assertEqual("name is of type type", self.mammal.info())


if __name__ == "__main__":
    unittest.main()