import pandas as pd
imdb_df = pd.read_csv('data\IMDb movies.csv', low_memory=False)
from user import User
from preferences import Preferences

def get_know_user():
    global name
    name = input('What is your name?')
    age = input('What is your age?')
    user = User(name, age)


def main():
    print("Movie recommendation program")
    get_know_user()
    print("Let's figure out your movie preferences")
    preference = Preferences(name)
    #language = Preferences.get_language()
    #genre = str(Preferences.get_genre())
    #year = Preferences.get_year()
    genre = input('What is your favourite genre?')
    try:
        recommendation = imdb_df[imdb_df['genre'] == genre].sort_values(by='reviews_from_critics', ascending=False).head(1)[
            'original_title']
        print("Here is our recommendation: ", recommendation)
    except Exception as e:
        ("No matching movies :( Try different genre?")
        print(e)




    #if language and genre and year:
    #    recommendation = imdb_df[(imdb_df['language'].str.contains(language, regex = False)) & (imdb_df['genre'].str.contains(genre, regex = False)) & (imdb_df['year'] == year)].sort_values(by='reviews_from_critics', ascending=False).head(1)['original_title']
    #    print("Here is our recommendation: ", recommendation)
    #else:
    #    print("Doesnt work")







if __name__ == "__main__":
    main()