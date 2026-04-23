from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """Generate a strong random password and copy it to clipboard"""
    # Password composition: 8-12 letters, 2-4 numbers, 2-4 symbols
    letters = random.randint(8, 12)
    numbers = random.randint(2, 4)
    symbols = random.randint(2, 4)
    
    # Character sets
    password_letters = [random.choice(string.ascii_letters) for _ in range(letters)]
    password_numbers = [random.choice(string.digits) for _ in range(numbers)]
    password_symbols = [random.choice(string.punctuation) for _ in range(symbols)]
    
    # Combine and shuffle
    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    
    # Create password string
    password = "".join(password_list)
    
    # Clear and insert into password entry
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    
    # Copy to clipboard
    pyperclip.copy(password)
    messagebox.showinfo("Success", "Password generated and copied to clipboard!")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """Save password details to file after validation"""
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()
    
    # Validation
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror("Error", "Please fill in all fields!")
        return
    
    # Confirmation dialog
    is_ok = messagebox.askokcancel(
        title=website,
        message=f"These are the details entered:\n\nWebsite: {website}\nEmail: {email}"
                f"\nPassword: {password}\n\nIs it ok to save?"
    )
    
    if is_ok:
        try:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
            
            # Clear fields after saving
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            # Keep email for convenience (usually same email for multiple sites)
            
            messagebox.showinfo("Success", "Password saved successfully!")
            
            # Focus back to website entry
            website_entry.focus()
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save password: {str(e)}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

# Canvas with logo
canvas = Canvas(window, width=200, height=200, bg="white", highlightthickness=0)
try:
    logo_img = PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=logo_img)
except:
    # If logo.png doesn't exist, create a placeholder
    canvas.create_text(100, 100, text="🔐", font=("Arial", 60))
canvas.grid(row=0, column=1, pady=20)

# Labels
website_label = Label(text="Website:", bg="white", font=("Arial", 10))
website_label.grid(row=1, column=0, sticky="e", pady=5)

email_label = Label(text="Email/Username:", bg="white", font=("Arial", 10))
email_label.grid(row=2, column=0, sticky="e", pady=5)

password_label = Label(text="Password:", bg="white", font=("Arial", 10))
password_label.grid(row=3, column=0, sticky="e", pady=5)

# Entries
website_entry = Entry(width=35, font=("Arial", 10))
website_entry.grid(row=1, column=1, columnspan=2, sticky="ew", pady=5, padx=5)
website_entry.focus()

email_entry = Entry(width=35, font=("Arial", 10))
email_entry.grid(row=2, column=1, columnspan=2, sticky="ew", pady=5, padx=5)
email_entry.insert(0, "example@email.com")  # Default email

password_entry = Entry(width=21, font=("Arial", 10))
password_entry.grid(row=3, column=1, sticky="ew", pady=5, padx=5)

# Buttons
generate_password_button = Button(
    text="Generate Password",
    command=generate_password,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 9, "bold"),
    cursor="hand2"
)
generate_password_button.grid(row=3, column=2, sticky="ew", pady=5, padx=5)

add_button = Button(
    text="Add",
    width=36,
    command=save,
    bg="#2196F3",
    fg="white",
    font=("Arial", 10, "bold"),
    cursor="hand2"
)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew", pady=10, padx=5)

window.mainloop()
