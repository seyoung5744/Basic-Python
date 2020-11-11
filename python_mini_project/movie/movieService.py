import python_mini_project.movie.movieDao as md

class MovieService:
    def __init__(self):
        self.dao = md.MovieDao()
        # self.uI = u.UI()

    def getMovieInfo(self, title):
        movie_info = self.dao.getMovie(title) # 저장된 객체 인덱스 반환
        # uI.printUI(movie_info)
        return movie_info

