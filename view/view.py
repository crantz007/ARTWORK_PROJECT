from model.Model import Artist
from model.Model import Artwork
from exceptions.artworkError import ArtworkError
from view.view_utils import input_positive_float
from view.view_utils import input_yes_or_no


# setting view
class View:
    def __init__(self, view_model):
        self.view_model = view_model

    # Menu for user choice
    def display_menu(self):
        while True:
            choice = int(input("*****MENU***** \n1: Add Artist \n2: "
                               "Search all artwork by artist \n3: Search available artwork by artist \n"
                               "4: Add an artwork \n5: Delete an artwork  \n6: Change status of artwork \n7: Exit \n"))
            if choice == 1:
                self.add_artist()
            elif choice == 2:
                self.search_all_artwork()
            elif choice == 3:
                self.search_available_artwork()
            elif choice == 4:
                self.add_artwork()
            elif choice == 5:
                self.delete_artwork()
            elif choice == 6:
                self.change_status()
            elif choice == 7:
                break
            else:
                print("choice must be between 1 and 7")

    # add an artist
    def add_artist(self):
        while True:
            name = input("Enter the artist name to insert into database \n")
            if not name:
                break
            email = input(f"Enter the artist email for {name}: \n")
            artist = Artist(name, email)
            try:
                self.view_model.insert_artist(artist)
                print(f"artist {artist.name} successfully added!")
                break
            except ArtworkError as e:
                print(str(e))

    # add artwork
    def add_artwork(self):
        while True:
            artist = input("Enter the artist of the artwork\n")
            if not artist:
                break
            name = input("Enter the name of the artwork\n")
            price = input_positive_float(f'Enter the artwork price for {name}')
            available = input_yes_or_no(f"Is {name} available? yes or no\n")
            artwork = Artwork(artist, name, price, available)
            try:
                self.view_model.insert_artwork(artwork)
                print(f"artwork {artwork.name} added!")
                break
            except ArtworkError as e:
                print(str(e))

    # search artwork by artist name
    def search_all_artwork(self):
        while True:
            artist = input('Enter the artist name to find the artworks\n')
            if not artist:
                break
            try:
                all_artwork = self.view_model.search_all_artwork(artist)
                if not all_artwork:
                    print(f" {artist} is not found ")
                for row in all_artwork:
                    if row.available == 1:
                        available = "Yes"
                    elif row.available == 0:
                        available = "No"
                    print(f'Name: {row.name} Artist: {row.artist} Price: {row.price} Available: {available}')
                break
            except ArtworkError as e:
                print(str(e))

    # search the available artwork by artist name
    def search_available_artwork(self):
        while True:
            artist = input('Enter the artist to search to get the artwork\n')
            if not artist:
                break
            try:
                available_artwork = self.view_model.search_available_artwork(artist)
                for row in available_artwork:
                    print(f'Name: {row.name} Artist: {row.artist} Price: {row.price} Available: Yes')
                break
            except ArtworkError as e:
                print(str(e))

    # delete artwork by artwork name
    def delete_artwork(self):
        while True:
            artwork = input('Enter the artwork name to be deleted\n')
            if not artwork:
                break
            try:
                delArt = self.view_model.delete_artwork(artwork)
                if delArt is False:
                    print(f"{artwork} is not found!")
                else:
                    print(f"{artwork} is deleted")
                break
            except ArtworkError as e:
                print(str(e))

    # change the artwork status
    def change_status(self):
        while True:
            artwork = input('Enter the artworks name to change his status\n')
            available = input_yes_or_no(f"is {artwork} available? yes or no\n")
            if not artwork:
                break
            try:
                changed_artwork_status = self.view_model.change_status(artwork, available)
                if changed_artwork_status is False:
                    print(f"{artwork} is not found")
                else:
                    print(f'{artwork} is updated')
                break
            except ArtworkError as e:
                print(str(e))
