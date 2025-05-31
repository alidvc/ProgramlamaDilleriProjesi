import unittest
import tkinter as tk
from src.highlighter import Highlighter

class TestHighlighter(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.text_widget = tk.Text(self.root)
        self.highlighter = Highlighter(self.text_widget)

    def tearDown(self):
        self.root.destroy()

    def test_highlight_tokens(self):
        tokens = [
            ('KEYWORD', 'if', 0),
            ('IDENTIFIER', 'x', 3),
            ('OPERATOR', '=', 5),
            ('NUMBER', '42', 7)
        ]
        self.text_widget.insert("1.0", "if x = 42")
        self.highlighter.highlight(tokens)

        # Tag'lerin doğru uygulandığını kontrol et
        self.assertEqual(self.text_widget.tag_names("1.0"), ('KEYWORD',))
        self.assertEqual(self.text_widget.tag_names("1.3"), ('IDENTIFIER',))
        self.assertEqual(self.text_widget.tag_names("1.5"), ('OPERATOR',))
        self.assertEqual(self.text_widget.tag_names("1.7"), ('NUMBER',))

    def test_highlight_clear_previous(self):
        tokens = [('KEYWORD', 'if', 0)]
        self.text_widget.insert("1.0", "if")
        self.highlighter.highlight(tokens)
        self.assertEqual(self.text_widget.tag_names("1.0"), ('KEYWORD',))

        # Yeni token'larla vurgulama, eski tag'lerin temizlendiğini kontrol et
        new_tokens = [('NUMBER', '42', 0)]
        self.text_widget.delete("1.0", tk.END)
        self.text_widget.insert("1.0", "42")
        self.highlighter.highlight(new_tokens)
        self.assertEqual(self.text_widget.tag_names("1.0"), ('NUMBER',))

if __name__ == '__main__':
    unittest.main()