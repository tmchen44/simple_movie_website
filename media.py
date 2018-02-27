class Movie():
    """The Movie class holds information about a particular movie.

    Attributes:
        title (string): the title of the movie
        poster_image_url (string): a link to the movie poster
        trailer_youtube_url (string): a link to the movie Youtube trailer

    """

    def __init__(self, title, poster_image, youtube_trailer):
        """__init__ method for class Movie

        Args:
            title (string): title of the movie
            poster_image (string): link to the movie's poster image
            trailer_youtube_url (string): link to the movie's Youtube trailer

        """
        self.title = title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer
