# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import variables
import inputs


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print('Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
def runDFA(automaton, word):
    currentState = automaton.startState

    for char in word:  # transition using current state and input char
        currentState = automaton.transitionFcn[(currentState, char)]

    # check if DFA goes into rejected state
    if currentState is None:
        print("Reject State")
    else:  # check whether final state is accepted state
        if currentState in automaton.acceptStates:
            print("Accepted")
        else:
            print("Rejected")


if __name__ == '__main__':
    dfaTuple = inputs.get_inputs()
    flag = 1  # flag for the menu
    while flag == 1:
        print("Test with string (1) or exit (0)")
        userIn = input()
        if userIn == '1':
            print("Input a valid string: ", end="")
            inputString = input()
            runDFA(dfaTuple, inputString)
        if userIn == '0':
            flag = 0
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
