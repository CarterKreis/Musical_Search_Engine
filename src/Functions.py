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
"""
import lyricsgenius
from lyricsgenius import Genius
from collections import Counter
import Genius_API_Key


# searches top 20 songs with the keyword "songs" and prints out the title of the songs
def testSongs():
    genius = lyricsgenius.Genius(Genius_API_Key.token)
    genius.verbose = False

    songs = genius.search_songs("girl", per_page=50)

    for song in songs['hits']:
        print("Song:", song['result']['full_title'], "\nArtist:", song['result']['artist_names'], "\n")

def most_common_word_from_song(artist, song): #ian
    genius = lyricsgenius.Genius(Genius_API_Key.token, verbose=False, remove_section_headers=True, skip_non_songs=True)


    popular_song = genius.search_song(artist, song)


    if popular_song:

        words = popular_song.lyrics.lower().split()
        word_counts = Counter(words)

        most_common, count = word_counts.most_common(1)[0]

        print(
            f"The most common word in '{popular_song.title}' by {popular_song.artist} is '{most_common}' with {count} occurrences.")
    else:
        print(f"Song '{song}' by {artist} not found on Genius.")

def most_common_word_from_album(artist, album): #Ian
    genius = lyricsgenius.Genius(Genius_API_Key.token, verbose=False, remove_section_headers=True, skip_non_songs=True)
    songs_albums = genius.search_album(artist, album).tracks
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    combined_lyrics = ' '.join(''.join(char.lower() for char in word if char in letters) for song in songs_albums)

    word_counts = Counter(combined_lyrics.split())

    most_common_word, count = word_counts.most_common(1)[0]

    print(f"The most common word in '{album}' by {artist} is '{most_common_word}' with {count} occurrences.")


def number_of_reviews(artist, album):
    genius = lyricsgenius.Genius(Genius_API_Key.token, verbose=False, remove_section_headers=True, skip_non_songs=True)
    album_info = genius.search_album(artist, album)

    song = genius.search_song(album, artist)

    if song:
        return song.stats
    else:
        print(f"No information found for the song '{album}' by {artist}.")
        return None


def does_song_exist(artist, album):
    genius = lyricsgenius.Genius(Genius_API_Key.token, verbose=False, remove_section_headers=True, skip_non_songs=True)
    album_search = genius.search_album(artist, album)

    if album_search:
        print(f"'{album}' by {artist} has been made.")

    else:
        print(f"'{album}' by {artist} has not been made yet!")

def common_words(artist, song1, song2):
    genius = lyricsgenius.Genius(Genius_API_Key.token, verbose=False, remove_section_headers=True, skip_non_songs=True)
    lyrics1 = genius.search_song(song1, artist)
    lyrics2 = genius.search_song(song2, artist)

    map1 = Counter(lyrics1.lyrics.lower().split())
    map2 = Counter(lyrics2.lyrics.lower().split())

    # Calculate common words
    shared_words=""
    for key in map1:
        if key in map2:
            shared_words+=key+", "
    shared_words=shared_words[0:len(shared_words)-2]
    print(f"Shared words in '{song1}' and '{song2}': {shared_words}")


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
"""







