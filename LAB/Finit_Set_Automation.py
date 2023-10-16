class State:
    def __init__(self, name):
        self.name = name
        self.transitions = {}

    def add_transition(self, input_symbol, next_state):
        self.transitions[input_symbol] = next_state


class Automaton:
    def __init__(self):
        self.start_state = State('start')
        self.accept_state = State('accept')
        self.start_state.add_transition('a', self.accept_state)
        self.accept_state.add_transition('b', self.accept_state)

    def run(self, input_string):
        current_state = self.start_state

        for symbol in input_string:
            if symbol in current_state.transitions:
                current_state = current_state.transitions[symbol]
            else:
                return False

        return current_state == self.accept_state


def main():
    automaton = Automaton()

    # Test cases
    test_strings = ["ab", "aab", "abab", "ba", "ac", "abc", "aabab"]
    
    for test_string in test_strings:
        is_match = automaton.run(test_string)
        print(f"'{test_string}' {'matches' if is_match else 'does not match'} the pattern.")

if __name__ == "__main__":
    main()