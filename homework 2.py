names = ['Alissa', 'Ben', 'Charlie', 'Diaanna']
rooms = ['B', 'D', 'B', 'A']

key = 'Charlie'

index = 0
found = False
while not found and index < len(names):
    if names[index] == key:
        found = True
    else: 
        index += 1
if found:
    print(rooms[index])
