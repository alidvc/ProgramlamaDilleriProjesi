import re

class LexicalAnalyzer:
    def __init__(self):
        # Token türleri ve düzenli ifadeler
        self.token_patterns = [
            ('KEYWORD', r'\b(if|else|while|return)\b'),
            ('IDENTIFIER', r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),
            ('NUMBER', r'\b\d+\b'),
            ('OPERATOR', r'[+\-*/=]'),
            ('COMMENT', r'//.*'),
            ('WHITESPACE', r'\s+'),
        ]
        self.token_table = [(name, re.compile(pattern)) for name, pattern in self.token_patterns]

    def tokenize(self, text):
        tokens = []
        pos = 0
        while pos < len(text):
            match = None
            for token_type, pattern in self.token_table:
                match = pattern.match(text, pos)
                if match:
                    if token_type != 'WHITESPACE':  # Boşlukları atla
                        tokens.append((token_type, match.group(0), pos))
                    pos = match.end()
                    break
            else:
                raise ValueError(f"Geçersiz karakter at pozisyon {pos}: {text[pos]}")
        return tokens