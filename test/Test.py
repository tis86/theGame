import unittest
from Hero import Hero as Character


class TestHeroMethod(unittest.TestCase):
    Character.name = "NPC"
    Character.armor = 0
    Character.health = 10
    Character.locationX = 0
    Character.locationY = 0

    def testName(self):
        self.assertEqual(Character.name, "NPC", "don`t work!")

    def testArmor(self):
        self.assertEqual(Character.armor, 0, "Don`t ok")

    def testHealth(self):
        self.assertEqual(Character.health, 10, "Don`t ok")

    def testLocationX(self):
        self.assertEqual(Character.locationX, 0, "Don`t ok")

    def testLocationY(self):
        self.assertEqual(Character.locationY, 0, "Don`t ok")
