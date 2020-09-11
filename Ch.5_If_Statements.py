# 9/9/2020
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:  # looks for value 'bmw' and prints in uppercase not title
    if car == 'bmw':  # == is checking for equality, not assigning
        print(car.upper())
    else:
        print(car.title())
# equality is cAsE sensetive
if car != 'Ford':  # != means NOT equal
    print("Fuck Ford")

if 'audi' in cars:  # "in" checks to see if list has certain value
    print("yes audi is a car")
    print(cars == 'audi')  # will be False because cars is more than audi
if 'ford' not in cars:  # "not in" does the opposite
    print("good, fuck that shit forreal")
a = "b"
print(a == "b")  # will print True
print('\n')
ages = [2, 9, 14, 26, 30]
for age in ages:
    if age < 4:
        print("Free admission")
    elif age >= 4 and age <=18:
        print("Pay 25 bucks")
    else:
        print("Pay 40 old-timer")

for car in cars:
    if car == 'audi':
        print("\nSorry we dont have audi.")
    else:
        print(f"We have {car} for sale.")  # this will run through all 4 cars

#9/11/2020
print('\n')
toppings = []  # empty list, we are checking to see if it's empty with "if"
if toppings:  # checks to see if theres ANYTHING at all
    for topping in toppings:  # if there is, goes to this for loop
        print(f"Adding {topping}.")

else:  # THIS MUST BE SAME INDENT AS IF. if empty list, goes to else
     print("Well you have a plain ol' cheese pizza!")
print("Finished making your pizza!")

available = ['ham','onions', 'olives']
requested = ['peppers', 'ham', 'onions']
for item in requested:  # uses 'item' to become each element in 'requested'
    if item in available:  # if 'item' is
      print(f"{item.title()} is added!")
    else:
        print(f"We dont have {item}.")

