from random import uniform
from unittest import TestCase

from geortree.coordinates import Coordinates, Rectangle


def make_coordinates(n):
    return [Coordinates(uniform(-20, 20), uniform(-40, 40)) for _ in range(n)]


class Test(TestCase):
    def test_coordinates_distance(self):
        coord1, coord2 = make_coordinates(2)
        distance = coord1.distance_to(coord2)
        self.assertTrue(distance > 0)

    def test_rectangle_enclosing(self):
        sw = Coordinates(0, 0)
        ne = Coordinates(1, 1)
        rectangle = Rectangle.enclosing([sw, ne])
        self.assertEqual(sw, rectangle.sw)
        self.assertEqual(ne, rectangle.ne)

    def test_rectangle_area(self):
        rectangle = Rectangle.enclosing(make_coordinates(5))
        self.assertTrue(rectangle.area() > 0)
        sw = Coordinates(-21, -61)
        ne = Coordinates(21, 61)
        large_rectangle = Rectangle(sw, ne)
        self.assertTrue(large_rectangle.area() > rectangle.area())

    def test_rectangle_contains(self):
        points = make_coordinates(5)
        rectangle = Rectangle.enclosing(points)
        self.assertTrue(all(rectangle.contains(p) for p in points))
        self.assertTrue(rectangle.contains(rectangle.sw))
        self.assertTrue(rectangle.contains(rectangle.ne))
        self.assertFalse(rectangle.contains(Coordinates(80, 120)))

    def test_rectangle_distance(self):
        interior = make_coordinates(5)
        rect = Rectangle.enclosing(interior)
        point = make_coordinates(1)[0]
        self.assertTrue(all(rect.distance_to_point(p) == 0 for p in interior))

        # Compare distances in 'km' because of rounding and approximation errors.
        self.assertLessEqual(rect.distance_to_point(point)//1000,
                             rect.sw.distance_to(point)//1000)
        self.assertLessEqual(rect.distance_to_point(point)//1000,
                             rect.ne.distance_to(point)//1000)
