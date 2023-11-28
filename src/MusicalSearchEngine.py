import lyricsgenius
from lyricsgenius import Genius
from API import Genius_API_Key


def testGenius():
    # Examples of using lyricsgenius
    # setting verbose to false gets rid of print() statements
    genius = lyricsgenius.Genius(Genius_API_Key.token)
    genius.verbose = False

    # Includes songs where Andy is the main Artist for song
    # Can sort by "title" or "popularity"
    artist = genius.search_artist("Andy Shauf", max_songs=2, sort="title", include_features=True)
    for song in artist.songs:
        song.lyrics = ""
        print(song)

    # genius.search_artist will always choose the same artist
    # e.g. search_artist("Luke") will always return Luke Combs


if __name__ == "__main__":
    print("Welcome to the Musical Search Engine\n")

    testGenius()
