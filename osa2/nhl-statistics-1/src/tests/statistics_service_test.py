import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
		
    def test_nimi_loytyy(self):
        # Etsitään olemassaoleva pelaaja
        self.assertEqual(self.stats.search("Semenko").name, "Semenko")
        
    def test_nimea_ei_loydy(self):
        # Etsitään pelaaja, jota ei ole olemassa
        self.assertIsNone(self.stats.search("Foo"))
    
    def test_joukkue(self):
        # Varmistetaan että Kurri pelaa Edmontonissa
        result = any(plr.name == "Kurri" for plr in self.stats.team("EDM"))
        self.assertTrue(any)
        
    def test_top(self):
        # Varmistetaan että Gretzkyllä on eniten pisteitä
        result = self.stats.top(1)
        self.assertTrue(result[0].name == "Gretzky")