cancel = False
class_list = []

while (True):
    name = input("provide name, ")
    age = input("provide age, ")
    race = input("provide race,  ")
    

    class_list.append({
        "name": name,
        "age": age,
        "race": race,
    })

    cont = input("Want to add another? (Y/N)")
    if cont == "N":
        break;
print()
print(class_list)
print()
print("This is the list sorted by race")
epic = sorted(class_list, key=lambda k:(k['race']))
print(epic)
