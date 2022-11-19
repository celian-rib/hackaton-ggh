import pandas as pd
import csv
import sys

def calculate(A, b):
    if (b in A[7]):
        print(A)


def main():
    list = []
    inp = "a"
    while inp != "end":
        inp = input("Enter an aliment: ")
        list.append(inp)

    print(list)
    list = list[:-1]
    print(list)
    df = pd.read_csv('./data/Table Ciqual 2020_ENG_2020 07 07.csv')
    for el in list:
        val = df.loc[df['alim_nom_eng'].str.contains(el, case=False)]
        print(val)

if __name__ == '__main__':
    main()
