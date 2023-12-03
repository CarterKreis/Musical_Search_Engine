import lyricsgenius
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


# searches top 20 songs with the keyword "songs" and prints out the title of the songs
def testSongs():
    genius = lyricsgenius.Genius(Genius_API_Key.token)
    genius.verbose = False

    songs = genius.search_songs("girl", per_page=50)

    for song in songs['hits']:
        print("Song:", song['result']['full_title'], "\nArtist:", song['result']['artist_names'], "\n")


# Prints out Main-menu
def printMenu():
    print("What action would you like to perform?")
    print("Please input the number for each option")
    print("1. Sort")
    print("2. Search")
    print("3. Compare")
    print("4. Quit Searching")


# Prints out subMenu
def subMenu(choice):
    print(f"What would you like to {choice}?")
    print("1. Song Title")
    print("2. Album Name")
    print("3. Artist Name")
    print("4. Lyric(s)")
    print("5. Genre")
    print("6. Go Back to Main Menu")


if __name__ == "__main__":
    print("Welcome to the Musical Search Engine")
    print("------------------------------------")

    testSongs()

    menu = True
    while menu:
        printMenu()
        mainChoice = input()

        # Sorting
        if mainChoice == "1":
            subMenu("Sort")
            subChoice = input()



        # Searching
        elif mainChoice == "2":
            subMenu("Search")
            subChoice = input()



        # Comparing
        elif mainChoice == "3":
            subMenu("Compare")
            subChoice = input()



        # Exit option
        elif mainChoice == "4":
            print("See you later!")
            menu = False

        else:
            print("Please type a number 1-4")

    # demoGenius()
