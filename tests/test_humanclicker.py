import unittest
from pyclick.humanclicker import HumanClicker
import pyautogui
import random

class TestHumanClicker(unittest.TestCase):

    def test_simple(self):
        width, height = pyautogui.size()
        toPoint = (width//2, height//2)
        hc = HumanClicker()
        hc.move(toPoint)
        self.assertTrue(pyautogui.position() == toPoint)

    def test_identityMove(self):
        toPoint = pyautogui.position()
        hc = HumanClicker()
        hc.move(toPoint)
        self.assertTrue(pyautogui.position() == toPoint)

    def test_randomMove(self):
        width, height = pyautogui.size()
        toPoint = random.randint(width//2,width-1), random.randint(height//2,height-1)
        hc = HumanClicker()
        hc.move(toPoint)
        self.assertTrue(pyautogui.position() == toPoint)

