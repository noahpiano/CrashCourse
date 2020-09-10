magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

    print("THANK YOU PEOPLE")  # as long as everything is indented under for loop, it stays in loop

for value in range(1, 5):  # range() generates consecutive integers from 1 to last-1
    print(value)  # this will print 1 2 3 4 aka first to last-1
print('\n')
for value in range(6):  # with just one number it will return 0 to last-1
    print(value)
numbers = list(range(4))  # list() converts any group of numbers into a list/array
print(numbers)
print('\n')
for value in range(2, 11, 2):  # generates all even numbers btw 1 and 10 (3rd argument in range
    print(value)  #              specifies the spacing between integers
print('\n')

cubes = []
for value in range(1, 11):
    cube = value**3  # to do exponents ^ in Python it must be '**' 2**3=8
    cubes.append(cube)  # append() adds to end of list
print(cubes)
comprehensive = [value**3 for value in range(1,11)]  # this combines previous code into one line
print(comprehensive)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
for player in players[0:3]:  # returns elements 0, 1 and 2
   print(player.title())
for player in players[3:]:  # returns elements 3 to end (4)
    print(player.upper())
for player in players[-1:]:  # returns the last element, second to last would be -2 and so on
    print(player.lower())
team = players[:]  # just a colon returns all of the list, this is how you copy a list
print(f'{team} makes up the whole team!')
