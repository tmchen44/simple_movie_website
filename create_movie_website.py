from media import Movie
import fresh_tomatoes

# This script instantiates Movie objects and uses them to create a website
# by calling fresh_tomatoes.open_movies_page

# Instantiate Movie objects here
star_wars = Movie("SW: The Force Awakens",
                  "poster_images/star_wars.jpg",
                  "https://www.youtube.com/watch?v=sGbxmsDFVnE")

lord_of_the_rings = Movie("LotR: Return of the King",
                          "poster_images/return_of_the_king.jpg",
                          "https://www.youtube.com/watch?v=amGFXKHlE78")

wall_e = Movie("Wall-E",
               "poster_images/wall_e.jpg",
               "https://www.youtube.com/watch?v=8-_9n5DtKOc")

up = Movie("Up",
           "poster_images/up.jpg",
           "https://www.youtube.com/watch?v=pkqzFUhGPJg")

hacksaw_ridge = Movie("Hacksaw Ridge",
                      "poster_images/hacksaw_ridge.jpg",
                      "https://www.youtube.com/watch?v=s2-1hz1juBI")

inception = Movie("Inception",
                  "poster_images/inception.jpg",
                  "https://www.youtube.com/watch?v=8hP9D6kZseM")

# Store Movie objects in a list
movie_list = [star_wars,
              lord_of_the_rings,
              wall_e,
              up,
              hacksaw_ridge,
              inception]

# Create movie website using fresh_tomatoes.open_movies_page
fresh_tomatoes.open_movies_page(movie_list)
