#########################################
##### Name:  Fiona Fox                       #####
##### Uniqname: fionafox                    #####
#########################################

class Media:

    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url="No URL", json=None):
        if (json is None):
            self.title = title
            self.author = author
            self.release_year = release_year
            self.url = url
        else:
            try:
                self.title = json['collectionName']
                self.url = json['previewUrl']
            except:
                pass
        self.author = json['artistName']
        self.release_year = json['releaseDate'][:4]


    def info(self):
        return self.title + " by " + self.author + " (" + str(self.release_year) + ")"

    def length(self):
        return 0


class Song(Media):

    def __init__(self, title="No Title", author="No Author",
    release_year="No Release Year", url="No URL", json=None,
    album="No Album", genre="No Genre", track_length=0):
        super().__init__(title, author, release_year, url,json)
        if (json is None):
            self.album = album
            self.genre = genre
            self.track_length = track_length
        else:
            try:
                self.title = json['trackName']
            except:
                pass
            self.album = json['collectionName']
            self.genre = json['primaryGenreName']
            self.track_length = json['trackTimeMillis']

    def info(self):
        return super().info() + " [" + self.genre + "]"

    def length(self):
        len = self.track_length/1000
        return round(len)

class Movie(Media):
    def __init__(self, title="No Title", author="No Author",
    release_year="No Release Year", url="No URL", json=None,
    rating="No Rating", movie_length=0):
        super().__init__(title, author, release_year, url, json)
        if (json is None):
            self.rating = rating
            self.movie_length = movie_length
        else:
            try:
                self.title = json['trackName']
                self.rating = json['contentAdvisoryRating']
                self.movie_length = json['trackTimeMillis']
            except:
                pass
    

    def info(self):
        return super().info() + " [" + str(self.rating) + "]"

    def length(self):
        len = self.movie_length/60000
        return round(len)




# Other classes, functions, etc. should go here
from re import I
import webbrowser
import requests
import json


def getdata(input1, songs, movies, medias, all):
    baseurl = "https://itunes.apple.com/search"
    input1 = input1.lower().replace(" ", "+")
    Param1 = {'term': input1}
    response = requests.get(baseurl, Param1)
    json_str = response.text
    json1 = json.loads(json_str)
    results = json1['results']
    for item in results:
        if item['wrapperType'] == 'track':
                if item['kind'] == 'song':
                    try:
                        song = Song(json=item)
                        songs.append(song)
                    except KeyError:
                        pass
                if item['kind'] == 'feature-movie':
                    try:
                        movie = Movie(json=item)
                        movies.append(movie)
                    except KeyError:
                        pass
                else:
                    try:
                        media = Media(json=item)
                        medias.append(media)
                    except KeyError:
                        pass
        else:
            pass

    accum = 1
    print('SONGS\n')
    if len(songs) == 0:
        pass
    else:
        for song in songs:
            print(accum, song.info())
            accum += 1
            all.append(song)
    print('\nMOVIES\n')
    if len(movies) == 0:
        pass
    else:
        for movie in movies:
            print(accum, movie.info())
            accum += 1
            all.append(movie)
    print('\nOTHER MEDIA\n')
    if len(medias) == 0:
        pass
    else:
        for media in medias:
            print(accum, media.info())
            accum += 1
            all.append(media)

    return all

def preview(songs, movies, medias, all):
            term = input("\nPlease input a result number to launch a preview or enter exit to quit")
            if term.lower().strip() == 'exit':
                exit
            else:
                try:
                    if int(term) in range(len(all)):
                        ind = int(term) - 1
                        item = all[ind]
                        webbrowser.open(item.url)
                except:
                    getdata(term, songs, movies, medias, all)








if __name__ == "__main__":
    songs = []
    movies = []
    medias = []
    all = []


    fname = input("\nPlease input a search term or enter exit to quit")

    if fname.lower().strip() == 'exit':
        exit
    else:
        while fname != 'exit':
            getdata(fname, songs, movies, medias, all) 

            preview(all, songs, movies, medias)
            songs.clear()
            movies.clear()
            medias.clear()
            all.clear()

            fname = input("\nPlease input a search term or enter exit to quit")

