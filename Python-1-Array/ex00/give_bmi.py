import numpy

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
	if all(isinstance(h, int) for h in height) and all(isinstance(w, int) for w in weight):
		is_int = True
	elif all(isinstance(h, float) for h in height) and all(isinstance(w, float) for w in weight):
		is_int = False
	else:
		raise ValueError("Mismatched types in lists")
	if len(height) != len(weight):
		print("Warning: Lists do not have the same length. The last values of the longer list are ignored.")
	bmi = []
	for h, w in zip(height, weight):
		if is_int:
			bmi.append(int(w/(h**2)))
		else:
			bmi.append(w/(h**2))
	return bmi

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
	if all(isinstance(value, (int, float)) for value in bmi):
		return [True if item > limit else False for item in bmi]
	else:
		raise ValueError("Passed list must be consistantly of type int or float")
