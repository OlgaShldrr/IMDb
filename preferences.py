class Preferences:
    def __init__(self, name, language, year, genre):
        self.name = name
        self.year = year
        self.language = language
        self.genre = genre
        print("Finding a good movie for ", self.name)


    def get_budget():
        # classify later
        budget = input("What budget?")


    def get_vote_type():
        # from users or critics or their avg
        vote_type = input("Which vote type?")

    def get_gross():
        # usa gross or worldwide gross? separate columns
        # if want English lang film, then add USA gross or otherwise worldwide gross
        gross_amount = input("How much for minimum gross?")

    def get_production_company():
        # like Disney
        prod_company = input("Are you looking for a movie from a specific production company?")

# extras for later
# director - see who are the top 10 directors or directors with more than X movies


