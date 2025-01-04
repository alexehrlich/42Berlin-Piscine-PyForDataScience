from load_csv import load
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def convert(value: str) -> float:
    """Convert a string wiht suffix to a float"""
    if value.endswith('k'):
        return float(value[:-1])*1_000
    if value.endswith('M'):
        return float(value[:-1])*1_000_000
    if value.endswith('B'):
        return float(value[:-1])*1_000_000_000
    else:
        return float(value)


def main():
    """Display the population of France vs. Germany from 1800 to 2050"""
    df = load('population_total.csv')
    df_numeric = df.copy().map(convert)
    x = range(1800, 2051)
    plt.plot(x, df_numeric.loc['Germany', '1800':'2050'], label='Germany')
    plt.plot(x, df_numeric.loc['France', '1800':'2050'], label='France')
    plt.xlabel('Years')
    plt.ylabel('Population')
    plt.title('Population Germany vs. France')
    plt.legend()
    formatter = ticker.FuncFormatter(lambda x, pos: f'{x/1_000_000:.0f}M')
    plt.gca().yaxis.set_major_formatter(formatter)
    plt.show()


if __name__ == "__main__":
    main()
