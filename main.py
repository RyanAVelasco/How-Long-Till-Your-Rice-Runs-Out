from tkinter import *

mainWindow = Tk()

# === Create label widget
bagWeight = Label(mainWindow, text="Bag weight: 8000g", pady=10).grid(row=0, padx=20)
noPeople = Label(mainWindow, text="Number of people", pady=10).grid(row=2, padx=20)
portion = Label(mainWindow, text="Portion size", pady=10).grid(row=4, padx=20)

# === Entry fields
weight = Entry(mainWindow)
weight.grid(row=1)
people = Entry(mainWindow)
people.grid(row=3)
serving = Entry(mainWindow)
serving.grid(row=5)

def calculate():
    days = 1
    new_amt = int(serving.get()) * int(people.get())

    while new_amt < int(weight.get()):
        days += 1
        new_amt += int(serving.get()) * int(people.get())

    # === Console Information to reference
    print("Your rice will last:", days, "days")
    print("Your rice will last:", days / 52, "weeks")
    print("Your rice will last:", days / 365, "years")

    days = days
    weeks = days/52
    years = days/365

    label_days = Label(mainWindow, text=("Days:", days))
    label_weeks = Label(mainWindow, text=("Weeks:", weeks))
    label_years = Label(mainWindow, text=("Years:", years))

    label_days.grid(row=7)
    label_weeks.grid(row=8)
    label_years.grid(row=9)

# === Create button
button = Button(mainWindow, text="CALCULATE", command=calculate, fg="blue")
button.grid(row=6, pady=10)

# === Main loop
mainWindow.mainloop()



quit()