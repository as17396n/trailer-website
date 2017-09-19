import webbrowser


class Movie():
    """A model of a Movie"""
    def __init__(self, title, storyline, poster_image, trailer_youtube):
                """Initialize movie features"""
                self.title = title
                self.storyline = storyline
                self.poster_image_url = poster_image
                self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Shows Trailer"""
        webbrowser.open(self.trailer_youtube_url)
