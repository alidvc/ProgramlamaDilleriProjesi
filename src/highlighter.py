class Highlighter:
    def __init__(self, text_widget):
        self.text_widget = text_widget
        # Renk etiketleri
        self.text_widget.tag_configure("KEYWORD", foreground="blue")
        self.text_widget.tag_configure("IDENTIFIER", foreground="black")
        self.text_widget.tag_configure("NUMBER", foreground="green")
        self.text_widget.tag_configure("OPERATOR", foreground="purple")
        self.text_widget.tag_configure("COMMENT", foreground="gray")

    def highlight(self, tokens):
        # Önceki vurgulamaları temizle
        for tag in ["KEYWORD", "IDENTIFIER", "NUMBER", "OPERATOR", "COMMENT"]:
            self.text_widget.tag_remove(tag, "1.0", tk.END)

        # Token'ları vurgula
        for token_type, token_value, pos in tokens:
            start_idx = self.text_widget.index(f"1.0 + {pos} chars")
            end_idx = self.text_widget.index(f"1.0 + {pos + len(token_value)} chars")
            self.text_widget.tag_add(token_type, start_idx, end_idx)