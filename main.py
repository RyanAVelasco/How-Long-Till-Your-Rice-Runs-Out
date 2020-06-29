from colored import stylize

bag = 8000  # grams
bamt = int(input("How much rice: "))
# ppl = input("How many people: ")


days = 0
namt = 0


while namt < bag:
    days += 1
    namt += bamt


print("Your rice will last:", days, "days")
print("Your rice will last:", days/365, "years")

## TEST ##

