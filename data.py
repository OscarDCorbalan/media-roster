import media

# Possible upgrade: use some free database to store all this info,
# and put here the code to retrieve it from the database

def getMedia():
    # Create some movies. See class definition for the parameter order.
    the_martian = media.Movie(
        'The Martian',
        ('During a manned mission to Mars, Astronaut Mark Watney is presumed '
        'dead after a fierce storm and left behind by his crew. But Watney has '
        'survived and finds himself stranded and alone on the hostile planet.'),
        ['Sci Fi'],
        'The_Martian.jpg',
        'https://www.youtube.com/watch?v=ej3ioOneTy8',
        'PG-13',
        144,
        '27 September 2015',
        'Ridley Scott',
        ['Matt Damon', 'Jessica Chastain', 'Kristen Wiig', 'Jeff Daniels',
        'Michael Pena', 'Kate Mara', 'Sean Bean', 'Sebastian Stan',
        'Aksel Hennie', 'Chiwetel Ejiofor'])
    torrente = media.Movie(
        'Torrente',
        ('Torrente is a drunkard, sexist, racist, right-wing Madrid cop who '
        'only cares about himself. He discovers that a band of drug traffickers '
        'are operating in a nearby chinese restaurant, what could make him '
        'regain the status he lost within the police.'),
        ['Comedy'],
        'Torrente.jpg',
        'https://www.youtube.com/watch?v=ZC9XPvePksc',
        'NC-17',
        97,
        '13 March 1998',
        'Santiago Segura',
        ['Santiago Segura', 'Javier Bardem', 'Javier Camara', 'Tony Leblanc',
        'Neus Asensi'])
    interstellar = media.Movie(
        'Interstellar 2014',
        ('A group of explorers must travel beyond our solar system in search of'
        ' a planet that can sustain life.'),
        ['Sci Fi, Adventure'],
        'Interstellar.jpg',
        'https://www.youtube.com/watch?v=zSWdZVtXT7E',
        'PG-13',
        169,
        '26 October 2014',
        'Christopher Nolan',
        ['Matthew McConaughey', 'Anne Hathaway', 'Jessica Chastain',
        'Bill Irwin', 'Ellen Burstyn', 'Michael Caine'])
    star_trek_ix = media.Movie(
        'Star Trek IX',
        ('The young crew onboard for the maiden voyage of the most advanced '
        'starship ever created, the U.S.S. Enterprise, must find a way to stop '
        'the evil Nero, whose mission of vengeance threatens all of mankind.'),
        ['Sci Fi'],
        'Star_Trek_IX.jpg',
        'https://www.youtube.com/watch?v=pKFUZ10Wmbw',
        'PG-13',
        127,
        '6 April 2009',
        'Jonathan Frakes',
        ['Patrick Stewart', 'Jonathan Frakes', 'Brent Spiner', 'LeVar Burton',
        'Michael Dorn', 'Gates McFadden', 'Marina Sirtis', 'F. Murray Abraham',
        'Donna Murphy','Anthony Zerbe'])
    breaveheart = media.Movie(
        'Braveheart',
        ('Edward the Longshanks, King of England (Patrick McGoohan), has '
        'captured Scotlands throne and threatens the freedom of all Scottish '
        'people, as tyrannical policies instituted by the English plague the '
        'Scots.'),
        ['Action, History'],
        'Braveheart.jpg',
        'https://www.youtube.com/watch?v=vBXBtORI7pE',
        'NC-17',
        178,
        '18 May 1995',
        'Mel Gibson',
        ['Mel Gibson', 'Sophie Marceau', 'Patrick McGoohan',
        'Catherine McCormack', 'Angus Macfadyen'])
    troy = media.Movie(
        'Troy',
        ('An adaptation of Homer\'s great epic, the film follows the assault on'
        ' Troy by the united Greek forces and chronicles the fates of the men'
        ' involved.'),
        ['Adventure'],
        'Troy.jpg',
        'https://www.youtube.com/watch?v=aiyQOumuSN4',
        'PG-13',
        163,
        '14 May 2004',
        'Wolfgang Petersen',
        ['Brad Pitt', 'Eric Bana', 'Orlando Bloom', 'Diane Kruger', 'Brian Cox',
        'Sean Bean', 'Brendan Gleeson', 'Peter O\'Toole'])
    kingdom = media.Movie(
        'Kingdom of Heaven',
        ('Balian of Ibelin travels to Jerusalem during the crusades of the 12th'
        ' century, and there he finds himself as the defender of the city and '
        'its people.'),
        ['Action', 'Adventure', 'Drama'],
        'Kingdom_of_Heaven.jpg',
        'https://www.youtube.com/watch?v=-oO6pCRe3pM',
        'PG-13',
        144,
        '6 May 2005',
        'Ridley Scott',
        ['Orlando Bloom', 'Ghassan Massoud', 'Eva Green', 'Jeremy Irons',
        'David Thewlis', 'Brendan Gleeson', 'Marton Csokas', 'Liam Neeson',
        'Edward Norton'])

    # Create some TV Shows. See class definition for the parameter order.
    galactica = media.TvShow(
        'Battlestar Galactica',
        ('In a distant galaxy lie The Twelve Colonies of Man, a civilization '
        'that has been at peace with an empire of machines, the Cylons, who '
        'were created as worker drones for mankind, rose in rebellion, and '
        'launched war on their masters.'),
        ['Fantasy, Action'],
        'Battlestar_Galactica.jpg',
        'https://www.youtube.com/watch?v=TnYsf2Yv8i8',
        'PG-13',
        44,
        4,
        75,
        'Syfy')
    star_trek_voy = media.TvShow(
        'Star Trek: Voyager',
        ('The Federation starship USS Voyager, chasing a band of Maquis rebels'
        ', enters the dangerous space nebula known as the Badlands. Both ships '
        'are transported by a distant space probe 75,000 light-years from '
        'home.'),
        ['Sci Fi'],
        'Star_Trek_Voyager.jpg',
        'https://www.youtube.com/watch?v=b1PX9E2RsgU',
        'PG',
        44,
        7,
        172,
        'UPN')

    # Create some Books. See class definition for the parameter order.
    worldwar1 = media.Book(
        'Worldwar: In the Balance',
        ('First novel of the Worldwar tetralogy. The plot begins in late 1941, '
        'while the Earth is torn apart by World War II. An alien fleet arrive '
        'to conquer the planet, forcing the warring nations to make uneasy '
        'alliances against the invaders.'),
        ['Sci Fi', 'Alternate History'],
        'Worldwar_In_the_balance.jpg',
        'Harry Turtledove',
        'Del Rey Books',
        1994,
        488,
        '0-345-38241-2')
    worldwar2 = media.Book(
        'Worldwar: Tilting the Balance',
        ('As the year 1943 begins, the Race attempts to consolidate its hold '
        'over Latin America, Africa, and Australia while engaged in a fierce '
        'struggle with the advanced nations of the world: the United States, '
        'the United Kingdom, the Soviet Union, Japan, and the Greater German '
        'Reich.'),
        ['Sci Fi', 'Alternate History'],
        'Worldwar_Tilting_the_balance.jpg',
        'Harry Turtledove',
        'Del Rey Books',
        1995,
        478,
        '0-345-38997-2')
    worldwar3 = media.Book(
        'Worldwar: Upsetting the Balance',
        ('The United States and Germany develop atomic weapons of their own and'
        ', alongside the Soviets, engage in a nuclear exchange with the Race. '
        'The Soviets detonte the first atomic bomb, but only because they '
        'captured a sample of plutonium from the Race.'),
        ['Sci Fi', 'Alternate History'],
        'Worldwar_Upsetting_the_balance.jpg',
        'Harry Turtledove',
        'Del Rey Books',
        1996,
        481,
        '0-345-40221-9')
    worldwar4 = media.Book(
        'Worldwar: Striking the Balance',
        ('At the beginning of 1944, the Battle of Chicago has ended with the '
        'Race\'s forces decimated as a result of an American atomic bomb. '
        'German forces in Western Europe have successfully kept the Race from '
        'reaching the Rhine while managing to hurl back the Race\'s troops in '
        'Poland after a nuclear attack on Breslau.'),
        ['Sci Fi', 'Alternate History'],
        'Worldwar_Striking_the_balance.jpg',
        'Harry Turtledove',
        'Del Rey Books',
        1996,
        465,
        '0-345-40550-1')
    colonization1 = media.Book(
        'Colonization: Second Contact',
        ('The novel is set in 1963, twenty one years following the end of the '
        'alternate World War II and nineteen years after the Race Invasion of '
        'Tosev 3. Earl Warren is President of the United States, Vyacheslav '
        'Molotov is the Premier of the Soviet Union, and Heinrich Himmler '
        'leads Nazi Germany.'),
        ['Sci Fi', 'Alternate History'],
        'Colonization_Second_Contact.jpg',
        'Harry Turtledove',
        'Del Rey Books',
        1999,
        466,
        '0-345-43019-0')
    colonization2 = media.Book(
        'Colonization: Down to Earth',
        ('Following the nuclear attack on the colonist ships in Second Contact,'
        ' the Race continues to try to find the responsible nation, along with '
        'the purpose of the Lewis and Clark, a large space station launched by '
        'the United States.'),
        ['Sci Fi', 'Alternate History'],
        'Colonization_Down_to_Earth.jpg',
        'Harry Turtledove',
        'Del Rey Books',
        2000,
        496,
        '0-345-43020-4')
    colonization3 = media.Book(
        'Colonization: Aftershocks',
        ('The nuclear war between Nazi Germany and the Race ends with a German '
        'surrender after the Fuhrer is killed and replaced by Walter Dornberger'
        ', who agrees to disband the Axis Forces, withdraw German troops from '
        'occupied France and Vichy France, and disband the German rocket and '
        'nuclear forces.'),
        ['Sci Fi', 'Alternate History'],
        'Colonization_Aftershocks.jpg',
        'Harry Turtledove',
        'Del Rey Books',
        2001,
        496,
        '0-345-43021-2')
    homeward = media.Book(
        'Homeward Bound',
        ('The Admiral Peary travels at between 0.35 and 0.4 c and took a little'
        ' over 30 years to cross the twelve light years between Earth and Tau '
        'Ceti. The ship is named Admiral Peary for its role as a military '
        'exploration ship, after Adm. Robert Peary, who did the same in Arctic '
        'exploration.'),
        ['Sci Fi', 'Alternate History'],
        'Homeward_Bound.jpg',
        'Harry Turtledove',
        'Del Rey Books',
        2004,
        608,
        '0-345-45846-X')

    # Return a list with the elements in the order we want them to be shown
    return [the_martian, galactica, torrente, star_trek_voy, interstellar,
            star_trek_ix, breaveheart, homeward, worldwar1, worldwar2,
            worldwar3, worldwar4, colonization1, colonization2, colonization3,
            troy, kingdom]
