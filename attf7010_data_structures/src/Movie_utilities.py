"""
-------------------------------------------------------
Movie Class Utility Functions
-------------------------------------------------------
Author:  Evan Attfield
ID:      180817010
Email:   attf7010@mylaurier.ca
__updated__ = "Jan 15, 2019"
-------------------------------------------------------
"""
from Movie import Movie

def get_movie():
    """
    -------------------------------------------------------
    Creates a Movie object by requesting data from a user.
    Use: movie = get_movie()
    -------------------------------------------------------
    Returns:
        movie - a Movie object based upon the user input (Movie).
    -------------------------------------------------------
    """

    title = input('Title: ')
    year = int(input('Year of release: '))
    director = input('Director: ')
    rating = float(input('Rating: '))
    genres = read_genres()
    
    movie = Movie(title, year, director, rating, genres)

    return movie


def read_movie(line):
    """
    -------------------------------------------------------
    Creates and returns a Movie object from a line of formatted string data.
    Use: movie = read_movie(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of movie data in the format
          title|year|director|rating|genre codes (str)
    Returns:
        movie - a Movie object based upon the data from line (Movie)
    -------------------------------------------------------
    """
    movie_list = line.split("|")
    
    title = movie_list[0]
    year =int(movie_list[1])
    director = movie_list[2]
    rating = float(movie_list[3])
    genres = movie_list[4].split(",")
    for i in range(len(genres)):
        genres[i] = int(genres[i])
    
    movie = Movie(title, year, director, rating, genres)

    return movie


def read_movies(fv):
    """
    -------------------------------------------------------
    Reads a file of string data into a list of Movie objects.
    Use: movies = read_movies(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file of movie data (file)
    Returns:
        movies - a list of Movie objects (list of Movie)
    -------------------------------------------------------
    """

    movies = []
    fv.seek(0)
    line = fv.readline()
    line = line.strip()
    
    while line != "":
        movie_list = line.split("|")
    
        title = movie_list[0]
        year =int(movie_list[1])
        director = movie_list[2]
        rating = float(movie_list[3])
        genres = movie_list[4].split(",")
        for i in range(len(genres)):
            genres[i] = int(genres[i])
        
        movie = Movie(title, year, director, rating, genres)
        movies.append(movie)
        
        line = fv.readline()
        line = line.strip()

    return movies


def menu():
    """
    -------------------------------------------------------
    Prints all genres in the Movie.GENRES list. Use for input menus.
    Use: menu()
    -------------------------------------------------------
    Returns:
        None
    -------------------------------------------------------
    """
    print('Genres')
    for i in range(len(Movie.GENRES)):
        print('{}: {}'.format(i, Movie.GENRES[i]))

    return


def read_genres():
    """
    -------------------------------------------------------
    Asks a user to select genres from a list of genres and returns
    an integer list of the genres chosen.
    Use: genres = read_genres()
    -------------------------------------------------------
    Returns:
        genres - sorted numeric list of movie genres (list of int)
    -------------------------------------------------------
    """
    genres = []
    num = input('Enter a genre number (ENTER to quit): ')
    while num != "" or genres == []:
        #int
        if  num.isdigit() == True:
            num = int(num)
            #positive
            if num < 0:
                print('Error: not a positive number.')
            #<10
            elif num > 10:
                print('Error: input must be < 10')
            #no repeat (WORKS :) )
            elif num in genres:
                print('Error: genre already chosen')
            #else
            else:
                genres.append(num)
        else:
            print('Error: not a positive number.')
        num = input('Enter a genre number (ENTER to quit): ')
    genres.sort()
    return genres


def write_movies(fv, movies):
    """
    -------------------------------------------------------
    Writes the contents of movies to fv. Overwrites or
    creates a new file of Movie objects converted to strings.
    Use: write_movies(fv, movies)
    -------------------------------------------------------
    Parameters:
        fv - an already open file of movie data (file)
        movies - a list of Movie objects (list of Movie)
    Returns:
        None
    -------------------------------------------------------
    """

    # Your code here

    return


def get_by_year(movies, year):
    """
    -------------------------------------------------------
    Creates a list of Movies from a particular year.
    Use: ymovies = get_by_year(movies, year)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        year - the Movie year to select (int)
    Returns:
        ymovies - Movie objects whose year attribute is 
            year (list of Movie)
    -------------------------------------------------------
    """
    ymovies = []
    
    for i in range(len(movies)):
        if movies[i].year == year:
            ymovies.append(movies[i])
    
    return ymovies


def get_by_rating(movies, rating):
    """
    -------------------------------------------------------
    Creates a list of Movies whose ratings are equal to or higher
    than rating.
    Use: rmovies = get_by_rating(movies, rating)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        rating - the minimum Movie rating to select (float)
    Returns:
        rmovies - Movie objects whose rating attribute is 
            greater than or equal to rating (list of Movie)
    -------------------------------------------------------
    """
    rmovies = []
    
    for r in movies: #more efficient than get_by_year lmao
        if r.rating >= rating:
            rmovies.append(r)
    
    return rmovies


def get_by_genre(movies, genre):
    """
    -------------------------------------------------------
    Creates a list of Movies whose list of genres include genre.
    Use: gmovies = get_by_genre(movies, genre)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        genre - the genre code to look for (int)
    Returns:
        gmovies - Movie objects whose genre list includes 
            genre (list of Movie)
    -------------------------------------------------------
    """
    gmovies = []
    
    for g in movies:
        if genre in g.genres:
            gmovies.append(g)

    return gmovies


def get_by_genres(movies, genres):
    """
    -------------------------------------------------------
    Creates a list of Movies whose list of genres include all the genre
    codes in genres.
    Use: m = get_by_genres(movies, genres)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        genres - the genre codes to look for (list of int)
    Returns:
        gmovies - Movie objects whose genre list includes 
            all the genres in genres (list of Movie)
    -------------------------------------------------------
    """
    gmovies = []
    
    for g in movies:
        if genres == g.genres:
            gmovies.append(g)
    
    return gmovies


def genre_counts(movies):
    """
    -------------------------------------------------------
    Counts the number of movies in each genre given in Movie.GENRES.
    Use: counts = genre_counts(movies)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
    Returns:
        counts - the number of Movies in each genre in Movie.GENRES.
            The index of each number in counts is the index of
            the matching genre in Movie.GENRES. (list of int)
    -------------------------------------------------------
    """
    counts = [0,0,0,0,0,0,0,0,0,0]
    
    for i in movies:
        for j in range(len(i.genres)):
            counts[i.genres[j]] += 1
            
    return counts