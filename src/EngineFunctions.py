import lyricsgenius
from lyricsgenius import Genius
from API import Genius_API_Key


# searches top 20 songs with the keyword "songs" and prints out the title of the songs
def testSongs():
    genius = lyricsgenius.Genius(Genius_API_Key.token)
    genius.verbose = False

    songs = genius.search_songs("girl", per_page=50)

    for song in songs['hits']:
        print("Song:", song['result']['full_title'], "\nArtist:", song['result']['artist_names'], "\n")
