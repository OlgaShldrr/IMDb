import pandas as pd
imdb_df = pd.read_csv('data\IMDb movies.csv', low_memory=False)
from user import User
from preferences import Preferences

#ask user name and age
def get_know_user():
    #while True:
    user_name_input = input('What is your name?')
    name = user_name_input.strip() # remove spaces
    if name:
        name = name.capitalize() # name starts with capital
    age = int(input('What is your age?')) #age is integer

    user = User(name, age)
    return user

#age verification
def age_verification(user):
    if int(user.age)>=18:
        print("Welcome ", user.name, "! Thanks for providing your age (",
                  user.age,"). You are above the legal age, so your movie recommendation will be adjusted accordingly")
    else:
        print("Welcome ", user.name, "! Thanks for providing your age (",
                  user.age, "). You are below the legal age, so your movie recommendation will be adjusted accordingly")


def main():
    print("Movie recommendation program")
    user= get_know_user()
    age_verification(user)

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