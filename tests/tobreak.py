import unittest
from tobuild import count_words, pascals_triangle_row, calculator, reverse_words, factorial

class TestBreakItTillYouMakeIt(unittest.TestCase):
    # COUNT WORDS
    def test_count_words_basic(self):
        self.assertEqual(count_words("Hello, hello world"), {"hello":2, "world":1})
        self.assertEqual(count_words("Hi! Hi, hi."), {"hi":3})
    
    # PASCAL TRIANGLE
    def pascals_triangle_row(self):
        self.assertEqual(pascals_triangle_row(0), [1])
        self.assertEqual(pascals_triangle_row(4), [1,4,6,4,1])
    
    #cALCULATOR
    def test_calculator(self):
        self.assertEqual(calculator(5,5, "+"), 10) 
        self.assertEqual(calculator(5,1, "-"), 4) 
        self.assertEqual(calculator(5,5, "*"), 25) 
        self.assertEqual(calculator(15,5, "/"), 3) 
        with self.assertRaises(ValueError):
            calculator(5,0, "/")
    
    #Reverse Words
    def test_reverse_words(self):
        self.assertEqual(reverse_words("the quick brown fox"), "fox brown quick the")
        self.assertEqual(reverse_words("hello"), "hello")
    
    # FACTORIAL
    def test_factorial(self):
        with self.assertRaises(ValueError):
            factorial(-1)
        
if __name__ == "__main__":
    unittest.main()