
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


missing_data = df.isnull().any()
missing_locations = df['Locations'].isnull().value_counts()
missing_fun_facts = df['Fun Facts'].isnull().value_counts()
missing_production = df['Production Company'].isnull().value_counts()
missing_distributor = df['Distributor'].isnull().value_counts()
missing_writers = df['Writer'].isnull().value_counts()
missing_actor1 = df['Actor 1'].isnull().value_counts()
missing_actor2 = df['Actor 2'].isnull().value_counts()
missing_actor3 = df['Actor 3'].isnull().value_counts()
print(f'Location: {missing_locations}, Fun Facts: {missing_fun_facts}, Production: {missing_production}, Distributor: {missing_distributor}, Writer: {missing_writers}, Actor 1: {missing_actor1}, Actor 2: {missing_actor2}, Actor 3: {missing_actor3}')

df.drop('Fun Facts', 1)
