import tkinter as tk
import mysql.connector
from tkinter import ttk

# Connect to MySQL 
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Cake_Booking_System"
)

cursor = mydb.cursor()

# Function to register a member
def register_member():
    name = name_var.get()
    print("Customer's name:", name)
    email = email_var.get()
    print("Customer's email:", email)
    cake = cake_var.get()
    print("Selected cake:", cake)
    quantity = quantity_var.get()
    print("Quantity:", quantity)
    member_card = member_card_var.get()
    print("Member card:", member_card)

    # Insert member details into the database
    sql = "INSERT INTO cake_booking (name, email, cake_var, quantity_var, member_card_var) VALUES (%s, %s, %s, %s, %s)"
    values = (name, email, cake, quantity, member_card)
    cursor.execute(sql, values)
    mydb.commit()

    result_label.config(text=f"Registered {name} as a member!", fg="green")

# Function to handle booking
def book_cake():
    cake = cake_var.get()
    quantity = int(quantity_var.get())

    if member_card_var.get() == "Yes":
        member_discount = 0.9  # 10% discount for members
    else:
        member_discount = 1.0  # No discount for non-members

    total_price = quantity * prices[cake] * member_discount

    result_label.config(text=f"Booked {quantity} {cake}(s) for a total of ${total_price:.2f}", fg="blue")

# GUI Setup
root = tk.Tk()
root.title("Cake Booking System")
root.geometry("400x400")

prices = {
    "Royal Velvet Delight": 40,
    "Midnight Bliss Cake": 35,
    "Emerald Dream Cake": 45,
    "Enchanted Eclair": 38,
    "Velvet Symphony Cake": 42,
    "Celestial Frosting Fantasy": 50,
    "Golden Chiffon Cascade": 48,
    "Sparkling Raspberry Rhapsody": 36,
    "Caramel Elegance Supreme": 44,
    "Diamond Jubilee Cake": 55,
}

register_frame = tk.Frame(root)
register_frame.pack(pady=10)

name_label = tk.Label(register_frame, text="Name:", fg="pink")
name_label.grid(row=0, column=0)

name_var = tk.StringVar()
name_entry = tk.Entry(register_frame, textvariable=name_var)
name_entry.grid(row=0, column=1)

email_label = tk.Label(register_frame, text="Email:", fg="blue")
email_label.grid(row=1, column=0)

email_var = tk.StringVar()
email_entry = tk.Entry(register_frame, textvariable=email_var)
email_entry.grid(row=1, column=1)

register_button = tk.Button(register_frame, text="Register Member", command=register_member, fg="white", bg="brown")
register_button.grid(row=2, columnspan=2)

booking_frame = tk.Frame(root)
booking_frame.pack(pady=10)

cake_label = tk.Label(booking_frame, text="Select Cake:", fg="blue")
cake_label.grid(row=0, column=0)

cake_var = tk.StringVar()
cake_var_combobox = ttk.Combobox(booking_frame, values=list(prices.keys()), textvariable=cake_var)
cake_var_combobox.grid(row=0, column=1)

quantity_label = tk.Label(booking_frame, text="Quantity:", fg="pink")
quantity_label.grid(row=1, column=0)

quantity_var = tk.StringVar()
quantity_entry = tk.Entry(booking_frame, textvariable=quantity_var)
quantity_entry.grid(row=1, column=1)

member_card_label = tk.Label(booking_frame, text="Member Card?", fg="blue")
member_card_label.grid(row=2, column=0)

member_card_var = tk.StringVar()
member_card_var.set("No")
member_card_combobox = ttk.Combobox(booking_frame, values=["Yes", "No"], textvariable=member_card_var)
member_card_combobox.grid(row=2, column=1)

book_button = tk.Button(root, text="Book Cake", command=book_cake, fg="white", bg="blue")
book_button.pack()

result_label = tk.Label(root, text="", fg="pink")
result_label.pack()

root.mainloop()
