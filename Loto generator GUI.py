import random
import Tkinter
import tkMessageBox

window = Tkinter.Tk()

greetings = Tkinter.Label(window, text="Dobrodosli v generatorju Loto stevilk.")
greetings.pack()

greetings1 = Tkinter.Label(window, text="Vpisite koliko stevilko hocete generirat")
greetings1.pack()

user = Tkinter.Entry(window)
user.pack()

def generator():
    numbers = []

    for x in range(int(user.get())):
        numbers.append(random.randint(1, 39))

    tkMessageBox.showinfo("Tvoje stevilke", numbers)


submit = Tkinter.Button(window, text="Zazeni", command=generator)

submit.pack()

window.mainloop()