class PluralizationFSM:
    def __init__(self):
        self.current_state = 'start'

    def transition(self, word):
        if word.endswith(('s', 'x', 'z', 'sh', 'ch')):
            return word + 'es'
        else:
            return word + 's'


def main():
    fsm = PluralizationFSM()

    # List of nouns to pluralize
    nouns = ["cat", "dog", "box", "dish", "bus", "church"]

    print("Original Noun\tPlural Form")

    for noun in nouns:
        plural_form = fsm.transition(noun)
        print(f"{noun}\t\t{plural_form}")

if __name__ == "__main__":
    main()