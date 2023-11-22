import unittest
from Poker import flush, paar


class TestCardFunctions(unittest.TestCase):
    def setUp(self):
        # You can set up any necessary variables or configurations here
        pass

    def test_paar(self):
        # Test for the pair function
        # You can create specific test cases to cover different scenarios

        # Test case 1: Test when there is a pair in the selected cards
        selected_cards = [1, 2, 3, 4, 14]
        cards_per_suit = 13
        self.assertTrue(paar(selected_cards, cards_per_suit))

        # Test case 2: Test when there is no pair in the selected cards
        selected_cards = [1, 2, 3, 4, 5]
        cards_per_suit = 13
        self.assertFalse(paar(selected_cards, cards_per_suit))

    def test_flush(self):
        # Test for the flush function
        # You can create specific test cases to cover different scenarios

        # Test case 1: Test when there is a flush in the selected cards
        selected_cards = [1, 3, 7, 9, 5]
        cards_per_suit = 13
        self.assertTrue(flush(selected_cards, cards_per_suit))

        # Test case 2: Test when there is no flush in the selected cards
        selected_cards = [1, 14, 51, 4, 13]
        cards_per_suit = 13
        self.assertFalse(flush(selected_cards, cards_per_suit))

if __name__ == '__main__':
    unittest.main()
