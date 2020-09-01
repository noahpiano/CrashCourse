# 8/25/2020
print("\n" + "Try it yourself\n")
print("Hello World")
name = "noah ballou"
print(name.title())
print(name.upper())
famous_person = 'Seinfeld'
quote = 'Newman!'
print(famous_person + " " + quote)

print("\n" + "NUMBERS AND MATH")
print(3 ** 2)  # this is how you do exponents i.e. 3 to the 2nd power
print(6 / 3)  # you always get a float when you divide
print(1 + 2.0)  # as well as include in operation
Bill = 1_000_000_000  # python prints the normal number, the underscore
print(Bill)  # just helps organize if you like. Only for Python 3.6+
x, y, z = 1, 2, 3  # you can initiate multiple variables this way
print(x + y + z)
CONSTANT = 10  # Python coders use all uppercase for constants

# 8/27/2020
print("\n" + "LISTS")
bicycles = ['trek', 'cannondale', 'redline', 'specialized']  # square brackets indicate list, elements
#                                                              separated by comma
print(bicycles)  # prints everything in bicycles including the brackets and quotes
print(bicycles[0])  # prints the first element
print(bicycles[0].title())  # prints in title case
print(bicycles[-1])  # "-1" in index always returns the last item in list
#                       -2 returns second-to-last, -3 third to last etc
message=f"My first bicycle was a {bicycles[0].title()}"
print(message)
bicycles[1]='huffy'  # change second element in list
print(bicycles)
bicycles.append('schwinn')  # append() -- ad new element to end of list
print(bicycles)
emptyList = []  # create list with no elements
bicycles.insert(2, 'cannondale')  # insert new element into 3rd index location from the left
print(bicycles)
del bicycles[1]  # deletes second element from list
print(bicycles)
popped_bicycle = bicycles.pop()  # pop()-removes the last element and keeps it as its own thing
print(bicycles)  # last element is now gone
print(popped_bicycle)
current_bike = bicycles.pop(0)  # can specify index of pop()
print(f"My current bike is a {current_bike.title()}.")  # pay attention to how you format this code!
bicycles.remove('specialized')  # remove() allows you to remove by specifying value of element instead
#                                 of index location. you can also work with the removed value like pop()
#                                 NOTE: the remove() method deletes just the first occurance, not all
print(bicycles)

print("\n" + "TRY IT YOURSELF")
guests=['abby', 'bill', 'colin']

print(guests[0].title() + guests[1].title() + guests[2])

# 9/1/2020
print("\nOrganizing Lists")
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()  # permanently sorts the list into alphabetical order
print(cars)
cars.sort(reverse=True)  # sorts in reverse alphabetical order
print(cars)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))  # length of array, starting with 1.

print("\n" + "TRY IT YOURSELF")
world = ['Greenland', 'Sweden', 'England', 'New Zealand', "Cuba"]
print(world)
print(sorted(world))
print(world)
print(sorted(world,reverse=True))
print(world)  # the list always reverts back after these specific commands
print(sorted(world,reverse=True))
world.sort()  #this command is how you make it permanent -- x.sort()
print(world)
world.sort(reverse=True)
print(world)
print(f'I have {len(world)} places I want to go in the world.')
