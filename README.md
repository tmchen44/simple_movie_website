## Movie Trailer Website

This simple movie trailer webpage lists several movies along with their poster art. If you click on any one of the posters, a pop-up will play the corresponding Youtube trailer.

### Quick Start
To see the example page, open `fresh_tomatoes.html` with any web browser.

To generate your own list of movies with corresponding box art and movie trailer:
- Install Python 3
- Within `create_movie_website.py`, or within an interactive Python session:
    - Instantiate Movie objects with the appropriate title and links to poster art and trailer. For more information on the Movie class, see `media.py`.
    - Place all Movie objects into a list. Pass this list into the `fresh_tomatoes.open_movies_page` function.
    - If you run the above code with the Python interpreter, an html file named `fresh_tomatoes.html` will be generated and will also automatically open in your default web browser.

### Code Attributions
`fresh_tomatoes.py`, which creates the front-end of the website was provided by Udacity.
