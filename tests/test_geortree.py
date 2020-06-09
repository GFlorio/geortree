from unittest import TestCase

from geortree import GeoRTree
from tests.test_coordinates import make_coordinates


class TestGeoRTree(TestCase):
    def setUp(self) -> None:
        self.tree = GeoRTree()

    def test_insert(self):
        point = make_coordinates(1)[0]
        self.tree.insert(point)
        self.assertTrue(self.tree.root.contains(point))

    def test_insert_all(self):
        points = make_coordinates(20)
        self.tree.insert_all(points)
        self.assertTrue(all(self.tree.root.contains(p) for p in points))

    def test_remove(self):
        p1, p2 = make_coordinates(2)
        self.tree.insert(p1)
        self.tree.insert(p2)
        self.tree.remove(p2)
        self.assertFalse(self.tree.root.contains(p2))

    def test_get_nearest(self):
        p1, p2, p3 = make_coordinates(3)
        nearest = p1 if p1.distance_to(p3) < p2.distance_to(p3) else p2
        self.tree.insert(p1)
        self.tree.insert(p2)

        result = self.tree.get_nearest(p3)
        self.assertEqual(result, nearest)
