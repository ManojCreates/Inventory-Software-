import tkinter as tk
from tkinter import messagebox, ttk
from database import add_product, fetch_all_products, delete_product

def product_management_ui(root):
    root.title("Inventory Management System")
    root.geometry("800x600")

    # UI components
    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack(fill="both", expand=True)

    title_label = tk.Label(frame, text="LANKA GLASS HOUSE INVENTORY", font=("Arial", 24))
    title_label.pack(pady=10)

    # Table for displaying products
    columns = ("ID", "Name", "Category", "Stock Quantity", "Price", "Low Stock Alert")
    product_table = ttk.Treeview(frame, columns=columns, show="headings")
    product_table.pack(fill="both", expand=True)

    for col in columns:
        product_table.heading(col, text=col)

    # Load products into table
    def load_products():
        for row in product_table.get_children():
            product_table.delete(row)
        products = fetch_all_products()
        for product in products:
            product_table.insert("", tk.END, values=product)

    load_products()

    # Add Product Form
    add_product_frame = tk.Frame(frame, pady=10)
    add_product_frame.pack(fill="x")

    tk.Label(add_product_frame, text="Name:").grid(row=0, column=0, padx=5)
    name_entry = tk.Entry(add_product_frame)
    name_entry.grid(row=0, column=1, padx=5)

    tk.Label(add_product_frame, text="Category:").grid(row=1, column=0, padx=5)
    category_entry = tk.Entry(add_product_frame)
    category_entry.grid(row=1, column=1, padx=5)

    tk.Label(add_product_frame, text="Stock Quantity:").grid(row=2, column=0, padx=5)
    stock_quantity_entry = tk.Entry(add_product_frame)
    stock_quantity_entry.grid(row=2, column=1, padx=5)

    tk.Label(add_product_frame, text="Price:").grid(row=3, column=0, padx=5)
    price_entry = tk.Entry(add_product_frame)
    price_entry.grid(row=3, column=1, padx=5)

    tk.Label(add_product_frame, text="Low Stock Alert:").grid(row=4, column=0, padx=5)
    low_stock_alert_entry = tk.Entry(add_product_frame)
    low_stock_alert_entry.grid(row=4, column=1, padx=5)

    def add_product_ui():
        name = name_entry.get()
        category = category_entry.get()
        stock_quantity = int(stock_quantity_entry.get())
        price = float(price_entry.get())
        low_stock_alert = int(low_stock_alert_entry.get())

        add_product(name, category, stock_quantity, price, low_stock_alert)
        load_products()
        messagebox.showinfo("Success", "Product added successfully!")

    add_product_button = tk.Button(add_product_frame, text="Add Product", command=add_product_ui)
    add_product_button.grid(row=5, column=1, pady=10)

    # Delete product function
    def delete_product_ui():
        selected_item = product_table.selection()
        if selected_item:
            product_id = product_table.item(selected_item[0])["values"][0]
            delete_product(product_id)
            load_products()
            messagebox.showinfo("Success", "Product deleted successfully!")
        else:
            messagebox.showwarning("Warning", "No product selected!")

    delete_product_button = tk.Button(frame, text="Delete Selected Product", command=delete_product_ui)
    delete_product_button.pack(pady=10)
