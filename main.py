from view.view import View
from model.view_model import viewModel
from database.Artwork_db import SQLArtworkDB


# main method for database , view_model , View and menu
def main():
    artwork_db = SQLArtworkDB()
    artwork_view_model = viewModel(artwork_db)
    artwork_view = View(artwork_view_model)
    artwork_view.display_menu()


if __name__ == '__main__':
    main()
