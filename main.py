from tkinter import *
from tkinter import messagebox


import os
import pyqrcode

window=Tk()

window.title("QR Code Generator//github.com/SoumyajitD")

window.iconbitmap(r'icon.ico')

def generate():
    if len(Subject.get()) !=0 :
        global qr,photo
        qr=pyqrcode.create(Subject.get())
        photo = BitmapImage(data= qr.xbm(scale=5))
    else :
        messagebox.showinfo("Please enter some URL")

    try:
        showcode()
    except:
        pass


def showcode():
    imageLabel.config(image=photo)
    subLabel.config(text="QR Image is generated")


def save():

	dir= path1 = os.getcwd() + "\\QR Codes"

	#create a folder is it doesn't exist
	if not os.path.exists(dir):
		os.makedirs(dir)


	else:
	       qr.png(os.path.join(dir, name.get()+".png"), scale= 6)








Sub=Label(window,text="Enter the URL")
Sub.grid(row =0,column =0, sticky=N+S+E+W)

FName=Label(window,text="Enter FileName")
FName.grid(row =1,column =0, sticky=N+S+E+W)

Subject=StringVar()
SubEntry=Entry(window,textvariable=Subject)
SubEntry.grid(row =0,column =1, sticky=N+S+E+W)

name=StringVar()
nameEntry=Entry(window,textvariable=name)
nameEntry.grid(row =1,column =1, sticky=N+S+E+W)

button=Button(window,text="Generate QR",width=15,command=generate)
button.grid(row =0,column =3, sticky=N+S+E+W)

imageLabel=Label(window)
imageLabel.grid(row =2,column =1, sticky=N+S+E+W)
subLabel=Label(window,text="")
subLabel.grid(row =3,column =1, sticky=N+S+E+W)

saveB=Button(window,text="Save QR",width=15,command=save)
saveB.grid(row =1,column =3, sticky=N+S+E+W)



Rows= 3
Columns = 3

for row in range(Rows+1):
    window.grid_rowconfigure(row,weight=1)

for col in range(Columns+1):
    window.grid_columnconfigure(col,weight=1)


window.mainloop()
