import sys
import pytest
sys.path.insert(0, "lib")  # This ensures the lib folder is included in the import path

from song import Song  # Import Song from lib/song.py
 
def test_song_initialization():
    song = Song("Bohemian Rhapsody", "Queen", "Rock")
    assert song.name == "Bohemian Rhapsody"
    assert song.artist == "Queen"
    assert song.genre == "Rock"

def test_song_count():
    Song.count = 0  # Reset count before test
    Song("Song 1", "Artist 1", "Genre 1")
    Song("Song 2", "Artist 2", "Genre 2")
    assert Song.count == 2  # Should count 2 songs
