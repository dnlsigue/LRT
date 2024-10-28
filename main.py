import tkinter as tk


def on_button_click():
    label.config(text="Button Clicked!")


# Create the main window
root = tk.Tk()
root.title("My Tkinter App")
root.geometry("600x600")  # Width x Height

# Add a label widget
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=20)

# Add a button widget
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
