from load_csv import load
import matplotlib.pyplot as plt


def main():
    """plots the life expectancy projected on income for 1900
    and the development from 1800 to 2000"""
    df_life_expectancy = load('life_expectancy_years.csv')
    df_income = load(
        'income_per_person_gdppercapita_ppp_inflation_adjusted.csv')

    life_exp_1900 = df_life_expectancy.loc[:, '1900']
    income_1900 = df_income.loc[:, '1900']

    plt.figure(1)
    plt.scatter(income_1900, life_exp_1900)
    plt.xlabel("Income per person")
    plt.ylabel("life expectancy")
    plt.title('1900')
    plt.xscale('log')

    fig, axes = plt.subplots(nrows=2, ncols=5, figsize=(20, 10))
    axes = axes.flatten()

    for idx, year in enumerate(range(1800, 2000, 20)):
        life_exp_year = df_life_expectancy.loc[:, str(year)]
        income_year = df_income.loc[:, str(year)]
        ax = axes[idx]
        ax.scatter(income_year, life_exp_year)
        ax.set_xlabel("Income per person")
        ax.set_ylabel("Life expectancy")
        ax.set_title(f'Year {year}')
        ax.set_xscale('log')

    plt.show()


if __name__ == "__main__":
    main()
