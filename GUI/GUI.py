from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import os
import csv



def csvspeicher():                                      # writes values saved by "week" and "value" to Graph.csv file
    csvfile = open("Graph.csv", "a", newline="")
    try:
        csvrow = [int(week.get()), int(value.get())]
        with csvfile:                                   # csv.writer appends a new line in .csv when button3 is pressed
            writer = csv.writer(csvfile)
            writer.writerow(csvrow)
        csvfile.close()
        label_error.config(text="")
    except ValueError:
        label_error.config(text="Only Values!")

root=Tk()

def csvrefresh():
    root.destroy()
    os.system("python App.py")

button4 = Button(root, text="Refresh Graph", command=csvrefresh)
button4.place(x=850, y=395, width=80, height=25)







with open("Graph.csv") as f:
    csv_f = csv.reader(f, delimiter=",")

    woche = []
    wert = []
    for row in csv_f:
        if any(row):
            woche.append(row[0])
            wert.append(row[1])
    f.close()

x = woche
y = wert


figure = Figure(figsize=(4, 4), dpi=70)
figure.suptitle("Trainingsverlauf")

a = figure.add_subplot(111)
a.set_xlabel("Monat seit Trainingsbeginn")
a.set_ylabel("Einstellgrad [%]")
a.plot(x, y, marker="o")
a.grid()

canvas = FigureCanvasTkAgg(figure, root)
canvas.get_tk_widget()
graph_widget = canvas.get_tk_widget()
graph_widget.place(x=550, y=50, width=400, height=300)




label_error = Label(root, bg="white", fg="red")
label_error.place(x=500, y=360, height=20, width=80)

week = Entry(root, text="Week", fg="black", bg="lightblue")         # define entry for "week" input
week.place(x=500, y=390, width=80, height=25)

value = Entry(root, text="Value", fg="black", bg="lightblue")       # define entry for "value" input
value.place(x=610, y=390, width=80, height=25)

button3 = Button(root, text="Save Entry", command=csvspeicher)      # declare Button to csvspeicher() function
button3.place(x=750, y=395, width=80, height=25)

button4 = Button(root, text="Refresh Graph", command=csvrefresh)
button4.place(x=850, y=395, width=80, height=25)



root.mainloop()

