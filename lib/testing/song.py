class Song:
    count = 0  # Class attribute to track the number of songs

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1  # Increment count when a new song is created
