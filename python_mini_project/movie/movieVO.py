'''
영화 제목, 영화 평점
'''
class Movie:
    # 제목, 개봉, 등급, 장르, 국가, 러닝타임, 배급, 소개
    def __init__(self, title, release, film_rate, genre, nation, running_time, distribution, introduction):
        self.__title = title
        self.__release = release
        self.__film_rate =  film_rate
        self.__genre =  genre
        self.__nation =  nation
        self.__running_time =  running_time
        self.__distribution =  distribution
        self.__introduction = introduction

    def printMovie(self):
        print(self.__title)
        print("",)
