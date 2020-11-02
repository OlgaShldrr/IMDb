
import pandas as pd
from User import User
from preferences import Preferences

imdb_df = pd.read_csv('data\IMDb movies.csv', low_memory=False)


#def get_log():
#    fp = open('log.csv', 'wa')
 #   writer = csv.writer(fp)
 #   somelist = [name,age,genre,language,year,recommendation,rent]
 #   writer.writerow((somelist))

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

def get_genre(data_df, genres):
    genre_list = str(genres).split()
    genre_rec = data_df[data_df['genre'].isin(genre_list)]
    return genre_rec


def get_language(data_df, languages):
    language_list = str(languages).split()
    lang_rec = data_df[data_df['language'].isin(language_list)]
    return lang_rec


def get_year(data_df, years):
    year_list = str(years).split()
    year_rec = data_df[data_df['year'].isin(year_list)]
    return year_rec


def get_preferences(user):
    #global years
    #global genres
    #global languages
    years = input("What year?")
    genres = input("What genre would you like to watch?")
    languages = input("What should be the original language?")
    preferences = Preferences(user.name, languages, years, genres)
    return preferences


def get_recommendation(rec_df, preferences): # add argument, instead of line 33
    recommendation = []
    if preferences.genres:
        rec_df = get_genre(rec_df, preferences.genres)
    if preferences.languages:
        rec_df = get_language(rec_df, preferences.languages)
    if preferences.years:
        rec_df = get_year(rec_df, preferences.years)

    # rec = rec_df.head(1)['original_title'] # if we want only the title
    rec = rec_df.head(10)[['original_title', 'year', 'genre']] # check that the filtering worked
    return rec





def rent_option():
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



def main():

    print("Movie recommendation program")
    user = get_know_user()
    age_verification(user)
    print("Let's figure out your movie preferences")
    preferences = get_preferences(user)
    recommendation = get_recommendation(imdb_df, preferences)
    print("Here is our recommendation: ", recommendation)
    rent_option()
    #get_log()



if __name__ == "__main__":
    main()