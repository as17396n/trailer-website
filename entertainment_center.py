import media
import fresh

toy_story = media.Movie("Toy story",
                        "A story of a boy",
                        "http://www.impawards.com/1995/posters/toy_story_ver1_xlg.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

rocky = media.Movie("Rocky",
                    "A story of a fighter",
                    "https://www.movieposter.com/posters/archive/main/90/MPW-45270",  # NOQA
                    "https://www.youtube.com/watch?v=Wif1EzGQ9Fk")

shaolin_Soccer = media.Movie("Shaolin Soccer",
                    "A story of shaolin brothers",
                    "http://www.impawards.com/2003/posters/shaolin_soccer.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=QfuTz2pT7tQ")

pk = media.Movie("PK",
                    "A story of a alien",
                    "http://www.impawards.com/intl/india/2014/posters/pk_xlg.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=SOXWc32k4zA")

idiots = media.Movie("PK",
                    "A story of three students",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BZWRlNDdkNzItMzhlZC00YTdmLWIwNjktYjY5NjQ1ZmQ3N2FkXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,747,1000_AL_.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=xvszmNXdM4w")


movies = [toy_story, avatar, rocky, Shaolin_Soccer, pk, idiots]
fresh.open_movies_page(movies)
