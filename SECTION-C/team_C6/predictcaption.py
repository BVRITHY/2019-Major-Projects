from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import requests
import torch
import os
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import argparse
import subprocess
from tkinter import messagebox


processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")
result_string =""
score=0

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("IMAGE CAPTION GENERATION")
        self.minsize(640, 400)

        self.labelFrame = ttk.LabelFrame(self, text = "Open And Clear Image")
        self.labelFrame.grid(column = 0, row = 1, padx = 20, pady = 20)

        self.button()
        self.clearbutton()


    def button(self):
        self.button = ttk.Button(self.labelFrame, text = "Browse Image",command = self.fileDialog)
        self.button.grid(column = 1, row = 1)

    def clearbutton(self):
        self.button = ttk.Button(self.labelFrame, text = "CLEAR",command =self.cleardataimage)
        self.button.grid(column = 2, row = 1)


    def fileDialog(self):
        global result_string
        global resultlist
        global scorelist
        self.filename = filedialog.askopenfilename()
     
        print(self.filename)

        #self.label = ttk.Label(self.labelFrame, text = "")
        #self.label.grid(column = 1, row = 2)
        #self.label.configure(text = self.filename)
        img = Image.open(self.filename)
        photo = ImageTk.PhotoImage(img)	
     
        
        #im = Image.open(self.filename)
        result_string=gen(img)
        print("========================")
        print(result_string)
        print("========================")
        pred1=result_string[0]
        pred2=result_string[1]
        pred3=result_string[2]

        self.label3 = Label(text="PREDICTION RESULT  ")
        self.label3.grid(column=0, row=2)
        self.label3.config(font=("Courier", 15))
        self.label4 = Label(text=pred1)
        self.label4.config(font=("Courier", 15))
        self.label4.grid(column=0, row=3)

        self.label5 = Label(text=pred2)
        self.label5.config(font=("Courier", 15))
        self.label5.grid(column=0, row=4)

        self.label6 = Label(text=pred3)
        self.label6.config(font=("Courier", 15))
        self.label6.grid(column=0, row=5)

        self.label2 = Label(image=photo)
        self.label2.image = photo 
        self.label2.grid(column=0, row=6)
 
		


    def cleardataimage(self):
        global result_string
        print("CLEAR FUNCTION CALLED")
        self.label2.image=None
        self.label3.configure(text = "")
        self.label4.configure(text = "")
        self.label5.configure(text = "")
        self.label6.configure(text = "")
        result_string=""
        #self.label5.configure(text = "")
        #resultlist.clear()
        #scorelist.clear()


def gen(image1):
    l=[]
    inputs = processor(image1, return_tensors='pt', padding=True)
    captions = model.generate(**inputs, max_length=20,num_beams=5, num_return_sequences=3, do_sample=True)
    for caption in captions :
            
              l1 = processor.decode(caption, skip_special_tokens=True)
              l.append(l1)
    return l



root = Root()
root.mainloop()