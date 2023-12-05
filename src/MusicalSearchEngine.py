import lyricsgenius
import Functions
from lyricsgenius import Genius
from API import Genius_API_Key


# Function to show some of lyricsgenius functionality
def demoGenius():
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


# Prints out Main-menu
def printMenu():
    print(f"What would you like to Search?")
    print("Please input a number 1-6")
    print("1. Most common word from song")
    print("2. Most common word from album")
    print("3. Top 5 songs of an Artist")
    print("4. Most common word from top 20 songs in a genre")
    print("5. ")
    print("6. Exit Program")


"""
Potential Functions 
? = potential concepts
1. Most Common word from song?
2. Most Common word from album?
3. Top 5 songs of Artist 
4. Most common word from top 20 songs in a genre?
5. 
6. Exit Program
"""

if __name__ == "__main__":
    print("Welcome to the Musical Search Engine")
    print("------------------------------------")

    # EngineFunctions.testSongs()
    # demoGenius()

    menu = True
    while menu:
        printMenu()
        mainChoice = input()

        if mainChoice == "1":
            pass

        elif mainChoice == "2":
            pass

        elif mainChoice == "3":
            print("Enter the name of the artist: ")
            name = input()
            Functions.topFiveSongs(name)

        elif mainChoice == "4":
            pass

        elif mainChoice == "5":
            pass

        elif mainChoice == "6":
            print("See you later!")
            menu = False

        else:
            print("Please read the instructions again")
"""
import lyricsgenius
import function
#from lyricsgenius import Genius
import Genius_API_Key


#carter
# Function to show some of lyricsgenius functionality
def demoGenius():
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


# Prints out Main-menu
def printMenu():#carter
    print(f"What would you like to Search?")
    print("Please input a number 1-6")
    print("1. Find artist from song (Map)")
    print("2. Most common word from song (Map)")
    print("3. Top 5 songs of an Artist (Map)")
    print("4. Have album been made(Map)")
    print("5. Shared words between songs (Map)")
    print("6. Find artist from song (Graph)")
    print("7. Most common word from song (Graph)")
    print("8. Top 5 songs of an Artist (Graph)")
    print("9. Find if a song title has been made before (Graph)")
    print("10. Shared words between songs (Graph)")
    print("11. Find all songs from an artist")
    print("12. Exit Program")


if __name__ == "__main__":
    print("Welcome to the Musical Search Engine")
    print("------------------------------------")

    # EngineFunctions.testSongs()
    # demoGenius()

    menu = True
    while menu:
        printMenu()
        mainChoice = input()

        if mainChoice == "1":       #Ian
            print("Enter the name of the song ")

            song = input()
            function.find_the_artist(song)


        elif mainChoice == "2":     #done
            print("Enter the name of the artist then song: ")
            artist = input()
            song = input()
            function.most_common_word_from_song(artist, album)

        elif mainChoice == "3":
            print("Enter the name of the artist: ")
            artist = input()
            function.topFiveSongs(artist)

        elif mainChoice == "4":
            print("Enter the name of the artist then album: ")
            artist = input()
            album = input()
            function.does_song_exist(artist, album)

        elif mainChoice == "5":
            print("Enter the name of the artist then album: ")
            artist = input()
            song1 = input()
            song2 = input()
            function.common_words(artist, song1,song2)

        elif mainChoice == "7":  #
                print("Enter the name of the artist then song: ")
                artist = input()
                album = input()
                function.most_common_word_from_song_graph(artist,album)


        elif mainChoice == "6":  # Ian
                print("Enter the song: ")
                song = input()
                function.find_the_artist_graph(song)

        elif mainChoice == "8": #sam
                print("Enter the name of the artist: ")
                artist = input()
                function.topFiveSongs_graph(artist)

        elif mainChoice == "9": #Ian
                print("Enter the name of the artist then album: ")
                artist = input()
                album = input()
                function.does_song_exist_graph(artist, album)

        elif mainChoice == "10":#sam
                print("Enter the name of the artist then songs: ")
                artist = input()
                song1 = input()
                song2 = input()
                function.common_words_graph(artist, song1, song2)
        elif mainChoice == "11":
            print("Enter an artist name: ")
            artist = input()
            function.all_songs(artist)

        else:
            print("Please read the instructions again")
#ian: we split up the code equally so we all had even work to do
"""
