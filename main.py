import pandas as pd
imdb_df = pd.read_csv('data\IMDb movies.csv', low_memory=False)

def get_recommendation()

def main():
    print("Movie recommendation program")
    name = input('What is your name?')
    print('Hi, ', name, '!')
    #age
    #time periodgit st
    #language
    genre = input('What is your favourite genre?')
    try:
        get_recommendation(recommendation = imdb_df[imdb_df['genre'] == genre].sort_values(by='reviews_from_critics', ascending=False).head(1)[
            'original_title']
        print("Here is our recommendation: ", recommendation)
    except Exception as e:
        ("No matching movies :( Try different genre?")
        print(e)

if __name__ == "__main__":
    main()