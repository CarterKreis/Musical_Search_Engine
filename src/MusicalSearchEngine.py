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
