import os

class MovieDao:
    # def __init__(self):
    #     self.mov = []
    #
    # # def select(self, num):
    def getMovie(self, title):
        print(os.getcwd())
        # os.chdir("../data/movie")
        f = open("../data/movie/" + title+".txt", "r", encoding="utf-8")
        print(os.getcwd())
        movie_info = f.read()
        f.close()
        return movie_info



