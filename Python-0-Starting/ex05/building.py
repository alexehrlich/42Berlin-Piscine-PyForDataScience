import sys
import string


def read_arguments() -> str:
    if len(sys.argv) == 1:
        text = ""
        try:
            text = input("What text to count?\n")
            return text + "\n"
        except EOFError:
            return text
    assert len(sys.argv) == 2, "more than one argiment provided"
    return sys.argv[1]


def main():
    try:
        text = read_arguments()
        lower_letters = 0
        upper_letters = 0
        punct_signs = 0
        spaces = 0
        digits = 0
        for c in text:
            if c in string.ascii_lowercase:
                lower_letters += 1
            elif c in string.ascii_uppercase:
                upper_letters += 1
            elif c in string.punctuation:
                punct_signs += 1
            elif c in string.digits:
                digits += 1
            elif c in string.whitespace:
                spaces += 1
        print(f"The text contains {len(text)} characters:")
        print(f"{upper_letters} upper letters")
        print(f"{lower_letters} lower letters")
        print(f"{punct_signs} punctuation marks")
        print(f"{spaces} spaces")
        print(f"{digits} digits")
    except AssertionError as error:
        print(f"AssertionError: {error}")
    except EOFError:
        print("No text provided.")


if __name__ == '__main__':
    main()
