import csv
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import time
import os

def sel():                                      # shows value of the scale
   selection = "Diesen Wert speichern: " + str(var.get())
   label.config(text=selection)

def write():                                    # writes saved value from scale to Value.txt file
   wert_write = str(var.get())
   value_file = open("Value.txt", "w")
   value_file.write(wert_write)
   value_file.close()

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

def csvrefresh():                                       # read's values form Graph.csv and imports them into a List
    root.destroy()
    os.system("python App.py")

def tick():                                     # function clock
    global time1                                # define global variable
    time2 = time.strftime('%H:%M:%S')           # define strftime
    if time2 != time1:                          # clock refresh after 200 tick
        time1 = time2
        clock.config(text=time2)
    clock.after(200, tick)


root = Tk()
root.title("Gesture Control Glove")
root.geometry("1000x500")
root.configure(bg="white")

positionRight = int(root.winfo_screenwidth() / 2 - 500)
positionDown = int(root.winfo_screenheight() / 2 - 250)
root.geometry("+{}+{}".format(positionRight, positionDown))


time1 = ''
status = Label(root, bd=1, relief=SUNKEN, anchor=W)                 # define Clock label parameter
status.grid(row=300, column=150)

clock = Label(root, font=('times', 20, 'bold'), bg="lightblue")     # define Clock label background parameter
clock.grid(row=300, column=150)
tick()                                             # starts clock function

var = IntVar()                                     # init variable for scale

with open("Graph.csv") as f:
    csv_f = csv.reader(f, delimiter=",")

    woche = []                               # Lists where the Graph.csv files are stored
    wert = []
    for row in csv_f:                        # imports the value in the second column for each row to a list
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


img = PhotoImage(file="GCG_Logo.png")
label2 = Label(root, image=img)
label2.place(x=250, y=50, width=150, height=180)

scale = Scale(root, variable=var, bg="white", fg="black", from_=0, to=100, resolution=5)   # define scale
scale.place(x=100, y=80, width=50, height=150)

label = Label(root, bg="white")                             # define label for scale value
label.place(x=80, y=300, width=150, height=20)

label3 = Label(root, text="Grenzwert:", bg="white")                 # Anzeige Grenzwert
label3.place(x=90, y=50, height=20, width=60)

label_error = Label(root, bg="white", fg="red")
label_error.place(x=500, y=360, height=20, width=80)

ubsr1 = Label(root, text="Week:", bg="white")                       # title for week entry
ubsr1.place(x=500, y=420, width=80, height=25)

ubsr2 = Label(root, text="Value:", bg="white")                      # title for value entry
ubsr2.place(x=610, y=420, width=80, height=25)

week = Entry(root, text="Week", fg="black", bg="lightblue")         # define entry for "week" input
week.place(x=500, y=390, width=80, height=25)

value = Entry(root, text="Value", fg="black", bg="lightblue")       # define entry for "value" input
value.place(x=610, y=390, width=80, height=25)

button1 = Button(root, text="Show", command=sel)             # declare Button to sel() function
button1.place(x=105, y=250, width=50, height=20)

button2 = Button(root, text="Save", command=write)          # declare Button to write() function
button2.place(x=160, y=250, width=50, height=20)

button3 = Button(root, text="Save Entry", command=csvspeicher)      # declare Button to csvspeicher() function
button3.place(x=750, y=395, width=80, height=25)

button4 = Button(root, text="Refresh Graph", command=csvrefresh)      # declare Button to csvreader() function
button4.place(x=850, y=395, width=80, height=25)


root.mainloop()                         # mainloop for window
