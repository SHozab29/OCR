import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:/Users/SHozab29\AppData/Local/Programs/Tesseract-OCR/tesseract.exe'
class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Create button to select image file
        self.select_image_button = tk.Button(self, text="Select Image", command=self.select_image)
        self.select_image_button.pack(side="top")

        # Create label to display selected image
        self.image_label = tk.Label(self)
        self.image_label.pack(side="top")

        # Create button to extract text from image
        self.extract_text_button = tk.Button(self, text="Extract Text", command=self.extract_text)
        self.extract_text_button.pack(side="top")

        # Create label to display extracted text
        self.text_label = tk.Label(self, wraplength=500)
        self.text_label.pack(side="top")

        self.save_text_button = tk.Button(self, text="Save Text", command=self.save_text)
        self.save_text_button.pack(side="top")

    def select_image(self):
        # Open file dialog to select image file
        self.image_file = filedialog.askopenfilename(title="Select Image", filetypes=(("Image files", "*.png *.jpg *.jpeg *.bmp"), ("All files", "*.*")))
        
        # Load selected image and display in label
        image = Image.open(self.image_file)
        image = image.resize((500, 500))
        self.image = ImageTk.PhotoImage(image)
        self.image_label.configure(image=self.image)

    def extract_text(self):
        # Extract text from selected image using Tesseract
        text = pytesseract.image_to_string(Image.open(self.image_file))

        # Display extracted text in label
        self.text_label.configure(text=text)
        self.extracted_text = text
    
    
    def save_text(self):
        # Open file dialog to select save file location
        save_file = filedialog.asksaveasfilename(title="Save Text", defaultextension=".txt", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))

        # Write extracted text to file
        with open(save_file, "w") as file:
            file.write(self.extracted_text)
root = tk.Tk()
app = App(master=root)
app.mainloop()