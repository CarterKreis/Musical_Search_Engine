import lyricsgenius
import Functions
from lyricsgenius import Genius
from API import Genius_API_Key


# Prints out Main-menu
def printMenu():  # Carter
    print(f"What would you like to Search?")
    print("Please input a number 1-6")
    print("1. Find artist from song (Map)")
    print("2. Most common word from song (Map)")
    print("3. Top 5 songs of an Artist (Map)")
    print("4. Find if an album has been made before (Map)")
    print("5. Shared words between songs (Map)")
    print("6. Find artist from song (Graph)")
    print("7. Most common word from song (Graph)")
    print("8. Top 5 songs of an Artist (Graph)")
    print("9. Find if an album has been made before (Graph)")
    print("10. Shared words between songs (Graph)")
    print("11. Find all songs from an artist (Map)")
    print("12. Exit Program")


if __name__ == "__main__":
    print("Welcome to the Musical Search Engine")
    print("------------------------------------")

    menu = True
    while menu:
        printMenu()
        mainChoice = input()

        # Ian
        if mainChoice == "1":
            print("Enter the name of the song ")
            song = input()
            Functions.find_the_artist(song)

        # Carter
        elif mainChoice == "2":
            print("Enter the name of the artist then song: ")
            artist = input()
            song = input()
            Functions.most_common_word_from_song(artist, song)

        # Carter
        elif mainChoice == "3":
            print("Enter the name of the artist: ")
            artist = input()
            Functions.topFiveSongs(artist)

        # Sam
        elif mainChoice == "4":
            print("Enter the name of the artist then album: ")
            artist = input()
            album = input()
            Functions.does_album_exist(artist, album)

        # Carter
        elif mainChoice == "5":
            print("Enter the name of the artist then album: ")
            artist = input()
            song1 = input()
            song2 = input()
            Functions.common_words(artist, song1, song2)

        # Carter
        elif mainChoice == "7":
            print("Enter the name of the artist then song: ")
            artist = input()
            album = input()
            Functions.most_common_word_from_song_graph(artist, album)

        # Ian
        elif mainChoice == "6":
            print("Enter the song: ")
            song = input()
            Functions.find_the_artist_graph(song)

        # Sam
        elif mainChoice == "8":
            print("Enter the name of the artist: ")
            artist = input()
            Functions.topFiveSongs_graph(artist)

        # Ian
        elif mainChoice == "9":
            print("Enter the name of the artist then album: ")
            artist = input()
            album = input()
            Functions.does_album_exist_graph(artist, album)

        # Sam
        elif mainChoice == "10":
            print("Enter the name of the artist then songs: ")
            artist = input()
            song1 = input()
            song2 = input()
            Functions.common_words_graph(artist, song1, song2)

        # Sam
        elif mainChoice == "11":
            print("Enter an artist name: ")
            artist = input()
            Functions.all_songs(artist)

        else:
            print("Please read the instructions again")

# Ian: we split up the code equally, so we all had even work to do
