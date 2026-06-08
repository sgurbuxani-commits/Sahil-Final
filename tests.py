"""Unit tests to test functionality of project.
"""

import unittest
from module import FlashcardQuiz

class TestFlashcardQuiz(unittest.TestCase):

    def test_add_flashcard(self):
        quiz = FlashcardQuiz()
        quiz.add_flashcard("2 + 3", "5", "Addition")

        self.assertEqual(len(quiz.flashcards), 1)
        self.assertEqual(quiz.flashcards[0]["answer"], "5")

    def test_filter_by_category(self):
        quiz = FlashcardQuiz()
        quiz.add_flashcard("2 + 3", "5", "Addition")
        quiz.add_flashcard("8 ÷ 2", "4", "Division")

        self.assertEqual(len(quiz.filter_by_category("Addition")), 1)

    def test_check_answer(self):
        quiz = FlashcardQuiz()

        card = {
            "question": "2 + 3",
            "answer": "5",
            "category": "Addition"
        }

        self.assertTrue(quiz.check_answer(card, "5"))
        self.assertFalse(quiz.check_answer(card, "6"))

if __name__ == "__main__":
    unittest.main()

 



                 
    