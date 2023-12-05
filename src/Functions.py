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
import time
from lyricsgenius import Genius
from collections import Counter
import Genius_API_Key

#Carter, i coded the outline and finding the songs
# searches top 20 songs with the keyword "songs" and prints out the title of the songs
def find_the_artist(song): #Sam
    genius = lyricsgenius.Genius(Genius_API_Key.token, verbose=False, remove_section_headers=True, skip_non_songs=True)

    search_song = genius.search_song(song)
    Map={}
    if search_song:
        Map[search_song]=search_song
        print(search_song)
        artist = search_song.primary_artist

        if artist:
            print(f"The Artist of '{song}': {artist.name}")
    else:
        print("Not found!")




def find_the_artist_graph(song):    #ian
    genius = lyricsgenius.Genius(Genius_API_Key.token, verbose=False, remove_section_headers=True, skip_non_songs=True)
    start = time.time()
    search_song = genius.search_song(song)
    Adjlist={}
    if search_song:
        Adjlist[search_song]=[]
        artist = search_song.primary_artist
        Adjlist[search_song].append(artist)
        print(search_song)


        if artist:
            print(f"The Artist of '{song}': {artist.name}")
    else:
        print("Not found!")
    end = time.time()
    print(end - start)



def testSongs(): #carter
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
        word_counts = Counter(words)    #counter is a map of occurences

        most_common, count = word_counts.most_common(1)[0]

        print(
            f"The most common word in '{popular_song.title}' by {popular_song.artist} is '{most_common}' with {count} occurrences.")
    else:
        print(f"Song '{song}' by {artist} not found on Genius.")


def most_common_word_from_song_graph(artist, song): #ianQQQ
    genius = lyricsgenius.Genius(Genius_API_Key.token, verbose=False, remove_section_headers=True, skip_non_songs=True)
    popular_song = genius.search_song(artist, song)


    if not popular_song:
        print("Song not found, please try again")
        return

    words = popular_song.lyrics.lower().split()

    adjlist = {}    #will be a map of lists

    for i in range(len(words) - 1):
        if words[i] in adjlist:
            adjlist[words[i]].append(words[i + 1])
        else:
            adjlist[words[i]] = []


        if words[i + 1] in adjlist: #append or create list depending on if elelment is there
            adjlist[words[i + 1]].append(words[i])
        else:
            adjlist[words[i + 1]] = []


    most_common_word = ""
    degree = 0

    for word, neighbors in adjlist.items():
        if len(neighbors) > degree:
            most_common_word = word
            degree = len(neighbors)

    print(f"The most common word for '{popular_song.title}' by {popular_song.artist} is '{most_common_word}' with {degree} occurrences.")


def does_song_exist(artist, album):#Carter
    genius = lyricsgenius.Genius(Genius_API_Key.token, verbose=False, remove_section_headers=True, skip_non_songs=True)
    album_search = genius.search_album(artist, album)

    Map={}
    Map[album_search]=album_search if album_search else None
    if album_search:
        print(f"'{album}' by {artist} has been made.")

    else:
        print(f"'{album}' by {artist} has not been made yet!")

def does_song_exist_graph(artist, album):#ian
    genius = lyricsgenius.Genius(Genius_API_Key.token, verbose=False, remove_section_headers=True, skip_non_songs=True)
    album_search = genius.search_album(artist, album)

    AdjList={}

    if album_search:
        AdjList[album_search]=[]
        AdjList[album_search].append(album_search)

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

def common_words_graph(artist, song1, song2):#ian
    genius = lyricsgenius.Genius(Genius_API_Key.token, verbose=False, remove_section_headers=True, skip_non_songs=True)

    lyrics1 = genius.search_song(song1, artist)
    lyrics2 = genius.search_song(song2, artist)


    words1 = lyrics1.lyrics.lower().split()
    words2 = lyrics2.lyrics.lower().split()

    Adjlist = {}

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
def topFiveSongs(inputArtist):#carter

    genius = lyricsgenius.Genius(Genius_API_Key.token, verbose=False, remove_section_headers=True, skip_non_songs=True)
    genius.excluded_terms = ["(Live)"]

    # get Artist object from Genius
    artist = genius.search_artist(inputArtist, max_songs=5)

    print(f"Top 5 songs of {inputArtist}: ")
    Map={}
    for song in artist.songs:
        Map[song.title]=song.title
        print(song.title)

def topFiveSongs_graph(inputArtist):#carter
    genius = lyricsgenius.Genius(Genius_API_Key.token, verbose=False, remove_section_headers=True, skip_non_songs=True)
    genius.excluded_terms = ["(Live)"]

    # get Artist object from Genius
    artist = genius.search_artist(inputArtist, max_songs=5)

    print(f"Top 5 songs of {inputArtist}: ")
    AdjList={}
    for song in artist.songs:
        if song.title not in AdjList:
            AdjList[song.title]=[]
        AdjList[song.title].append(song.title)
        print(song.title)
def all_songs(artist_name):
    # Create genius object with no print statements included
    # No section headers will be included in lyrics, and non songs will be skipped
    # The object will also skip songs that are "Live" performances
    genius = lyricsgenius.Genius(Genius_API_Key.token, verbose=False, remove_section_headers=True, skip_non_songs=True)
    genius.excluded_terms = ["(Live)"]

    # get Artist object from Genius
    artist = genius.search_artist(artist_name, max_songs=None)
    Sum=0

    Map = {}
    for song in artist.songs:
        words = song.lyrics.lower().split()
        word_counts = Counter(words)
        Map[song.title] = sum(word_counts.values())

    print(f'This artist had {len(Map)} songs with {sum(Map.values())} lyrics')

"""







