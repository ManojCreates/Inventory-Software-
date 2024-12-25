# main.py
import tkinter as tk
from ui_components import product_management_ui
from database import setup_db

def main():
    setup_db()  # Ensure database is initialized
    root = tk.Tk()
    product_management_ui(root)
    root.mainloop()

if __name__ == "__main__":
    main()
