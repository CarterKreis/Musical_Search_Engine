import lyricsgenius
from lyricsgenius import Genius
from API import Genius_API_Key


def testGenius():
    # Examples of using lyricsgenius
    genius = lyricsgenius.Genius(Genius_API_Key.token)

    # artist = genius.search_artist("Andy Shauf", max_songs=2, sort="title", include_features=True)
    # print(artist.songs)

    # genius.search_artist will always choose the same artist
    # e.g. search_artist("Luke") will always return Luke Combs
    num = 5
    for i in range(num):
        artist = genius.search_artist("Luke", max_songs=2)
        print(artist.songs)


if __name__ == "__main__":
    print("Welcome to the Musical Search Engine")

    testGenius()

