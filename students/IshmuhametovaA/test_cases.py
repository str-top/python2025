import unittest
from collections import Counter

def word_count(text):
    words = text.split()
    return len(words)

def unique_words(text):
    words = [word.lower() for word in text.split()]
    unique = sorted(set(words))
    return unique

def most_frequent_word(text):
    if not text.strip():
        return ''
    
    words = [word.lower() for word in text.split()]
    word_counts = Counter(words)
    max_count = max(word_counts.values())
    most_frequent = [word for word, count in word_counts.items() if count == max_count]
    return most_frequent[0] if most_frequent else ''

class TestTextFunctions(unittest.TestCase):
    def test_word_count(self):
        self.assertEqual(word_count("Hello world"), 2)
        self.assertEqual(word_count("   Hello   world   "), 2)
        self.assertEqual(word_count(""), 0)
        self.assertEqual(word_count("One"), 1)
        self.assertEqual(word_count("Multiple     spaces here"), 3)
    
    def test_unique_words(self):
        self.assertEqual(unique_words("Hi hi HI"), ['hi'])
        self.assertEqual(unique_words("apple banana Apple"), ['apple', 'banana'])
        self.assertEqual(unique_words(""), [])
        self.assertEqual(unique_words("zebra apple banana"), ['apple', 'banana', 'zebra'])
    
    def test_most_frequent_word(self):
        self.assertIn(most_frequent_word("a b a c b a"), ['a'])
        self.assertIn(most_frequent_word("x y z"), ['x', 'y', 'z'])
        self.assertEqual(most_frequent_word(""), '')
        self.assertIn(most_frequent_word("Cat cat dog DOG dog"), ['cat', 'dog'])

if __name__ == '__main__':
    unittest.main()  
