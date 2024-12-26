import numpy as np

def slice_me(family: list, start: int, end: int):
    if not isinstance(family, list) or not isinstance(start, int) or not isinstance(end, int):
        raise ValueError(f"Wrong argument types: <list, int, int>. You passed {type(family)}, {type(start)}, {type(end)}")
    np_list = np.array(family)
    print(f"My shape is: {np_list.shape}")
    sliced = np_list[start:end]
    print(f"My new shape is: {sliced.shape}")
    return sliced
