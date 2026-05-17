from unittest import TestCase
from main import NPC

class TestNPC(TestCase):

    def setUp(self):
        self.npcs = [
            NPC("Гаррі", 10, 100, "Торговці", False),
            NPC("Орк", 15, 200, "Монстри", True),
            NPC("Гоблін", 10, 150, "Монстри", True)
        ]

    def test_initialization(self):
        #ініц кл
        npc = NPC("Маг", 20, 80, "Люди", False)

        #пер атр об
        self.assertEqual(npc.name, "Маг")
        self.assertEqual(npc.level, 20)
        self.assertEqual(npc.health, 80)
        self.assertFalse(npc.hostile)

    def test_equality(self):
        #ств ідент об
        npc1 = NPC("Ельф", 5, 50, "Ліс", False)
        npc2 = NPC("Ельф", 5, 50, "Ліс", False)
        npc3 = NPC("Троль", 10, 300, "Гори", True)

        #пер рівн об
        self.assertEqual(npc1, npc2)
        #пер відмін об
        self.assertNotEqual(npc1, npc3)

    def test_sorting(self):
        #сорт мас об
        self.npcs.sort(key=lambda x: (x.level, -x.health))

        #очік мас рез
        expected = [
            NPC("Гоблін", 10, 150, "Монстри", True),  # рівень 10, хп 150
            NPC("Гаррі", 10, 100, "Торговці", False), # рівень 10, хп 100
            NPC("Орк", 15, 200, "Монстри", True)      # рівень 15
        ]

        #пер сорт мас
        self.assertEqual(self.npcs, expected)