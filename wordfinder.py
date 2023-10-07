"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder:
    """
    Initializes the WordFinder with a path to a file containing words.
    Reads the file, makes a list of those words, and prints the 
    number of words read.

    Args:
        file_path (str): Path to the file containing words, one word per line.

    NOTE: Examples provided are NOT doctests since there will variability 
    based on specific file being read.

    Example: Assume you have a file at /Users/student/words.txt  or a direct path to file "words.txt" 
    within the same directory that looks like this:
    ------------
    cat
    dog
    porcupine
    ------------

    Working with your class should work like this:

    wf = WordFinder("/Users/student/words.txt")
    3 words read

    wf.random()
    'cat'

    wf.random()
    'cat'

    wf.random()
    'porcupine'

    wf.random()
    'dog'

    """

    def __init__(self, file_path):
        """
        Initializes the WordFinder with a path to a file containing words.
        Reads the file, makes a list of those words, and prints the number of words read.

        Args:
            file_path (str): Path to the file containing words, one word per line.
        """

        self.words = self.read_words(file_path)
        print(f"{len(self.words)} words read")

    def __repr__(self): 
        """Show representation."""

        return f"<SerialGenerator start={self.start} next={self.next}>"


    def read_words(self, file_path):
        """
        Reads words from a file and returns a list of those words. It also strips out empty space
        in each line with a word.

        Args:
            file_path (str): Path to the file containing words, one word per line.

        Returns:
            list: A list of words read from the file.
        """

        with open(file_path, 'r') as file:
            lines = file.readlines()
            words = [word.strip() for word in lines]
            return words

    def random(self):
        """
        Returns a random word from the list of words.

        Returns:
            str: A random word from the list of words.
        """
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):

    """Specialized WordFinder that excludes blank lines/comments.
    
        >>> swf = SpecialWordFinder("complex.txt")
        3 words read

        >>> swf.random() in ["pear", "carrot", "kale"]
        True

        >>> swf.random() in ["pear", "carrot", "kale"]
        True

        >>> swf.random() in ["pear", "carrot", "kale"]
        True
    """

    def __init__(self, file_path):
        self.words = self.read_words(file_path)
        print(f"{len(self.words)} words read")
    
    def read_words(self, file_path):
        """
        Reads words from a file and returns a parsed list of those words by excluding 
        "#" comments, empty lines and stripping space from each line.

        Args:
            file_path (str): Path to the file containing words, one word per line.

        Returns:
            list: A list of words read from the file.
        """
        words = super().read_words(file_path)

        #return statement handles hashed out comments and empty lines by removing them
        #in addition to stripping spaces from each line with the super Class
        return [word for word in words if word and not word.startswith("#")]