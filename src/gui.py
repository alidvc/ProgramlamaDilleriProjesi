import tkinter as tk
from tkinter import messagebox
from lexer import LexicalAnalyzer
from parser import SyntaxAnalyzer
from highlighter import Highlighter

class SyntaxHighlighterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerçek Zamanlı Sözdizimi Vurgulayıcı")
        self.lexer = LexicalAnalyzer()
        self.parser = SyntaxAnalyzer()
        self.highlighter = Highlighter(self.text_area)

        # GUI bileşenleri
        self.text_area = tk.Text(root, height=20, width=60)
        self.text_area.pack(padx=10, pady=10)
        self.error_label = tk.Label(root, text="", fg="red")
        self.error_label.pack()

        # Gerçek zamanlı vurgulama için olay bağlama
        self.text_area.bind("<KeyRelease>", self.highlight)

    def highlight(self, event=None):
        try:
            # Metni al ve token'lara ayır
            text = self.text_area.get("1.0", tk.END)
            tokens = self.lexer.tokenize(text)

            # Sözdizimsel analiz
            self.parser.shift_reduce_parse(tokens)

            # Token'ları vurgula
            self.highlighter.highlight(tokens)

            self.error_label.config(text="Sözdizimi doğru")
        except ValueError as e:
            self.error_label.config(text=str(e))