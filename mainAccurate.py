import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
from google.cloud import vision
import io

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.client = vision.ImageAnnotatorClient()  # initialize Google Vision API client

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

    def select_image(self):
        # Open file dialog to select image file
        self.image_file = filedialog.askopenfilename(title="Select Image", filetypes=(("Image files", "*.png *.jpg *.jpeg *.bmp"), ("All files", "*.*")))
        
        # Load selected image and display in label
        image = Image.open(self.image_file)
        image = image.resize((500, 500))
        self.image = ImageTk.PhotoImage(image)
        self.image_label.configure(image=self.image)

    def extract_text(self):
        # Extract text from selected image using Google Vision API
        with io.open(self.image_file, 'rb') as image_file:
            content = image_file.read()

        image = vision.Image(content=content)
        response = self.client.document_text_detection(image=image)
        text = response.full_text_annotation.text

        # Display extracted text in label
        self.text_label.configure(text=text)

root = tk.Tk()
app = App(master=root)
app.mainloop()