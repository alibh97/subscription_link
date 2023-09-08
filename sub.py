
import tkinter as tk
from tkinter import ttk

def transform_link(link):
    parts = link.split('/')
    file_id = parts[5] if len(parts) > 5 else None
    if file_id:
        return f"https://drive.google.com/uc?id={file_id}&export=download"
    else:
        return None

def on_transform_click():
    original_link = link_entry.get()
    transformed = transform_link(original_link)
    if transformed:
        result_var.set(transformed)

def copy_to_clipboard():
    app.clipboard_clear()
    app.clipboard_append(result_var.get())
    app.update()  # Now it stays on the clipboard after the window is closed

app = tk.Tk()
app.title("Link Transformer")

# Input field for the original link
ttk.Label(app, text="Enter Google Drive Link:").pack(pady=10)
link_entry = ttk.Entry(app, width=60)
link_entry.pack(pady=10)

# Button to perform the transformation
transform_button = ttk.Button(app, text="Transform", command=on_transform_click)
transform_button.pack(pady=10)

# Display the transformed link
result_var = tk.StringVar()
result_display = ttk.Entry(app, textvariable=result_var, state='readonly', width=60)
result_display.pack(pady=10)

# Button to copy the result to clipboard
copy_button = ttk.Button(app, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=20)

app.mainloop()
