import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card_1 = Card("spades", 7)
        self.card_2 = Card("hearts", 9)
        self.cards = [self.card_1, self.card_2]

    def test_check_for_ace(self):
        ace_check = CardGame.check_for_ace(self.card_1)
        self.assertEqual(False, ace_check)
    
    def test_highest_card(self):
        highest_check = CardGame.highest_card(self.cards)    
        self.assertEqual("The highest card is 9 of hearts.", highest_check)

    def test_card_total(self):
        total_check = CardGame.cards_total(self.cards)
        self.assertEqual("You have a total of 16", total_check) 