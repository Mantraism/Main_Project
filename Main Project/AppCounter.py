from itertools import count
from tkinter import *
window = Tk()
window.title('App Counter')
angka = 0
def counterup():
    global angka
    angka += 1
    outputhasil = Label(window,text=angka)
    outputhasil.grid(column=1,row=1,columnspan=2)
def counterdown():
    global angka
    angka -= 1
    outputhasil = Label(window,text=angka)
    outputhasil.grid(column=1,row=1,columnspan=2)
tomboltambah = Button(window,text='+',padx=50,pady=10,bg='green',fg='white',command=counterup)
tombolkurang = Button(window,text='-',padx=50,pady=10,bg='red',fg='white',command=counterdown)
tomboltambah.grid(column=1,row=0,columnspan=2)
Label(window,text=angka).grid(column=1,row=1,columnspan=2)
tombolkurang.grid(column=1,row=2,columnspan=3)
window.mainloop()

#Mantraism was here
# 0    0
# /\/\/\
