# UI component class for zipper file archiver
# Author: Chase Quinn
# Date: 3/20/2025

from tkinter import *
from PIL import Image, ImageTk

class Components:
    def __init__(self):
        self.geometry = "500x500"
        self.title = "FilePacker"
        self.background = "#aaaaaa"

    def root(self):
        root = Tk()
        root.geometry(self.geometry)
        root.title(self.title)
        root.configure(bg=self.background)
        return root
    
    def label(self, root, text):
        label = Label(root, text=text)
        return label
    
    def image(self, root, image):
        image = Image.open(image)
        photo = ImageTk.PhotoImage(image)
        imageLabel = Label(root, image=photo, borderwidth=0, highlightthickness=0)
        imageLabel.image = photo
        return imageLabel
    
    def button(self, root, text):
        button = Button(root, text=text)
        return button
    
    def checkbox(self, root, text, var):
        checkbox = Checkbutton(root, text=text, onvalue=1, offvalue=0, variable=var)
        return checkbox