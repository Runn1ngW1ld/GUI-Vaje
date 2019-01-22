import Tkinter
import tkMessageBox


window = Tkinter.Tk()

greetings = Tkinter.Label(window, text="Dobrodosli v kalkulatorju z GUI vmesnikom")
greetings.pack()

text1 = Tkinter.Label(window, text="Vnesite prvo stevilo.")
num1 = Tkinter.Entry(window)
text2 = Tkinter.Label(window, text="Vnesite drugo stevilo")
num2 = Tkinter.Entry(window)

text1.pack()
num1.pack()
text2.pack()
num2.pack()


def plus(x, y):
    result = int(x) + int(y)
    tkMessageBox.showinfo("Vsota", result)


def minus(x, y):
    result = int(x) - int(y)
    tkMessageBox.showinfo("Vsota", result)


def mnozeno(x, y):
    result = int(x) * int(y)
    tkMessageBox.showinfo("Vsota", result)


def deljeno(x, y):
    result = int(x) / int(y)
    tkMessageBox.showinfo("Vsota", result)


submit1 = Tkinter.Button(window, text="+", command=lambda: plus(num1.get(), num2.get()))
submit2 = Tkinter.Button(window, text="-", command=lambda: minus(num1.get(), num2.get()))
submit3 = Tkinter.Button(window, text="*", command=lambda: mnozeno(num1.get(), num2.get()))
submit4 = Tkinter.Button(window, text="/", command=lambda: deljeno(num1.get(), num2.get()))

submit1.pack()
submit2.pack()
submit3.pack()
submit4.pack()

window.mainloop()