import tkinter as tk
from autocorrect import Speller

def autocorrect_text():
    # Using English for autocorrection
    spell = Speller(lang='en')   
    corrected_text = spell(text_entry.get())
    corrected_label.config(text="Auto Corrected: " + corrected_text)

# Create the GUI
app = tk.Tk()
app.title("Auto-Correct App")
# Set the window size
app.geometry("500x200")  
# Set the background color
app.configure(bg="cyan")  

text_entry = tk.Entry(app, width=50)
# Adjust the padding
text_entry.pack(pady=20)  

autocorrect_button = tk.Button(app, text="Auto Correct", command=autocorrect_text)
# Adjust the padding
autocorrect_button.pack(pady=5) 

# Set the background color
corrected_label = tk.Label(app, text="", bg="#f0f0f0")
# Adjust the padding
corrected_label.pack(pady=10)  

app.mainloop()
