import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import StringVar, messagebox
import json
import os

# File paths for roles
ROLE_FILES = {
    "Admin": "admin.json",
    "Supplier": "supplier.json",
    "Client": "client.json"
}

# Utility functions
def load_users(role):
    """ Load users for a given role from JSON file. """
    file_path = ROLE_FILES.get(role)
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    return []


def save_users(role, users):
    """Save users for a given role to JSON file."""
    file_path = ROLE_FILES.get(role)
    with open(file_path, "w") as f:
        json.dump(users, f, indent=4)


def sign_up(role, name, email):
    """Add a new user to the role file."""
    users = load_users(role)
    # Check if user already exists
    if any(user["email"] == email for user in users):
        messagebox.showerror("Error", f"User with email {email} already exists in {role}.")
        return
    # Add the new user
    users.append({"name": name, "email": email})
    save_users(role, users)
    messagebox.showinfo("Success", f"Sign-Up successful for {role}. You can now log in!")


def login(role, name, email, root):
    """Check if the user exists in the role file."""
    users = load_users(role)
    if any(user["name"] == name and user["email"] == email for user in users):
        messagebox.showinfo("Success", f"Welcome back, {name}!")
        root.withdraw()  # Close the login window
        redirect_user(role,name)  # Redirect to the appropriate interface
    else:
        # Prompt to sign up if not found
        result = messagebox.askyesno("Not Found", "User not found. Would you like to sign up?")
        if result:
            sign_up(role, name, email)


def redirect_user(role,name):
    """Redirect the user to the appropriate interface based on role."""
    if role == "Admin":
        open_admin_interface(name)
    elif role == "Supplier":
        open_supplier_interface(name)
    elif role == "Client":
        open_client_interface(name)


# Admin Interface
def open_admin_interface(name):
    admin_window = ttk.Toplevel()
    admin_window.title("Admin Dashboard")
    # Set window size (800x500)
    window_width = 800
    window_height = 500

    # Get screen width and height
    screen_width = admin_window.winfo_screenwidth()
    screen_height = admin_window.winfo_screenheight()

    # Calculate position to center the window on both x and y axes
    position_top = int((screen_height / 2) - (window_height / 2))  # Vertical center
    position_left = int((screen_width / 2) - (window_width / 2))  # Horizontal center

    # Set window geometry with the calculated position
    admin_window.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")

    ttk.Label(admin_window, text=name, font=("Helvetica", 16),style='success').pack()
    ttk.Label(admin_window, text="Welcome to the Admin Dashboard!", font=("Helvetica", 16)).pack(pady=20)


# Supplier Interface
def open_supplier_interface(name):
    supplier_window = ttk.Toplevel()
    supplier_window.title("Supplier Dashboard")
    # Set window size (800x500)
    window_width = 800
    window_height = 500

    # Get screen width and height
    screen_width = supplier_window.winfo_screenwidth()
    screen_height = supplier_window.winfo_screenheight()

    # Calculate position to center the window on both x and y axes
    position_top = int((screen_height / 2) - (window_height / 2))  # Vertical center
    position_left = int((screen_width / 2) - (window_width / 2))  # Horizontal center

    # Set window geometry with the calculated position
    supplier_window.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")

    ttk.Label(supplier_window, text=name, font=("Helvetica", 16),style='success').pack()
    ttk.Label(supplier_window, text="Welcome to the Supplier Dashboard!", font=("Helvetica", 16)).pack(pady=20)


# Client Interface
def open_client_interface(name):
    client_window = ttk.Toplevel()
    client_window.title("Client Dashboard")
    # Set window size (800x500)
    window_width = 800
    window_height = 500

    # Get screen width and height
    screen_width = client_window.winfo_screenwidth()
    screen_height = client_window.winfo_screenheight()

    # Calculate position to center the window on both x and y axes
    position_top = int((screen_height / 2) - (window_height / 2))  # Vertical center
    position_left = int((screen_width / 2) - (window_width / 2))  # Horizontal center

    # Set window geometry with the calculated position
    client_window.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")
    ttk.Label(client_window, text=name, font=("Helvetica", 16),style='success').pack()
    ttk.Label(client_window, text=f"Welcome to the Client Dashboard!", font=("Helvetica", 16)).pack(pady=20)


# Submit handler
def submit_form(root):
    name = name_var.get()
    email = email_var.get()
    role = role_var.get()

    if not name or not email or role == "Select Role":
        messagebox.showerror("Error", "All fields are required!")
        return

    # Perform login and redirect
    login(role, name, email, root)


# Create main application window
root = ttk.Window(themename="journal")  # Modern theme
root.title("Authentication System")

# Set window size (800x500)
window_width = 800
window_height = 500

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate position to center the window on both x and y axes
position_top = int((screen_height / 2) - (window_height / 2))  # Vertical center
position_left = int((screen_width / 2) - (window_width / 2))  # Horizontal center

# Set window geometry with the calculated position
root.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")


# Variables to store input
name_var = StringVar()
email_var = StringVar()
role_var = StringVar(value="Select Role")

# Form layout
form_frame = ttk.Frame(root, padding=20)
form_frame.place(relx=0.5, rely=0.5, anchor="center")  # Center the frame in the window

# Title at the top (with coll font style and size)
ttk.Label(form_frame, text="User Authentication", font=("Comic Sans MS", 20, "bold"), style="success").grid(row=0, column=0, columnspan=2, pady=20)

# Field 1: Name (Larger input field)
ttk.Label(form_frame, text="Name:", font=("Helvetica", 12)).grid(row=1, column=0, sticky=W, pady=10, padx=20)
ttk.Entry(form_frame, textvariable=name_var, width=40, font=("Helvetica", 12)).grid(row=1, column=1, pady=10, padx=20)

# Field 2: Email (Larger input field)
ttk.Label(form_frame, text="Email:", font=("Helvetica", 12)).grid(row=2, column=0, sticky=W, pady=10, padx=20)
ttk.Entry(form_frame, textvariable=email_var, width=40, font=("Helvetica", 12)).grid(row=2, column=1, pady=10, padx=20)

# Field 3: Role (Larger dropdown)
ttk.Label(form_frame, text="Role:", font=("Helvetica", 12)).grid(row=3, column=0, sticky=W, pady=10, padx=20)
ttk.Combobox(form_frame, textvariable=role_var, values=["Admin", "Supplier", "Client"], width=38, font=("Helvetica", 12)).grid(row=3, column=1, pady=10, padx=20)

# Submit Button (Larger button)
ttk.Button(form_frame, text="Login / Sign-Up", bootstyle="primary", command=lambda: submit_form(root), width=20, style="success").grid(row=4, column=1, sticky=E, pady=20, padx=20)

# Run the application
root.mainloop()
