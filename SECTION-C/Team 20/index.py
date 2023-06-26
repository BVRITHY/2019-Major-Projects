from tkinter import *
from flask import Flask,redirect, url_for,render_template,request
import os


def d_dtcn():
    root = Tk()
    w=340
    h=246
    
    
    
    ws=root.winfo_screenwidth()
    hs=root.winfo_screenheight()
    
    x=(ws/2)-(w/2)
    y=(hs/2)
    print(ws,hs)
    
    
    ##root.geometry("343x335")
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    #img = Tk.PhotoImage(file = "C:/Users/Windows 10/Documents/a/static/assets/abc.gif")
    bg = PhotoImage(file = "abc.gif")
#     label1 = Label( root, image = bg)
#     label1.place(x = 0, y = 0)
    def function1(): 
        os.system("python drowsiness_detection.py --shape_predictor shape_predictor_68_face_landmarks.dat")
        exit()

    def function2(): 
        os.system("python android_cam.py --shape_predictor shape_predictor_68_face_landmarks.dat")
        exit()
        
    root.title("DROWSINESS DETECTION")
    label1 = Label(root, text="DROWSINESS DETECTION",font=("times new roman",20),height=2)
    label1.grid(row=2,rowspan=2,columnspan=5,sticky=N+E+W+S,padx=5,pady=10)
    
    
    my_button =Button(root,text="Run using web cam",font=("times new roman",20),bg="#0D47A1",fg='white',command=function1)
    my_button.grid(row=5,columnspan=5,sticky=W+E+N+S,padx=5,pady=5)
    my_button.place(relx=0.5,rely=0.5,anchor=CENTER)    
         

    root.mainloop()