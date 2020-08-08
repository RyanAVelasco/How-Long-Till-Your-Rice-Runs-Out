from tkinter import *

mainWindow = Tk()

# === Create label widget
bagWeight = Label(mainWindow, text="Bag weight: 8kg", pady=5).grid(row=1, column=0, padx=10)
noPeople = Label(mainWindow, text="Number of people", pady=5).grid(row=2, column=0, padx=10)
portion = Label(mainWindow, text="Portion size", pady=5).grid(row=3, column=0, padx=10)

# === Entry fields
weight = Entry(mainWindow)
weight.grid(row=1, column=1, padx=10)
people = Entry(mainWindow)
people.grid(row=2, column=1, padx=10)
serving = Entry(mainWindow)
serving.grid(row=3, column=1, padx=10)


def calculate():
    days = 1
    new_amt = int(serving.get()) * int(people.get())

    while new_amt < int(weight.get()):
        days += 1
        new_amt += int(serving.get()) * int(people.get())

    # === Console Information to reference
    # print("Your rice will last:", days, "days")
    # print("Your rice will last:", days / 52, "weeks")
    # print("Your rice will last:", days / 365, "years")

    days = days
    weeks = days//52
    years = days//365

    label_days = Label(mainWindow, text=("Days:", days))
    label_weeks = Label(mainWindow, text=("Weeks:", weeks))
    label_years = Label(mainWindow, text=("Years:", years))

    label_days.grid(row=7, columnspan=2)
    label_weeks.grid(row=8, columnspan=2)
    label_years.grid(row=9, columnspan=2)

# === Create button
button = Button(mainWindow, text="CALCULATE", command=calculate, fg="black")
button.grid(row=6, columnspan=2, column=0, pady=10)

# === Main loop
mainWindow.mainloop()



quit()