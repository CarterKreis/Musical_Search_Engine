import lyricsgenius
from lyricsgenius import Genius
from API import Genius_API_Key


# Function to show some of lyricsgenius functionality
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


# Prints out menu
def printMenu():
    print("How would you like to search?")
    print("1. ")
    print("2. ")
    print("3. ")
    print("4. ")
    print("5. ")
    print("6. Quit Searching")


if __name__ == "__main__":
    print("Welcome to the Musical Search Engine")
    print("------------------------------------\n")

    menu = True
    while menu:
        printMenu()
        choice = input()

        if choice == "1":
            pass

        elif choice == "2":
            pass

        elif choice == "3":
            pass

        elif choice == "4":
            pass

        elif choice == "5":
            pass

        elif choice == "6":
            print("See you later!")
            menu = False

        else:
            print("Please type a number 1-6")

    # testGenius()
