import pandas as pd
imdb_df = pd.read_csv('data\IMDb movies.csv', low_memory=False)
from user import User

def get_know_user():
    name = input('What is your name?')
    age = input('What is your age?')
    user = User(name, age)


def main():
    print("Movie recommendation program")
    get_know_user()


    #time periodgit st
    #language
    genre = input('What is your favourite genre?')
    try:
        recommendation = imdb_df[imdb_df['genre'] == genre].sort_values(by='reviews_from_critics', ascending=False).head(1)[
            'original_title']
        print("Here is our recommendation: ", recommendation)
    except Exception as e:
        ("No matching movies :( Try different genre?")
        print(e)

if __name__ == "__main__":
    main()