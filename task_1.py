import pandas as pd

# Load dataset
df = pd.read_csv("netflix_titles.csv")

# Basic cleanup
df.drop_duplicates(inplace=True)
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['country'] = df['country'].fillna('Unknown')
df['rating'] = df['rating'].fillna('Unknown')
df['cast'] = df['cast'].fillna('')
df['director'] = df['director'].fillna('Unknown')
df['duration'] = df['duration'].fillna('Unknown')

# Strip text fields
df['title'] = df['title'].str.strip()
df['director'] = df['director'].str.strip()
df['country'] = df['country'].str.strip()

# Convert 'cast' and 'listed_in' into lists
df['cast'] = df['cast'].apply(lambda x: [i.strip() for i in x.split(',')] if x else [])
df['listed_in'] = df['listed_in'].apply(lambda x: [i.strip() for i in x.split(',')] if pd.notnull(x) else [])

# Feature engineering
df['year_added'] = df['date_added'].dt.year
df['month_added'] = df['date_added'].dt.month
df['num_cast'] = df['cast'].apply(len)
df['num_genres'] = df['listed_in'].apply(len)

# Save cleaned dataset
df.to_csv("cleaned_netflix_dataset.csv", index=False)

print("✅ Dataset cleaned and saved as 'cleaned_netflix_dataset.csv'")
