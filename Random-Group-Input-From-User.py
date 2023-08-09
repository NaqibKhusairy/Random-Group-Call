import random

gpnum = int(input("Enter the number of groups: "))
name = []

for i in range(gpnum):
    gpname = input("Enter the name for Group : ")
    gpmember = input("Enter the members for Group : ")
    name.append(gpname+" : "+gpmember)

while True:
    print("-------------------------------------")
    AskUser = input("Insert Q to quit or any key to Roll: ")
    print("-------------------------------------")
    AskUser = AskUser.upper()
    
    if AskUser == 'Q':
        break
    else:
        if name:
            random_name = random.choice(name)
            name.remove(random_name)
            print("You rolled:", random_name)
        else:
            print("No more names to roll.")
            break
