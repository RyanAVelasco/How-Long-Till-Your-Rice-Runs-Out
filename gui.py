from tkinter import *

mainWindow = Tk()

# === Create label widget
emptySpace = Label(mainWindow, text="", pady=10)
bagWeight = Label(mainWindow, text="Bag weight: 8kg", pady=10)
noPeople = Label(mainWindow, text="Number of people", pady=10)
portion = Label(mainWindow, text="Portion size", pady=10)

# === Assign labels to specific areas on the window (grid)
# label.push()  # places the label in the top centre regardless of window size
emptySpace.grid(row=0, column=0)
bagWeight.grid(row=1, column=0)
noPeople.grid(row=2, column=0)
portion.grid(row=3, column=0)
emptySpace.grid(row=4, column=0)

# === Have button do something
def calculate():
    global days
    global weeks
    global years

    bag = 8000  # gram: standard weight of rice bag

    base_amt = int(input("How much rice: "))

    # ppl = input("How many people: ")

    days = 0
    new_amt = 0

    while new_amt < bag:
        days += 1
        new_amt += base_amt

    print("Your rice will last:", days, "days")
    print("Your rice will last:", days / 52, "weeks")
    print("Your rice will last:", days / 365, "years")

    days = days
    weeks = days/52
    years = days/365

    labela = Label(mainWindow, text=("Days:", days))
    labelb = Label(mainWindow, text=("Weeks:", weeks))
    labelc = Label(mainWindow, text=("Years:", years))

    labela.grid(row=6, column=0)
    labelb.grid(row=7, column=0)
    labelc.grid(row=8, column=0)

# === Create button
button = Button(mainWindow, text="click please", command=calculate)
button.grid(row=5, column=0, pady=10)

# === Main loop
mainWindow.mainloop()



quit()