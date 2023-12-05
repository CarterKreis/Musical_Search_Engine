import lyricsgenius
import time
from lyricsgenius import Genius
from collections import Counter
from API import Genius_API_Key

"""
Carter: coded the outline and finding the songs
verbose=False: turns off print statements from Genius API
remove_section_headers=True: removes headers such as [Chorus], [Verse], etc. from lyrics
skip_non_songs=True: does not return objects believed to not be songs
"""

"""
adjList is implemented through this Map class
This is the Map that we are implementing; canvas had information on insertion
"""


class Map:
    def __init__(self):
        self.list = []

    def insert(self, add_Key, value):
        found = True
        for i, (key, v) in enumerate(self.list):
            if add_Key == key:
                found = False
                self.list[i] = (add_Key, value)
                break  # breaks and found
        if found:
            self.list.append((add_Key, value))

    # checks if key is in the map and returns value if it exists
    def search(self, searchKey):
        for key, value in self.list:
            if searchKey == key:
                return value
        return

    # https://www.geeksforgeeks.org/__getitem__-and-__setitem__-in-python/
    # have to set to support item assignment
    def __setitem__(self, key, value):
        self.insert(key, value)

    def __getitem__(self, key):
        return self.search(key)

    # is a counter that keeps track of length
    def __len__(self):
        return len(self.list)

    def values(self):
        Sum = 0
        for key, value in self.list:
            Sum += value
        return Sum


# Prints artist of the input song if song exists
def find_the_artist(song):  # Ian
    genius = lyricsgenius.Genius(Genius_API_Key.token, verbose=False, remove_section_headers=True, skip_non_songs=True)

    # retrieves given song from Genius API request
    search_song = genius.search_song(song)
    my_map = Map()

    # If the song exists get the artist and print it out
    if search_song:
        my_map[search_song] = search_song  # QQQ
        print(search_song)
        artist = search_song.primary_artist

        if artist:
            print(f"The Artist of '{song}': {artist.name}")
    else:
        print("Not found!")


# Prints the artist of the input song if song exists and uses and Adjacency List
def find_the_artist_graph(song):  # Ian
    genius = lyricsgenius.Genius(Genius_API_Key.token, verbose=False, remove_section_headers=True, skip_non_songs=True)

    # retrieves song and stores in AdjList if exists
    search_song = genius.search_song(song)
    Adjlist = {}
    if search_song:
        Adjlist[search_song] = []
        artist = search_song.primary_artist
        Adjlist[search_song].append(artist)
        print(search_song)

        if artist:
            print(f"The Artist of '{song}': {artist.name}")
    else:
        print("Not found!")


# Retrieves song and prints out most common word from the song
def most_common_word_from_song(artist, song):  # Carter
    genius = lyricsgenius.Genius(Genius_API_Key.token, verbose=False, remove_section_headers=True, skip_non_songs=True)

    # Retrieve song from Genius API
    popular_song = genius.search_song(artist, song)

    # If the song exists use a map to get the amount of times a word appears in the song
    if popular_song:

        words = popular_song.lyrics.lower().split()
        word_counts = Counter(words)  # counter is a map of occurrences

        most_common, count = word_counts.most_common(1)[0]

        print(
            f"The most common word in '{popular_song.title}' by {popular_song.artist} is '{most_common}' with {count} occurrences.")
    else:
        print(f"Song '{song}' by {artist} not found on Genius.")


# Retrieves song and prints out most common word from the song using a AdjList
def most_common_word_from_song_graph(artist, song):  # Carter
    genius = lyricsgenius.Genius(Genius_API_Key.token, verbose=False, remove_section_headers=True, skip_non_songs=True)
    popular_song = genius.search_song(artist, song)

    if not popular_song:
        print("Song not found, please try again")
        return

    words = popular_song.lyrics.lower().split()

    # will be a map of lists
    adjlist = {}

    for i in range(len(words) - 1):
        if words[i] in adjlist:
            adjlist[words[i]].append(words[i + 1])
        else:
            adjlist[words[i]] = []

        # append or create list depending on if element is there
        if words[i + 1] in adjlist:
            adjlist[words[i + 1]].append(words[i])
        else:
            adjlist[words[i + 1]] = []

    most_common_word = ""
    degree = 0

    # Gets the most common word in song from adjList
    for word, neighbors in adjlist.items():
        if len(neighbors) > degree:
            most_common_word = word
            degree = len(neighbors)

    print(
        f"The most common word for '{popular_song.title}' by {popular_song.artist} is '{most_common_word}' with {degree} occurrences.")


# Checks if album exists from a search using album & artist name
def does_album_exist(artist, album):  # Sam
    genius = lyricsgenius.Genius(Genius_API_Key.token, verbose=False, remove_section_headers=True, skip_non_songs=True)
    album_search = genius.search_album(artist, album)

    # if search_album returns anything then print out the album & artist
    my_map = Map()
    my_map[album_search] = album_search if album_search else None
    if album_search:
        print(f"'{album}' by {artist} has been made.")

    else:
        print(f"'{album}' by {artist} has not been made yet!")


# Checks if album exists from a search using album & artist name using a AdjList
def does_album_exist_graph(artist, album):  # Ian
    genius = lyricsgenius.Genius(Genius_API_Key.token, verbose=False, remove_section_headers=True, skip_non_songs=True)
    album_search = genius.search_album(artist, album)

    AdjList = {}

    # Put search_album results into AdjList & print album & artist
    if album_search:
        AdjList[album_search] = []
        AdjList[album_search].append(album_search)

        print(f"'{album}' by {artist} has been made.")

    else:
        print(f"'{album}' by {artist} has not been made yet!")


# Finds common words between two input songs
def common_words(artist, song1, song2):  # Carter
    genius = lyricsgenius.Genius(Genius_API_Key.token, verbose=False, remove_section_headers=True, skip_non_songs=True)
    lyrics1 = genius.search_song(song1, artist)
    lyrics2 = genius.search_song(song2, artist)

    # Counts the lyrics and sets the all to lowercase
    my_map1 = Counter(lyrics1.lyrics.lower().split())
    my_map2 = Counter(lyrics2.lyrics.lower().split())

    # Calculate common words
    shared_words = ""
    for key in my_map1:
        if key in my_map2:
            # if they are the same then add to shared_words string
            shared_words += key + ", "

    shared_words = shared_words[0:len(shared_words) - 2]
    print(f"Shared words in '{song1}' and '{song2}': {shared_words}")


# Finds common words between two input songs using a AdjList
def common_words_graph(artist, song1, song2):  # Sam
    genius = lyricsgenius.Genius(Genius_API_Key.token, verbose=False, remove_section_headers=True, skip_non_songs=True)

    lyrics1 = genius.search_song(song1, artist)
    lyrics2 = genius.search_song(song2, artist)

    words1 = lyrics1.lyrics.lower().split()
    words2 = lyrics2.lyrics.lower().split()

    Adjlist = {}

    # Same as common_words for Map but with AdjList syntax
    for word in words1:
        Adjlist[word] = {song1: 1}
        Adjlist[word][song2] = 0

    for word in words2:
        if word not in Adjlist:
            Adjlist[word] = {song1: 0}
            Adjlist[word][song2] = 1
        else:
            Adjlist[word][song2] += 1

    common_words = [word for word, occurrences in Adjlist.items()]

    print(f"Common words between '{song1}' and '{song2}': {common_words}")


# searches name of artist and gets their top 5 songs
def topFiveSongs(inputArtist):  # Carter

    genius = lyricsgenius.Genius(Genius_API_Key.token, verbose=False, remove_section_headers=True, skip_non_songs=True)
    genius.excluded_terms = ["(Live)"]

    # get Artist object from Genius
    artist = genius.search_artist(inputArtist, max_songs=5)

    print(f"Top 5 songs of {inputArtist}: ")
    my_map = Map()
    # prints titles of songs from retrieved artist
    for song in artist.songs:
        my_map[song.title] = song.title
        print(song.title)


# Gets the top 5 songs of an artist using AdjList
def topFiveSongs_graph(inputArtist):  # Sam
    genius = lyricsgenius.Genius(Genius_API_Key.token, verbose=False, remove_section_headers=True, skip_non_songs=True)
    genius.excluded_terms = ["(Live)"]

    # get Artist object from Genius
    artist = genius.search_artist(inputArtist, max_songs=5)

    print(f"Top 5 songs of {inputArtist}: ")
    AdjList = {}
    for song in artist.songs:
        if song.title not in AdjList:
            AdjList[song.title] = []
        AdjList[song.title].append(song.title)
        print(song.title)


# Get all the songs of an input artist
# Warning: Can Time Out if artist has too many songs
def all_songs(artist_name):  # Sam
    # Create genius object with no print statements included
    # No section headers will be included in lyrics, and non songs will be skipped
    # The object will also skip songs that are "Live" performances
    genius = lyricsgenius.Genius(Genius_API_Key.token, verbose=False, remove_section_headers=True, skip_non_songs=True)
    genius.excluded_terms = ["(Live)"]

    # get Artist object from Genius
    # max at 50 can change to anything
    artist = genius.search_artist(artist_name, max_songs=None)

    my_map = Map()

    for song in artist.songs:
        words = song.lyrics.lower().split()
        word_counts = Counter(words)
        my_map[song.title] = sum(word_counts.values())

    print(f'This artist had {len(my_map)} songs with {(my_map.values())} lyrics')
