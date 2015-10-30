import media

def getMedia():
    # Create some movies
    toy_story = media.Movie(
        "Toy Martian",
        "During a manned mission to Mars, Astronaut Mark Watney is presumed dead after a fierce storm and left behind by his crew. But Watney has survived and finds himself stranded and alone on the hostile planet.",
        "http://pics.filmaffinity.com/The_Martian-972637166-large.jpg",
        "https://www.youtube.com/watch?v=ej3ioOneTy8")
    avatar = media.Movie(
        "Battlestar Galactica",
        "In a distant galaxy lie The Twelve Colonies of Man, a civilization that has been at peace with an empire of machines, the Cylons, who were created as worker drones for mankind, rose in rebellion, and launched war on their masters.",
        "http://pics.filmaffinity.com/Battlestar_Galactica_TV-925903043-large.jpg",
        "https://www.youtube.com/watch?v=TnYsf2Yv8i8")
    torrente = media.Movie(
        "Torrente",
        "A corrupt wanna-be cop becomes rich.",
        "http://i.jeded.com/i/torrente-the-stupid-arm-of-the-law-torrente-el-brazo-tonto-de-la-ley.15154.jpg",
        "https://www.youtube.com/watch?v=ZC9XPvePksc")
    interstellar = media.Movie(
        "Interstellar 2014",
        "A group of explorers must travel beyond our solar system in search of a planet that can sustain life.",
        "http://pics.filmaffinity.com/Interstellar-366875261-large.jpg",
        "https://www.youtube.com/watch?v=zSWdZVtXT7E")
    star_trek = media.Movie(
        "Star Trek XI",
        "The young crew onboard for the maiden voyage of the most advanced starship ever created, the U.S.S. Enterprise, must find a way to stop the evil Nero, whose mission of vengeance threatens all of mankind.",
        "http://pics.filmaffinity.com/Star_Trek-815589716-large.jpg",
        "https://www.youtube.com/watch?v=pKFUZ10Wmbw")

    breaveheart = media.Movie(
        "Braveheart",
        "Edward the Longshanks, King of England (Patrick McGoohan), has captured Scotlands throne and threatens the freedom of all Scottish people, as tyrannical policies instituted by the English plague the Scots.",
        "http://pics.filmaffinity.com/Braveheart-898928745-large.jpg",
        "https://www.youtube.com/watch?v=vBXBtORI7pE")

    return [toy_story, avatar, torrente, interstellar, star_trek, breaveheart]
