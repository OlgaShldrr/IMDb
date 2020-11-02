import pandas as pd
import inquirer
from openpyxl import load_workbook
imdb_df = pd.read_csv('data\IMDb movies.csv', low_memory=False)
from User import User
from preferences import Preferences

def get_log():
    file_in_out = 'log.xlsx'
    wb = load_workbook(filename=file_in_out)
    ws = wb['log']
    last_row = ws.max_row
    for col_idx, val in enumerate([name,age,genres,languages,years,get_recommendation(imdb_df)['original_title'].to_string(),rent]):
        ws.cell(column=col_idx + 1, row=last_row + 1, value=val)
    wb.save(file_in_out)
    #fp = open('log.csv', 'wa')
    #writer = csv.writer(fp)
    #somelist = [name,age,genre,language,year,recommendation,rent]
    #writer.writerow((somelist))


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

def get_recommendation(rec_df): # add argument, instead of line 33
    recommendation = []
    if genres:
        rec_df = get_genre(rec_df, genres)
    if languages:
        rec_df = get_language(rec_df, languages)
    if years:
        rec_df = get_year(rec_df, years)

    # rec = rec_df.head(1)['original_title'] # if we want only the title
    rec = rec_df.head(10)[['original_title', 'year', 'genre']] # check that the filtering worked
    return rec


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



def main():

    print("Movie recommendation program")
    get_know_user()
    print("Let's figure out your movie preferences")
    get_preferences()
    recommendation = get_recommendation(imdb_df)
    print("Here is our recommendation: ", recommendation)
    rent_option()
    get_log()


def get_know_user():
    global name
    global age
    name = input('What is your name?')
    age = input('What is your age?')
    user = User(name, age)
    return user

def get_preferences():
    global years
    global genres
    global languages
    years = input("What year?")
    genres = input("What genre would you like to watch?")
    languages = input("What should be the original language?")
    preferences = Preferences(name, languages, years, genres)
    return preferences


if __name__ == "__main__":
    main()