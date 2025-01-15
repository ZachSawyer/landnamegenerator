import os
import secrets
import json

def clrscr():
    os.system('cls' if os.name == 'nt' else "clear")

def sys_exit():
    clrscr()
    print("Quitting... Goodbye!")
    raise SystemExit

def open_file():
    with open("land_descriptors.json") as f:
        return json.load(f)
    
def land_name():
    name = open_file()
    evil_land_gen = f'The {secrets.choice(name["evil_land_adj"])} Lands of {secrets.choice(name["evil_land_noun"])}\n'
    good_land_gen = f'The {secrets.choice(name["good_land_adj"])} Lands of {secrets.choice(name["good_land_noun"])}\n'
    return evil_land_gen, good_land_gen

def main():
    while True:
        clrscr()
        evil_name, good_name = land_name()
        print(evil_name)
        print(good_name)
        print("Press Enter to Continue Generating Names")
        quit = input("1. Quit\n")
        if quit == "1":
            sys_exit()

if __name__ == '__main__':
    main()