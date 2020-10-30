import pandas as pd
imdb_df = pd.read_csv('data\IMDb movies.csv', low_memory=False)
imdb_df

name = input('What is your name?')
genre = input('What is your favourite genre?')
recommendation = imdb_df[imdb_df['genre']==genre].sort_values(by='reviews_from_critics', ascending=False).head(1)['original_title']
print("Here is our recommendation: ", recommendation)