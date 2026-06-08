"""Code for my project."""
import random


class FlashcardQuiz:
    """A flashcard quiz application for studying with question-answer pairs.
    
    Attributes
    ----------
    flashcards : list
        A list of dictionaries, each containing a question, answer, and category.
    """
    
    def __init__(self):
        # Initialize with an empty list to store all flashcard dictionaries
        self.flashcards = []

    def add_flashcard(self, question, answer, category="General"):
        """Add a new flashcard to the quiz deck.
        
        Parameters
        ----------
        question : str
            The question to display on the flashcard.
        answer : str
            The correct answer to the question.
        category : str, optional
            The category the flashcard belongs to. Defaults to 'General'.
            
        Raises
        ------
        TypeError
            If question, answer, or category are not strings.
        ValueError
            If question or answer are empty strings.
        """
        # Validate that all inputs are strings
        if not isinstance(question, str) or not isinstance(answer, str) or not isinstance(category, str):
            raise TypeError("Question, answer, and category must all be strings.")
        
        # Validate that question and answer are not empty or just whitespace
        if not question.strip():
            raise ValueError("Question cannot be empty.")
        if not answer.strip():
            raise ValueError("Answer cannot be empty.")
        
        # Build the flashcard as a dictionary and add to the deck
        flashcard = {
            "question": question.strip(),
            "answer": answer.strip(),
            "category": category.strip()
        }
        self.flashcards.append(flashcard)

    def filter_by_category(self, category):
        """Return all flashcards that belong to a given category.
        
        Parameters
        ----------
        category : str
            The category name to filter by (case-insensitive).
            
        Returns
        -------
        list
            A list of flashcard dictionaries matching the category.
            
        Raises
        ------
        TypeError
            If category is not a string.
        """
        # Validate input type
        if not isinstance(category, str):
            raise TypeError("Category must be a string.")
        
        # Filter cards using case-insensitive comparison
        return [
            card for card in self.flashcards
            if card["category"].lower() == category.lower()
        ]

    def get_random_card(self):
        """Return a random flashcard from the deck.
        
        Returns
        -------
        dict or None
            A randomly selected flashcard dictionary, or None if deck is empty.
        """
        # Return None early if there are no cards to choose from
        if len(self.flashcards) == 0:
            return None
        
        return random.choice(self.flashcards)

    def check_answer(self, flashcard, user_answer):
        """Check whether the user's answer matches the flashcard's correct answer.
        
        Parameters
        ----------
        flashcard : dict
            A flashcard dictionary containing at least an 'answer' key.
        user_answer : str
            The answer provided by the user.
            
        Returns
        -------
        bool
            True if the answer matches (case-insensitive), False otherwise.
            
        Raises
        ------
        TypeError
            If flashcard is not a dict or user_answer is not a string.
        KeyError
            If flashcard does not contain an 'answer' key.
        """
        # Validate flashcard is a dictionary with the expected structure
        if not isinstance(flashcard, dict):
            raise TypeError("Flashcard must be a dictionary.")
        if "answer" not in flashcard:
            raise KeyError("Flashcard must contain an 'answer' key.")
        
        # Validate user answer type
        if not isinstance(user_answer, str):
            raise TypeError("User answer must be a string.")
        
        # Compare answers after stripping whitespace and lowercasing both sides
        return flashcard["answer"].lower().strip() == user_answer.lower().strip()

    def quiz_user(self, category=None):
        """Run a single quiz round by presenting a random flashcard question.
        
        Parameters
        ----------
        category : str or None, optional
            If provided, only cards from this category will be used.
            If None, all cards are eligible. Defaults to None.
            
        Returns
        -------
        dict or str
            The flashcard dictionary that was asked, or a message string
            if no cards are available.
            
        Raises
        ------
        TypeError
            If category is provided but is not a string.
        """
        # Validate category type if one was provided
        if category is not None and not isinstance(category, str):
            raise TypeError("Category must be a string or None.")
        
        # Choose the pool of cards based on whether a category was specified
        if category:
            available_cards = self.filter_by_category(category)
        else:
            available_cards = self.flashcards
        
        # Let the caller know if there's nothing to quiz from
        if len(available_cards) == 0:
            return "No flashcards available."
        
        # Pick a random card and display the question
        card = random.choice(available_cards)
        print("Question:", card["question"])
        
        return card


        