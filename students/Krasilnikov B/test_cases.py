import unittest
from collections import Counter

class TestCases:
    def __init__(self,text):
        self.text = text

    def word_count(self):
        words = self.text.split()
        return len(words)
        

    def unique_words(self):
        words = self.text.lower().split()
        unique = sorted(list(set(words)))
        # unique.sort(reverse=True)
        return unique
        
        
    def most_frequent_word(self):
        words = self.text.lower().split()
        if not words:
            return None
        
        word_counts = Counter(words)
        most_common = word_counts.most_common(1)[0][0]
        return most_common
        
        
        




# test = TestCases('банана абоба  абоба банана иношопотянина банана')

# test.word_count()
# test.unique_words()
# test.most_frequent_word()

class TestTestCases(unittest.TestCase):
    def setUp(self):
        self.text1 = "банана абоба абоба банана иношопотянина банана"
        self.text2 = "один"
        self.text3 = ""
        self.text4 = "   "
        self.text5 = "Слова с разным РеГиСтРоМ"
        self.text6 = "А а а Б б"
        
    def test_word_count_normal(self):
        tc = TestCases(self.text1)
        self.assertEqual(tc.word_count(), 6)
        
    def test_word_count_single_word(self):
        tc = TestCases(self.text2)
        self.assertEqual(tc.word_count(), 1)
        
    def test_word_count_empty_string(self):
        tc = TestCases(self.text3)
        self.assertEqual(tc.word_count(), 0)
        
    def test_word_count_spaces_only(self):
        tc = TestCases(self.text4)
        self.assertEqual(tc.word_count(), 0)
    
    def test_unique_words_normal(self):
        tc = TestCases(self.text1)
        expected = ['абоба', 'банана', 'иношопотянина']
        self.assertEqual(tc.unique_words(), expected)
        
    def test_unique_words_case_sensitive(self):
        tc = TestCases(self.text5)
        expected = ['разным', 'регистром', 'с', 'слова'] 
        self.assertEqual(tc.unique_words(), expected)
    
    def test_most_frequent_word_normal(self):
        tc = TestCases(self.text1)
        self.assertEqual(tc.most_frequent_word(), "банана")
        
    def test_most_frequent_word_case_sensitive(self):
        tc = TestCases(self.text6)
        self.assertEqual(tc.most_frequent_word(), "а")  # Возвращает в оригинальном регистре

if __name__ == '__main__':
    unittest.main()
