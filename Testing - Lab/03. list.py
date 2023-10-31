import unittest


class TestIntegerList(unittest.TestCase):
    def test_add_element_to_the_list(self):
        integer_list = IntegerList(1, 2, 3)

        self.assertEqual(3, len(integer_list.get_data()))

    def test_not_int_are_added(self):
        integer_list = IntegerList(1, 2, 3.5)

        self.assertEqual(2, len(integer_list.get_data()))
        self.assertEqual([1, 2], integer_list.get_data())

    def test_get_data(self):
        integer_list = IntegerList(1, 2, 3)

        self.assertEqual([1, 2, 3], integer_list.get_data())

    def test_add_method_not_int_raises(self):
        integer_list = IntegerList(1, 2, 3)

        self.assertEqual(3, len(integer_list.get_data()))

        test_data = [3.4, False, [], {}, "asd"]

        for value in test_data:
            with self.assertRaises(ValueError) as ex:
                integer_list.add(value)

            self.assertEqual("Element is not Integer", str(ex.exception))

    def test_add_method_add_int(self):
        integer_list = IntegerList(1, 2, 3)

        self.assertEqual(3, len(integer_list.get_data()))

        integer_list.add(4)

        self.assertEqual(4, len(integer_list.get_data()))

    def test_remove_index_invalid_index_raises(self):
        integer_list = IntegerList(1, 2, 3)

        self.assertEqual(3, len(integer_list.get_data()))

        with self.assertRaises(IndexError) as ex:
            integer_list.remove_index(5)

        self.assertEqual("Index is out of range", str(ex.exception))

        self.assertEqual(3, len(integer_list.get_data()))

    def test_remove_element(self):
        integer_list = IntegerList(1, 2, 3)

        self.assertEqual(3, len(integer_list.get_data()))

        self.assertEqual(1, integer_list.get_data()[0])
        res = integer_list.remove_index(0)

        self.assertEqual(1, res)

        self.assertEqual(2, len(integer_list.get_data()))
        self.assertEqual(2, integer_list.get_data()[0])

    def test_get_invalid_index_raises(self):
        integer_list = IntegerList(1, 2, 3)

        self.assertEqual(3, len(integer_list.get_data()))

        with self.assertRaises(IndexError) as ex:
            integer_list.get(4)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_by_index(self):
        integer_list = IntegerList(1, 2, 3)

        self.assertEqual(3, len(integer_list.get_data()))

        el = integer_list.get(1)
        self.assertEqual(2, el)

    def test_insert_invalid_inx_raises(self):
        integer_list = IntegerList(1, 2, 3)

        self.assertEqual(3, len(integer_list.get_data()))

        with self.assertRaises(IndexError) as ex:
            integer_list.insert(4, 5)

        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual(3, len(integer_list.get_data()))

    def test_insert_element_not_int_raises(self):
        integer_list = IntegerList(1, 2, 3)
        self.assertEqual(3, len(integer_list.get_data()))

        with self.assertRaises(ValueError) as ex:
            integer_list.insert(0, 5.6)

        self.assertEqual("Element is not Integer", str(ex.exception))

        self.assertEqual(3, len(integer_list.get_data()))

    def test_insert(self):
        integer_list = IntegerList(1, 2, 3)

        self.assertEqual(3, len(integer_list.get_data()))
        self.assertEqual([1, 2, 3], integer_list.get_data())
        self.assertEqual([1, 2, 3], integer_list._IntegerList__data)

        integer_list.insert(0, 100)
        self.assertEqual(4, len(integer_list.get_data()))
        self.assertEqual([100, 1, 2, 3], integer_list.get_data())
        self.assertEqual([100, 1, 2, 3], integer_list._IntegerList__data)

    def test_get_biggest(self):
        integer_list = IntegerList(0, 12, -3)

        result = integer_list.get_biggest()
        self.assertEqual(12, result)

    def test_get_index(self):
        integer_list = IntegerList(1, 2, 3)

        self.assertEqual(integer_list.get_data()[0], 1)

        result = integer_list.get_index(1)
        self.assertEqual(0, result)


if __name__ == "__main__":
    unittest.main()
