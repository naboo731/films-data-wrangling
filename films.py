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


def grouping_films_director():
    grouped_directors = df.groupby('Director')
    print(grouped_directors)


# grouping_films_director()


def films_2000s():
    movies_after_2000 = df.loc[df['Release Year']] >= '2000'
    print(movies_after_2000)

# films_2000s()
