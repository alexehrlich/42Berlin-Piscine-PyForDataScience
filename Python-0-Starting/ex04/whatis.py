import sys

if len(sys.argv) < 2:
	exit()

try:
	try:
		number = int(sys.argv[1])
	except ValueError:
		raise AssertionError("argument is not an integer")
	if len(sys.argv) != 2:
		raise AssertionError("more than one argument provided.")
	print("I'm Odd." if number%2 != 0 else "I'm Even.")
except AssertionError as error:
	print(f"AssertionError: {error}")