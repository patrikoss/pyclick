import unittest
import pytweening
from pyclick.humanclicker import HumanCurve

class TestHumanCurve(unittest.TestCase):

    def test_generateCurve(self):
        fromPoint = (100,100)
        toPoint = (1000,1000)
        hc = HumanCurve(fromPoint, toPoint)
        points = hc.generateCurve(offsetBoundaryX=10, offsetBoundaryY=50,\
            leftBoundary=10, rightBoundary=1000, \
            downBoundary=10, upBoundary=1000, \
            knotsCount=5, \
            distortionMean=10, distortionStdev=5, distortionFrequency=0.5, \
            tween=pytweening.easeOutCubic, \
            targetPoints=100)

        self.assertTrue(len(points) == 100)
        self.assertTrue(points[0] == fromPoint)
        self.assertTrue(points[-1] == toPoint)

    def test_generateInternalKnots(self):
        fromPoint = (100,100)
        toPoint = (1000,1000)
        hc = HumanCurve(fromPoint, toPoint)

        lb, rb, db, ub = 10, 20, 30, 40
        knotsCount = 5
        internalKnots = hc.generateInternalKnots(lb,rb,db,ub, knotsCount)
        self.assertTrue(len(internalKnots) == knotsCount)
        for knot in internalKnots:
            self.assertTrue(lb <= knot[0] <= rb)
            self.assertTrue(db <= knot[1] <= ub)

    def test_generatePoints(self):
        fromPoint = (99,99)
        toPoint = (100,100)
        hc = HumanCurve(fromPoint, toPoint)

        lb, rb, db, ub = 10, 20, 30, 40
        knotsCount = 5
        internalKnots = hc.generateInternalKnots(lb,rb,db,ub, knotsCount)
        points = hc.generatePoints(internalKnots)

        self.assertTrue(len(points) >= 2)
        self.assertTrue(points[0] == fromPoint)
        self.assertTrue(points[-1] == toPoint)

    def test_distortPoints(self):
        points = [(1,1), (2,1), (3,1), (4,1), (5.5,1)]
        copyPoints = [pt for pt in points]
        fromPoint, toPoint = (1,1), (2,1)
        hc = HumanCurve(fromPoint, toPoint)
        distorted = hc.distortPoints(points, 0,0,0)
        self.assertTrue(distorted == copyPoints)

    def test_tweenPoints(self):
        points = [(i,1) for i in range(100,111)]
        copyPoints = [pt for pt in points]
        fromPoint, toPoint = (1,1), (2,1)
        hc = HumanCurve(fromPoint, toPoint)

        targetPoints = 11
        tweenConstantFun = lambda x : 0.5
        tweened = hc.tweenPoints(points, tweenConstantFun, targetPoints)
        self.assertTrue(len(tweened) == targetPoints)
        self.assertTrue(tweened == [points[5] for _ in range(targetPoints)])
