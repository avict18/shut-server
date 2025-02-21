import os
import sys
import tkinter as tk
from threading import Thread
from flask import Flask
from PIL import Image, ImageTk
from datetime import datetime

app = Flask(__name__)

# Function to calculate days remaining until May 5th
def days_until_may_5():
    today = datetime.today().date()
    target_date = datetime(today.year, 5, 5).date()
    if today > target_date:
        target_date = datetime(today.year + 1, 5, 5).date()  # Use next year's May 5th if already passed
    return (target_date - today).days

# Function to display the image and shutdown
def display_image_and_shutdown():
    window = tk.Toplevel(root)
    window.title("Shutdown Warning")
    
    # Make the window full screen
    window.attributes('-fullscreen', True)
    window.resizable(False, False)
    
    try:
        img = Image.open("logo.png")

        # Get screen dimensions
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        # Resize the image to fit the screen
        img_resized = img.resize((screen_width, screen_height), Image.Resampling.LANCZOS)

        # Convert the image to Tkinter's format
        img_tk = ImageTk.PhotoImage(img_resized)

        # Create a label to display the image as the background
        img_label = tk.Label(window, image=img_tk)
        img_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Keep a reference to the image
        window.image = img_tk

        # Calculate days remaining until May 5th
        days_remaining = days_until_may_5()

        # Display a message on top of the background
        message_text = f"Your computer is shutting down in a Moment...\nDays remaining until ASCEE: {days_remaining}"
        message = tk.Label(window, text=message_text, font=("Arial", 24), fg="white", bg="black")
        message.pack(pady=20)

        # Check if the host OS is Windows
        if sys.platform == "win32":
            os.system("shutdown /s /t 000")
        else:
            os.system("shutdown now")
    
    except Exception as e:
        print(f"Error displaying image: {str(e)}")

@app.route('/')
def home():
    return "Welcome to the Avict18 Shutdown Server! Visit /trigger_shutdown to trigger shutdown."

@app.route('/trigger_shutdown')
def trigger_shutdown():
    # Schedule the function in the main Tkinter thread
    root.after(0, display_image_and_shutdown)
    return "Shutdown has been triggered. Please wait while the image is displayed."

def run_flask():
    # Run Flask in a separate thread
    app.run(debug=True, host="0.0.0.0", port=5000, use_reloader=False)

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()

    # Start Flask in a separate thread
    flask_thread = Thread(target=run_flask, daemon=True)
    flask_thread.start()

    root.mainloop()
