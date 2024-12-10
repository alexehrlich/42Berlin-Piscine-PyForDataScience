def all_thing_is_obj(object: any) -> int:
	prefix = ""

	if isinstance(object, list):
		prefix = "List : "
	elif isinstance(object, tuple):
		prefix = "Tuple : "
	elif isinstance(object, set):
		prefix = "Set : "
	elif isinstance(object, dict):
		prefix = "Dict : "
	elif isinstance(object, str):
		if object == "Brian":
			prefix = "Brian is in the kitchen : "
		elif object == "Toto":
			prefix = "Toto is in the kitchen : "
	else:
		print("Type not found")
		return 42

	print(prefix + f"{type(object)}")
	return 42
