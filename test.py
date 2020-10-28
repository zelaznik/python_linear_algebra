from vector import Vector
import unittest

class DotProductTest(unittest.TestCase):
    def test_when_vectors_have_unequal_length(self):
        first = Vector([1, 2, 3])
        second = Vector([1, 2, 3, 4])
        with self.assertRaises(ValueError):
            first.dot(second)

    def test_it_does_a_sum_product(self):
        first = Vector([1, 2, 3])
        second = Vector([10, 11, 12])
        self.assertEqual(first.dot(second), 68)

class AbsoluteValueTest(unittest.TestCase):
    def test_it_equals_sum_of_elements_squared(self):
        v = Vector([3, 4, 12])
        self.assertEqual(abs(v), 13)

class GetItemTest(unittest.TestCase):
    def test_when_index_less_than_zero(self):
        v = Vector([2, 7, 1, 8])
        with self.assertRaises(IndexError):
            v[-1]

    def test_it_returns_nth_item_of_vector(self):
        v = Vector([2, 7, 1, 8])
        self.assertEqual(v[1], 7)

class IterationTest(unittest.TestCase):
    def test_that_it_converts_to_a_list(self):
        v = Vector([2, 7, 1, 8])
        self.assertEqual(list(v), [2, 7, 1, 8])

class LengthTest(unittest.TestCase):
    def test_it_returns_the_number_of_items(self):
        v = Vector([2, 7, 1, 8])
        self.assertEqual(len(v), 4)

class MultiplcationTest(unittest.TestCase):
    def test_when_other_item_is_vector(self):
        a = Vector([1, 0])
        b = Vector([0, 1])
        with self.assertRaises(TypeError):
            a * b

    def test_multiplies_all_elements_by_scalar(self):
        v = Vector([3, 4])
        self.assertEqual(list(v * 10), [30, 40])

    def test_when_number_comes_before_vector(self):
        v = Vector([3, 4])
        self.assertEqual(list(10*v), [30, 40])

class DivisionTest(unittest.TestCase):
    def test_divides_all_elements_by_scalar(self):
        v = Vector([30, 40])
        self.assertEqual(list(v / 10), [3, 4])

    def test_when_number_divided_by_vector(self):
        v = Vector([30, 40])
        with self.assertRaises(TypeError):
            10 / v

class NormalizedTest(unittest.TestCase):
    def test_divides_all_elements_by_absolute_value(self):
        v = Vector([3, 4])
        self.assertEqual(list(v.normalized()), [0.6, 0.8])

class ProjectionOntoTest(unittest.TestCase):
    def test_returns_zero_vector_when_vectors_are_perpindicular(self):
        a = Vector([1, 1])
        b = Vector([1, -1])
        self.assertEqual(list(a.projection_onto(b)), [0, 0])

    def test_returns_original_vector_when_vectors_are_parallel(self):
        a = Vector([1, 1])
        b = Vector([-20, -20])
        self.assertEqual(list(a.projection_onto(b)), [1, 1])

    def test_scales_down_vector_by_cosine_of_angle(self):
        a = Vector([1, 2])
        b = Vector([20, 10])
        self.assertEqual(list(a.projection_onto(b)), [1.6, 0.8])

class AdditionTest(unittest.TestCase):
    def test_raises_error_when_vectors_have_unequal_length(self):
        first = Vector([1, 2, 3])
        second = Vector([1, 2, 3, 4])
        with self.assertRaises(ValueError):
            first + second

    def test_adds_each_of_the_elements_togeter(self):
        a = Vector([1, 2, 3, 4])
        b = Vector([30, 33, 36, 39])
        self.assertEqual(list(a + b), [31, 35, 39, 43])

class SubtracitonTest(unittest.TestCase):
    def test_raises_error_when_vectors_have_unequal_length(self):
        first = Vector([1, 2, 3])
        second = Vector([1, 2, 3, 4])
        with self.assertRaises(ValueError):
            first - second

    def test_adds_each_of_the_elements_togeter(self):
        a = Vector([1, 2, 3, 4])
        b = Vector([31, 35, 39, 43])
        self.assertEqual(list(b - a), [30, 33, 36, 39])

if __name__ == '__main__':
    unittest.main()
