import pyttsx3
import PyPDF2
from threading import Thread
import os
from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfile
from PIL import ImageTk, Image


root = tk.Tk()  
root.geometry("500x300")
root.configure(bg="#FFBA7A")
root.title("Real Reader")
speaker = pyttsx3.init()



def asli():
    
    speaker.setProperty('rate', 150)
    for num in range(pag, pages):
        page_r = pdfReader.getPage(num)
        text = page_r.extractText()
        speaker.say(text)
        speaker.runAndWait()

def read():
    global pag,pages,pdfReader
    book_1 = open(file_1[0], 'rb')
    pdfReader = PyPDF2.PdfFileReader(book_1)
    pages = pdfReader.numPages
    pag = page.get()
    if pag > pages:
        print("Error")
    else:
        thread = Thread(target = asli,daemon=True)
        thread.start()
    
def open_file():
    global file_1
    file_1 = tk.filedialog.askopenfilenames(filetypes=(('PDF Files', '*.pdf'),))
    print(file_1)
    name = os.path.basename(file_1[0])[:-4]
    book.set(name)

label_0 = Label(master=root,bg = "#FFBA7A",fg="#815B3A")
label_0.configure(text = 'Real Reader',font=("Georgia 13 bold",28,"bold"))
label_0.place(x=140,y=60)

label_1 = Label(master=root,bg = "#FFBA7A",fg="#815B3A")
label_1.configure(text = 'Select PDF:',font=("Georgia 13",14))
label_1.place(x=30,y=120)

book= tk.StringVar()
Entry_label = tk.Entry(master=root)
Entry_label.configure(textvariable = book)
Entry_label.place(x=30,y=150,width=250,height=27)

button1 = tk.Button(master=root,relief = "groove", text="Browse", command=open_file).place(x=300,y=150,width=84,height=27)


label_2 = Label(master=root,bg = "#FFBA7A",fg="#815B3A")
label_2.configure(text = 'Read From Page #:',font=("Georgia 13",14))
label_2.place(x=30,y=180)

page= tk.IntVar()
Entry_label = tk.Entry(master=root)
Entry_label.configure(textvariable = page)
Entry_label.place(x=30,y=210,width=250,height=27)

button1 = tk.Button(master=root,relief = "groove", text="Read", command=read).place(x=300,y=210,width=84,height=27)

mainloop()