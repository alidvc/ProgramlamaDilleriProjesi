import unittest
from src.lexer import LexicalAnalyzer

class TestLexicalAnalyzer(unittest.TestCase):
    def setUp(self):
        self.lexer = LexicalAnalyzer()

    def test_tokenize_valid_input(self):
        text = "if x = 42 + 10 // comment"
        expected = [
            ('KEYWORD', 'if', 0),
            ('IDENTIFIER', 'x', 3),
            ('OPERATOR', '=', 5),
            ('NUMBER', '42', 7),
            ('OPERATOR', '+', 10),
            ('NUMBER', '10', 12),
            ('COMMENT', '// comment', 15)
        ]
        tokens = self.lexer.tokenize(text)
        self.assertEqual(tokens, expected)

    def test_tokenize_invalid_input(self):
        text = "if x = @"
        with self.assertRaises(ValueError) as cm:
            self.lexer.tokenize(text)
        self.assertEqual(str(cm.exception), "Geçersiz karakter at pozisyon 7: @")

    def test_tokenize_empty_input(self):
        text = ""
        tokens = self.lexer.tokenize(text)
        self.assertEqual(tokens, [])

    def test_tokenize_whitespace(self):
        text = "  \n\t  "
        tokens = self.lexer.tokenize(text)
        self.assertEqual(tokens, [])

if __name__ == '__main__':
    unittest.main()