import pandas as pd
import inquirer
imdb_df = pd.read_csv('data\IMDb movies.csv', low_memory=False)
from user import User
from preferences import Preferences

#def get_log():
#    fp = open('log.csv', 'wa')
 #   writer = csv.writer(fp)
 #   somelist = [name,age,genre,language,year,recommendation,rent]
 #   writer.writerow((somelist))

def get_recommendation():
    recommendation = []
    if genre and language and year:
        recommendation = imdb_df[(imdb_df['genre'].str.contains(genre)) & (imdb_df['language'].str.contains(language)) & (imdb_df['year']==year)].sort_values(by='reviews_from_critics', ascending=False).head(1)[
            'original_title']

    elif genre and language:
        recommendation = imdb_df[
            (imdb_df['genre'].str.contains(genre)) & (imdb_df['language'].str.contains(language))].sort_values(by='reviews_from_critics', ascending=False).head(1)[
            'original_title']

    elif genre and year:
        recommendation = imdb_df[
            (imdb_df['genre'].str.contains(genre)) & (
                        imdb_df['year'] == year)].sort_values(by='reviews_from_critics', ascending=False).head(1)[
            'original_title']

    elif language and year:
        recommendation = imdb_df[(imdb_df['language'].str.contains(language)) &
            (imdb_df['year'] == year)].sort_values(by='reviews_from_critics', ascending=False).head(1)[
            'original_title']

    elif language:
        recommendation = imdb_df[imdb_df['language'].str.contains(language)].sort_values(by='reviews_from_critics',
                                                                        ascending=False).head(1)[
            'original_title']

    elif year:
        recommendation = imdb_df[imdb_df['year'].str.contains(year)].sort_values(by='reviews_from_critics',
                                                                        ascending=False).head(1)[
            'original_title']

    elif genre:
        recommendation = imdb_df[imdb_df['genre'].str.contains(genre)].sort_values(by='reviews_from_critics',
                                                                        ascending=False).head(1)[
            'original_title']
    return recommendation

def  rent_option():
    global rent
    questions = [
        inquirer.List('rent',
                      message="Would you like to rent this movie?",
                      choices=['Yes', 'No'],
                      ),
    ]
    answers = inquirer.prompt(questions)
    rent = answers["rent"]
    if answers["rent"]== "Yes":
        print("Great! That costs 1,5 EUR")
    else:
        print("Nevermind. Come back later!")

def get_know_user():
    global name
    global age
    name = input('What is your name?')
    age = input('What is your age?')
    user = User(name, age)
    return user

def get_preferences():
    global year
    global genre
    global language
    year = input("What year?")
    genre = input("What genre would you like to watch?")
    language = input("What should be the original language?")
    preferences = Preferences(name, language, year, genre)
    return preferences


def main():

    print("Movie recommendation program")
    get_know_user()
    print("Let's figure out your movie preferences")
    get_preferences()
    recommendation = get_recommendation()
    print("Here is our recommendation: ", recommendation)
    rent_option()
    #get_log()



if __name__ == "__main__":
    main()