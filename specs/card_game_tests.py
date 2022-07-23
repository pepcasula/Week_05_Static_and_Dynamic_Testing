import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card_1 = Card("spades", 7)
        self.card_2 = Card("hearts", 9)
        self.easy_blackjack = CardGame(self.card_1.value, self.card_2.value)

    def test_check_for_ace(self):
        self.assertEqual(False, self.card_1.check_for_ace())
    
    def test_highest_card(self):
        self.assertEqual(9, self.easy_blackjack.highest_card())

    def test_card_total(self):
        self.assertEqual("You have a total of 16", self.easy_blackjack.cards_total()) 

