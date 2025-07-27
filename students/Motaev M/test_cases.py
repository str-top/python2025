import unittest
from collections import Counter

def word_count(text):
    words = text.strip().split()
    return len(words)

def unique_words(text):
    words = text.lower().split()
    unique = sorted(set(words))
    return unique

def most_frequent_word(text):
    words = text.lower().split()
    if not words:
        return ''
    counter = Counter(words)
    max_freq = max(counter.values())
    most_common_words = [word for word, count in counter.items() if count == max_freq]
    return most_common_words[0]
  
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
        result = most_frequent_word("x y z")
        self.assertIn(result, ['x', 'y', 'z'])
        self.assertEqual(most_frequent_word(""), '')
        result = most_frequent_word("Cat cat dog DOG dog")
        self.assertIn(result, ['cat', 'dog'])

if __name__ == "__main__":
    unittest.main()
