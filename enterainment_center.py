import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and its toys",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyH8NQC4")


avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://en.wikipedia.org/wiki/File:Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")


GoT = media.Movie("Game of Thrones",
                     "7 powerful Houses are fighting for the Iron Throne of 7 Kingdoms",
                     "http://4.bp.blogspot.com/-FuP3ehGClQs/TfBm4yiOSVI/AAAAAAAAA38/6Wgx0eijnKI/s1600/600full-game-of-thrones-poster.jpg",
                     "http://www.youtube.com/watch?v=BpJYNVhGf1s")


big_lebowski = media.Movie("The Big Lebowski",
                           "Times Like These Call For A Big Lebowski",
                           "http://upload.wikimedia.org/wikipedia/en/3/35/Biglebowskiposter.jpg",
                           "https://www.youtube.com/watch?v=cd-go0oBF4Y")

movies = [toy_story, avatar, GoT, big_lebowski]
fresh_tomatoes.open_movies_page(movies)


