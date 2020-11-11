import os

class MovieDao:
    # def __init__(self):
    #     self.mov = []
    #
    # # def select(self, num):
    def getMovie(self, title):
        # os.chdir("movie_info")
        f = open(title+".txt", "r", encoding="utf-8")
        movie_info = f.read()
        f.close()
        os.chdir("../")
        return movie_info



