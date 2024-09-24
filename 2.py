import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

file_path = 'MSW/olympics_dataset.csv'
df = pd.read_csv(file_path)

# Moje osobni kontrola, zda dataset byl importovan a nacten
# print(df.head())


# Rozdil poctu ucastniku v zavislosti na roce a pohlavi
gender = df.groupby(['Year', 'Sex']).size().unstack(fill_value=0)
gender.plot(kind='line', figsize=(10,5))
plt.title('Pohlavi ucastniku')
plt.ylabel('Pocet ucastniku')
plt.show()


# Top 10 sportu podle cisla ucastniku
sport_count = df['Sport'].value_counts().head(10)
sns.barplot(x=sport_count.values, y=sport_count.index)
plt.title('Top 10 sportu podle poctu ucastniku')
plt.xlabel('Pocet ucastniku')
plt.show()


# Pocet medailistu podle pohlavi
medaile_podle_pohlavi = df[df['Medal'] != 'No medal'].groupby('Sex').size()
medaile_podle_pohlavi.plot(kind='pie', autopct='%1.1f%%', figsize=(6,6))
plt.title('Pocet medailistu podle pohlavi')
plt.show()


# Top 10 sportu podle poctu medailistu
top_sporty = df[df['Medal'] != 'No medal']['Sport'].value_counts().head(10)
plt.figure(figsize=(10,6))
sns.barplot(x=top_sporty.values, y=top_sporty.index)
plt.title('Top 10 Sportu podle medaili')
plt.xlabel('Pocet medailistu')
plt.ylabel('Sport')
plt.show()


# Zjistuji jake jsou mozne hodnoty u medaili v df
# print(df['Medal'].unique())
df_clean = df[df['Medal'].notna() & (df['Medal'] != 'No medal')]
medals_by_year = df_clean.groupby('Year').size()

# Pocet vydanych medaili podle roku
plt.figure(figsize=(10,6))
sns.lineplot(x=medals_by_year.index, y=medals_by_year.values)
plt.title('Pocet vydanych medaili podle roku')
plt.xlabel('Rok')
plt.ylabel('Pocet medaili')
plt.show()
