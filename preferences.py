class Preferences:
    def __init__(self, name):
        self.name = name
        print("Finding a good movie for ", self.name)

    def get_language(self):
        language = input("What should be the original language?")
        print("language") # change to return, this is for error handling

    def get_year(self):
        # expand later on
        year = input("What year?")

    def get_budget(self):
        # classify later
        budget = input("What budget?")

    def get_genre(self):
        genre = input("What genre?")

    def get_vote_type(self):
        # from users or critics or their avg
        vote_type = input("Which vote type?")

    def get_gross(self):
        # usa gross or worldwide gross? separate columns
        # if want English lang film, then add USA gross or otherwise worldwide gross
        gross_amount = input("How much for minimum gross?")

    def get_production_company(self):
        # like Disney
        prod_company = input("Are you looking for a movie from a specific production company?")

# extras for later
# director - see who are the top 10 directors or directors with more than X movies
# genre is sometimes 3 types combined so right now those aren't picked up

