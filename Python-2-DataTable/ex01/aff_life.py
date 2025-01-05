import matplotlib.pyplot as plt
from load_csv import load
import numpy as np


def main():
    """Plots the life expectnacy of a country"""
    df = load('life_expectancy_years.csv')
    x_val = df.columns.tolist()
    ls = np.arange(int(x_val[0]), int(x_val[-1]) + 1)
    plt.plot(ls, df.loc['Germany'])
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.title("Life expectancy over Years: Germany")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
