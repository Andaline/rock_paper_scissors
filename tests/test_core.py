import unittest
from game.core import determine_winner

class TestGameLogic(unittest.TestCase):

    def test_determine_winner_tie(self):
        self.assertEqual(determine_winner("rock", "rock"), "It's a tie!")
        self.assertEqual(determine_winner("paper", "paper"), "It's a tie!")
        self.assertEqual(determine_winner("scissors", "scissors"), "It's a tie!")

    def test_determine_winner_player_wins(self):
        self.assertEqual(determine_winner("rock", "scissors"), "Player wins!")
        self.assertEqual(determine_winner("paper", "rock"), "Player wins!")
        self.assertEqual(determine_winner("scissors", "paper"), "Player wins!")

    def test_determine_winner_computer_wins(self):
        self.assertEqual(determine_winner("rock", "paper"), "Computer wins!")
        self.assertEqual(determine_winner("paper", "scissors"), "Computer wins!")
        self.assertEqual(determine_winner("scissors", "rock"), "Computer wins!")

if __name__ == '__main__':
    unittest.main()
