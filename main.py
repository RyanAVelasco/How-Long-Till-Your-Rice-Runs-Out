from colored import stylize

bag = 8000  # grams
base_amt = int(input("How much rice: "))
# ppl = input("How many people: ")


days = 0
new_amt = 0


while new_amt < bag:
    days += 1
    new_amt += base_amt


print("Your rice will last:", days, "days")
print("Your rice will last:", days/52, "weeks")
print("Your rice will last:", days/365, "years")

## TEST ##

