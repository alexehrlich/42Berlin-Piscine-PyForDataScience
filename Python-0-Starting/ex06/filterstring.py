from ft_filter import ft_filter
import sys

def read_input(arguments: [str]) -> (str, int):
    assert len(arguments) == 3, "the arguments are bad"
    try:
        num = int(arguments[2])
        return (arguments[1], num)
    except ValueError as ve:
        raise AssertionError("second argument must be an integer")

def main():
    try:
        to_split, word_len = read_input(sys.argv)
        str_arr = to_split.split(' ')
        print([e for e in ft_filter(lambda e: len(e) > word_len, str_arr)])
    except AssertionError as e:
        print(f"AssertionError: {e}")

if __name__ == "__main__":
    main()
