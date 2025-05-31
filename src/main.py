import tkinter as tk
from gui import SyntaxHighlighterGUI

def main():
    root = tk.Tk()
    app = SyntaxHighlighterGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()