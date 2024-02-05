import pandas as pd

# import data
df = pd.read_csv(r"C:\Users\Claire\Documents\upskilling_projects\SU_summer_school\data_01\movie_dataset.csv")
df.fillna

# Q1
high_rating = df[df['Rating'] == df['Rating'].max()]
print("Question 1: ")
print(high_rating['Title'])

# Q2
df.fillna(df['Revenue (Millions)'], inplace=True)
ave = df['Revenue (Millions)']/(df['Rank'].loc[:-1])
df.describe()

# Q3
df_yr = df.copy()
df_yr = df_yr[(df_yr['Year'] > 2014) & (df_yr['Year'] < 2018)]
df_yr.describe()

# Q4
df_2016 = df.copy()
df_2016 = df_2016[(df_2016['Year'] == 2016)]
num_2016 = len(df_2016)
print("Question 4: ")
print(num_2016)

# Q5
df_cn = df[df['Director'].str.contains("Christopher Nolan")]
df_cn.describe()
num_nolan = len(df_cn)
print("Question 5: ")
print(num_nolan)

# Q6
df_8 = df.copy()
df_8 = df_8[(df_8['Rating'] > 7.9)]
num_rating = len(df_8)
print("Question 6: ")
print(num_rating)

# Q7
df_cn.describe()

# Q8
if 'Year' in df.columns and 'Rating' in df.columns:
    average_ratings_per_year = df.groupby('Year')["Rating"].mean()

    highest_year = average_ratings_per_year.idxmax()

print("Question 8: ")
print(highest_year)

# Q9
v06 = df['Year'].value_counts()[2006]
v16 = df['Year'].value_counts()[2016]

pct_ch = ((v16 - v06) / v06) * 100

print("Question 9: ")
print(pct_ch)

# Q10
if 'Actors' in df.columns:
    all_actors = df['Actors'].str.split(', ')

    actor_ls = [actor for sublist in all_actors.dropna() for actor in sublist]

    actors_series = pd.Series(actor_ls)
    most_common_actor = actors_series.mode()[0]

print("Question 10: ")
print(most_common_actor)

# Q11
gen_ls = []
unique_ls = []

for i in df['Genre']:
    genre = i.split(',')
    gen_ls = gen_ls + genre

for x in gen_ls:
    if x not in unique_ls:
        unique_ls.append(x)

count = len(unique_ls)
print("Question 11: ")
print(count)

# Q12
corr = df.corr(method = 'pearson')

print("Question 12: ")
print(corr)