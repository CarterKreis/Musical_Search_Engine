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


# searches name of artist and gets their top 5 songs
def topFiveSongs(inputArtist):
    # Create genius object with no print statements included
    # No section headers will be included in lyrics, and non songs will be skipped
    # The object will also skip songs that are "Live" performances
    genius = lyricsgenius.Genius(Genius_API_Key.token, verbose=False, remove_section_headers=True, skip_non_songs=True)
    genius.excluded_terms = ["(Live)"]

    # get Artist object from Genius
    artist = genius.search_artist(inputArtist, max_songs=5)

    print(f"Top 5 songs of {inputArtist}: ")
    for song in artist.songs:
        print(song.title)







