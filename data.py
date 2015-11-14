import media

#TODO use a free MongoDB instance :)

def getMedia():
    # Create some movies
    the_martian = media.Movie(
        "The Martian",
        "During a manned mission to Mars, Astronaut Mark Watney is presumed dead after a fierce storm and left behind by his crew. But Watney has survived and finds himself stranded and alone on the hostile planet.",
        "Sci Fi",
        "img/The_Martian.jpg",
        "https://www.youtube.com/watch?v=ej3ioOneTy8",
        "PG-13",
        144,
        "27 September 2015",
        "Ridley Scott")
    galactica = media.TvShow(
        "Battlestar Galactica",
        "In a distant galaxy lie The Twelve Colonies of Man, a civilization that has been at peace with an empire of machines, the Cylons, who were created as worker drones for mankind, rose in rebellion, and launched war on their masters.",
        "Fantasy, Action",
        "img/Battlestar_Galactica.jpg",
        "https://www.youtube.com/watch?v=TnYsf2Yv8i8",
        "PG-13",
        44,
        4,
        75,
        "Syfy")
    star_trek_voy = media.TvShow(
        "Star Trek: Voyager",
        "The Federation starship USS Voyager, chasing a band of Maquis rebels, enters the dangerous space nebula known as the Badlands. Both ships are transported by a distant space probe 75,000 light-years from home.",
        "Sci Fi",
        "img/Star_Trek_Voyager.jpg",
        "https://www.youtube.com/watch?v=b1PX9E2RsgU",
        "PG",
        44,
        7,
        172,
        "UPN")
    torrente = media.Movie(
        "Torrente",
        "Torrente is a drunkard, sexist, racist, right-wing Madrid cop who only cares about himself. He discovers that a band of drug traffickers are operating in a nearby chinese restaurant, what could make him regain the status he lost within the police.",
        "Comedy",
        "img/Torrente.jpg",
        "https://www.youtube.com/watch?v=ZC9XPvePksc",
        "NC-17",
        97,
        "13 March 1998",
        "Santiago Segura")
    interstellar = media.Movie(
        "Interstellar 2014",
        "A group of explorers must travel beyond our solar system in search of a planet that can sustain life.",
        "Sci Fi, Adventure",
        "img/Interstellar.jpg",
        "https://www.youtube.com/watch?v=zSWdZVtXT7E",
        "PG-13",
        169,
        "26 October 2014",
        "Christopher Nolan")
    star_trek_ix = media.Movie(
        "Star Trek IX",
        "The young crew onboard for the maiden voyage of the most advanced starship ever created, the U.S.S. Enterprise, must find a way to stop the evil Nero, whose mission of vengeance threatens all of mankind.",
        "Sci Fi",
        "img/Star_Trek_IX.jpg",
        "https://www.youtube.com/watch?v=pKFUZ10Wmbw",
        "PG-13",
        127,
        "6 April 2009",
        "Jonathan Frakes")
    breaveheart = media.Movie(
        "Braveheart",
        "Edward the Longshanks, King of England (Patrick McGoohan), has captured Scotlands throne and threatens the freedom of all Scottish people, as tyrannical policies instituted by the English plague the Scots.",
        "Action, History",
        "img/Braveheart.jpg",
        "https://www.youtube.com/watch?v=vBXBtORI7pE",
        "NC-17",
        178,
        "18 May 1995",
        "Mel Gibson")

    return [the_martian, galactica, torrente, star_trek_voy, interstellar, star_trek_ix, breaveheart]
