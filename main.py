# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from DFA import DFA
# import inputs


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print('Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


if __name__ == '__main__':
    myDFA = DFA()
    flag = 1  # flag for the menu
    while flag == 1:
        print("Test with string (1) or exit (0)")
        userIn = input()
        if userIn == '1':
            print("Input a valid string: ", end="")
            inputString = input()
            myDFA.run(inputString)
        if userIn == '0':
            flag = 0
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
