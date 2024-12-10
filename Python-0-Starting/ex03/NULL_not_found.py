def NULL_not_found(object: any) -> int:
	prefix = ""
	if object == None:
		prefix = f"Nothing : "
	elif object != object: #special: Nan is not equal to itself
		prefix = "Cheese : "
	elif object == 0:
		prefix = "Zero : "
	elif object == "":
		prefix = "Empty : "
	elif object == False:
		prefix = "Fake : "
	else:
		print("Type not found")
		return 1

	print(prefix + f"{object} " + f"{type(object)}")
	return 0