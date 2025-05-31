import unittest
from src.parser import SyntaxAnalyzer
from src.lexer import LexicalAnalyzer

class TestSyntaxAnalyzer(unittest.TestCase):
    def setUp(self):
        self.lexer = LexicalAnalyzer()
        self.parser = SyntaxAnalyzer()

    def test_parse_valid_expression(self):
        text = "42 + 10"
        tokens = self.lexer.tokenize(text)
        stack = self.parser.shift_reduce_parse(tokens)
        self.assertTrue(any(t[0] == 'E' for t in stack))

    def test_parse_valid_assignment(self):
        text = "x = 42"
        tokens = self.lexer.tokenize(text)
        stack = self.parser.shift_reduce_parse(tokens)
        self.assertTrue(any(t[0] == 'E' for t in stack))

    def test_parse_invalid_expression(self):
        text = "42 + + 10"
        tokens = self.lexer.tokenize(text)
        stack = self.parser.shift_reduce_parse(tokens)
        self.assertFalse(any(t[0] == 'E' for t in stack))  # Hatalı ifade, E'ye redüklenemez

if __name__ == '__main__':
    unittest.main()