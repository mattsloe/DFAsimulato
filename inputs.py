# pre: parameter of dfaTuple[states,alphabet,startState,acceptStates,
# transitionFcn]
# post: returns DFA initialized by user
def get_inputs():
    states = []
    alphabet = []
    startState = ""
    acceptStates = []
    transitionFcn = {}

    print("Enter names of the DFA states separated by space character: ")
    states = input().split()
    # The input is split into a list of DFA states

    print("Enter the characters of the DFA alphabet separated by space "
          "character: ")
    alphabet = input().split()
    # alphabet is a list of characters

    # Start state
    print("Enter the start state: ")
    startState = input()

    # Accept states
    print("Enter the accept states seperated by spaces: ")
    acceptStates = input().split()

    # Inputting the Transition Function Table
    # Reject states represented as 'None' in dictionary
    print("Enter the transitions for the following states (enter . for reject "
          "state)")
    for state in states:
        for alpha in alphabet:
            print(f"\t {alpha}")
            print(f"{state}\t--->\t", end="")
            dest = input()

            if dest == ".":
                transitionFcn[(state, alpha)] = None
            else:
                transitionFcn[(state, alpha)] = dest
    Mtuple = [states, alphabet, startState, acceptStates, transitionFcn]
    return Mtuple


if __name__ == '__main__':
    import DFA
    dfaTuple = get_inputs()
    print(f"states: {dfaTuple.states}")
    print(f"alphabet: {dfaTuple.alphabet}")
    print(f"start state: {dfaTuple.startState}")
    print(f"accept states: {dfaTuple.acceptStates}")
    print(f"transition fcn: {dfaTuple.transitionFcn}")

