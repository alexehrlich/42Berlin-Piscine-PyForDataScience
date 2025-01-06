from typing import Any


def mean(values: list) -> float:
    """Defines the average value of a dataset"""
    return sum(values) / len(values)


def variance(values: list) -> float:
    """Measures the average quadratic deviation of the data from the mean"""
    mean_val = mean(values)
    return sum((x - mean_val) ** 2 for x in values) / (len(values) - 1)


def std_deviation(values: list) -> float:
    """Measures the average deviation of the data from the mean.
    The square root of the variance."""
    return variance(values) ** 0.5


def median(values: list) -> float:
    """Defines the middle value of a sorted datset.
    The 50% Quartile. 50% of the data lies below that value."""
    mid_positon = len(values) / 2
    if len(values) % 2 != 0:
        return values[int(mid_positon)]
    else:
        return (values[int(mid_positon - 1)] + values[int(mid_positon)]) / 2


def quartile(values: list) -> [float]:
    """Q1 defines the value below at max 25% the data lies.
    Q2 defines the value below at max 75% the data lies.
    The needs to be sorted."""
    mid_positon = len(values) // 2
    if len(values) % 2 == 0:
        return [median(values[:mid_positon]), median(values[mid_positon:])]
    else:
        return [median(values[:mid_positon]),
                median(values[mid_positon + 1:])]


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Takes quantity of unknown number and make the Mean, Median,
    Quartile (25% and 75%), Standard Deviation and Variance
    according to the **kwargs"""
    statistics = {
        'mean': mean,
        'median': median,
        'quartile': quartile,
        'var': variance,
        'std': std_deviation
    }

    if not all(isinstance(x, (int, float)) for x in args):
        print("Error: Values must be numbers.")
        return
    if len(args) < 2:
        print("Error: Pass at least 2 values to calculate the statistics")
        return
    values = sorted(args)

    if not kwargs:
        print("No statisitcal function provided.")
        return

    for key, stat in kwargs.items():
        if stat in statistics.keys():
            print(f"{stat}: {statistics[stat](values)}")
        else:
            print(f"Error: {stat} is no valid stat.")
