import sys

NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ", "E": ". ",
    "F": "..-. ", "G": "--. ", "H": ".... ", "I": ".. ", "J": ".--- ",
    "K": "-.- ", "L": ".-.. ", "M": "-- ", "N": "-. ", "O": "--- ",
    "P": ".--. ", "Q": "--.- ", "R": ".-. ", "S": "... ", "T": "- ",
    "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ", "Y": "-.-- ",
    "Z": "--.. ",
    "a": ".- ", "b": "-... ", "c": "-.-. ", "d": "-.. ", "e": ". ",
    "f": "..-. ", "g": "--. ", "h": ".... ", "i": ".. ", "j": ".--- ",
    "k": "-.- ", "l": ".-.. ", "m": "-- ", "n": "-. ", "o": "--- ",
    "p": ".--. ", "q": "--.- ", "r": ".-. ", "s": "... ", "t": "- ",
    "u": "..- ", "v": "...- ", "w": ".-- ", "x": "-..- ", "y": "-.-- ",
    "z": "--.. ",
    "0": "----- ", "1": ".---- ", "2": "..--- ", "3": "...-- ", "4": "....- ",
    "5": "..... ", "6": "-.... ", "7": "--... ", "8": "---.. ", "9": "----. "
}


def read_input(arguments: [str]) -> None:
    assert len(arguments) == 2, "the arguments are bad"
    assert all(c.isalnum() or c == ' ' for c in arguments[1]), "the arguments are bad"

def main():
    try:
        read_input(sys.argv)
        result = ""
        for c in sys.argv[1]:
            result += NESTED_MORSE[c]
        print(result[:-1])
    except AssertionError as e:
        print(f"AssertionError: {e}")

if __name__ == '__main__':
    main()