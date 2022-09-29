# DFA Implementation Variables

# 5-tuple variables for DFA
class DFA:
    states = []
    alphabet = []
    startState = ""
    acceptStates = []
    transitionFcn = {}

    def __init__(self):
        print("Enter names of the DFA states separated by space character: ")
        self.states = input().split()
        # The input is split into a list of DFA states

        print("Enter the characters of the DFA alphabet separated by space "
              "character: ")
        self.alphabet = input().split()
        # alphabet is a list of characters

        # Start state
        print("Enter the start state: ")
        self.startState = input()

        # Accept states
        print("Enter the accept states seperated by spaces: ")
        self.acceptStates = input().split()

        # Inputting the Transition Function Table
        # Reject states represented as 'None' in dictionary
        print(
            "Enter the transitions for the following states (enter . for reject"
            " state)")
        for state in self.states:
            for alpha in self.alphabet:
                print(f"\t {alpha}")
                print(f"{state}\t--->\t", end="")
                dest = input()

                if dest == ".":
                    self.transitionFcn[(state, alpha)] = None
                else:
                    self.transitionFcn[(state, alpha)] = dest

    def run(self, word):
        currentState = self.startState

        for char in word:  # transition using current state and input char
            print(f"State: {currentState}, next input: {char}", end="->")
            currentState = self.transitionFcn[(currentState, char)]
            print(f"new state: {currentState}")

        # check if DFA goes into rejected state
        if currentState is None:
            print("Reject State")
        else:  # check whether final state is accepted state
            if currentState in self.acceptStates:
                print("Accepted")
            else:
                print("Rejected")
