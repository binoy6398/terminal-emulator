import os
from utils import colors 

commands = ["ls","cd","exit","quit","pwd"]


def handleCommands(cmd):
    if cmd == "exit" or cmd == "quit":
        exit()
    if cmd == "pwd":
        print(os.getcwd())
    if cmd == "ls":
        print(f"{colors.OKBLUE}{'  '.join(os.listdir())}{colors.ENDC}")


while True:
    print(f"{colors.OKGREEN}{os.getcwd()} >{colors.ENDC}", end = " ")
    cmd = input()
    if cmd in commands:
        handleCommands(cmd)
    else:
        print("invalid command")
