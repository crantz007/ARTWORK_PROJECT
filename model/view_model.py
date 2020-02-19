class viewModel:
    # Arguments to communicate with the database
    def __init__(self, db):
        self.db = db

    def insert_artist(self, artist):
        self.db.insert_artist(artist)

    def insert_artwork(self, artwork):
        self.db.insert_artwork(artwork)

    def search_all_artwork(self, artist):
        artworks = self.db.search_all_artwork(artist)
        return artworks

    def search_available_artwork(self, artist):
        artworks = self.db.search_available_artwork(artist)
        return artworks

    def delete_artwork(self, artwork):
        delArtwork = self.db.delete_artwork(artwork)
        return delArtwork

    def change_status(self, artwork, available):
        statusChange = self.db.change_status(artwork, available)
        return statusChange
