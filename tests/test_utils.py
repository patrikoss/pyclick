import unittest
import numpy as np
from pyclick._utils import isNumeric, isListOfPoints

class TestBezierCurve(unittest.TestCase):
    def test_isNumeric(self):
        self.assertTrue(isNumeric(1))
        self.assertTrue(isNumeric(1.0))
        self.assertTrue(isNumeric(np.int(0)))
        self.assertTrue(isNumeric(np.int32(0)))
        self.assertTrue(isNumeric(np.int64(0)))
        self.assertTrue(isNumeric(np.float64(2)))

    def test_isNotNumeric(self):
        self.assertFalse(isNumeric("asd"))
        self.assertFalse(isNumeric(None))
        self.assertFalse(isNumeric([]))
        self.assertFalse(isNumeric({}))
        self.assertFalse(isNumeric(set()))

    def test_isListOfPoints(self):
        self.assertTrue(isListOfPoints([]))
        self.assertTrue(isListOfPoints([
            (0, 0), (1.2, 2), (np.float32(2), np.int(0))
        ]))
        self.assertTrue([
            [1,2.0]
        ])

    def test_isNotListOfPoints(self):
        self.assertFalse(isListOfPoints("asd"))
        self.assertFalse(isListOfPoints([
            (1, 2), ("asd", 3)
        ]))
        self.assertFalse(isListOfPoints([
            [None,None]
        ]))
        self.assertFalse(
            isListOfPoints([2,2])
        )
        self.assertFalse(isListOfPoints(None))