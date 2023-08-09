import random

name = [
    ["Group 1 : A,B,C"],
    ["Group 2 : D,E,F"],
    ["Group 3 : G,H,I"],
    ["Group 4 : J,K,L"],
    ["Group 5 : M,N,O"],
    ["Group 6 : P,Q,R"],
    ["Group 7 : S,T,U"],
    ["Group 8 : V,W,X"],
    ["Group 9 : Y,Z"]
]

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
