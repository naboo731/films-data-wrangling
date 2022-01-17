from tokenize import group
import pandas as pd
import os

CSV_PATH = os.path.abspath("Film Locations in San Fran.csv")
df = pd.read_csv(CSV_PATH)
# print(df.tail(5))


def exploration():
    print(df.shape)
    print(df.info)


# exploration()


def grouping_films_productionCo():
    grouped_productionCos = df.groupby('Production Company')
    print(grouped_productionCos)


grouping_films_productionCo()
