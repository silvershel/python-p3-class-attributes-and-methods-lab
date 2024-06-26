class Song:

    count = 0
    artists = []
    genres = []
    artist_count = {}
    genre_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_artists(self.artist)
        self.add_to_genres(self.genre)
        self.count_songs_by_artist()
        self.count_songs_by_genre()

    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment

    @classmethod
    def add_to_artists(cls, artist):
        cls.artists.append(artist)
    
    @classmethod
    def add_to_genres(cls, genre):
        cls.genres.append(genre)

    @classmethod
    def count_songs_by_artist(cls):
        cls.artist_count = {}
        for artist in cls.artists:
            if artist in cls.artist_count:
                cls.artist_count[artist] += 1
            else:
                cls.artist_count[artist] = 1

    @classmethod
    def count_songs_by_genre(cls):
        cls.genre_count = {}
        for genre in cls.genres:
            if genre in cls.genre_count:
                cls.genre_count[genre] += 1
            else:
                cls.genre_count[genre] = 1



    