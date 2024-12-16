from typing import Callable, Iterable, TypeVar

T = TypeVar('T')

def ft_filter(function: Callable[[T], bool], iterable: Iterable[T]) -> Iterable[T]:
    if function is None:
        function = bool
    return iter([element for element in iterable if function(element)])
