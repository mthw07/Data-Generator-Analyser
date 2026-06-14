import csv
import random
import os
import sys

NUM_ROWS = 50


COLUMNS = ["ALBUM", "ARTIST", "GENRE", "RELEASE YEAR"]

def generate_row():

    return {
        "ALBUM": random.choice(["Abbey Road", "Led Zeppelin IV", "The Dark Side of the Moon", "Sticky Fingers", "A Night at the Opera", "The Rise and Fall of Ziggy Stardust and the Spiders from Mars", "Nevermind", "In the Court of the Crimson King", "Close to the Edge", "Selling England by the Pound", "L.A. Woman", "Are You Experienced", "Rumours", "Who's Next", "Paranoid", "Back in Black", "Master of Puppets", "Ten", "Superunknown", "Disintegration", "Violator", "Power, Corruption & Lies", "Unknown Pleasures", "The Queen Is Dead", "Automatic for the People", "The Joshua Tree", "London Calling", "Rocket to Russia", "Elephant", "The Colour and the Shape", "Dookie", "Octopus", "Moving Pictures", "Synchronicity", "White Light/White Heat", "Remain in Light"]),
        "ARTIST": random.choice(["The Beatles", "Led Zeppelin", "Pink Floyd", "The Rolling Stones", "Queen", "David Bowie", "Nirvana","King Crimson", "Yes", "Genesis", "The Doors", "Jimi Hendrix", "Fleetwood Mac", "The Who", "Black Sabbath", "AC/DC", "Metallica", "Pearl Jam", "Soundgarden", "The Cure", "Depeche Mode", "New Order", "Joy Division", "The Smiths", "R.E.M.", "U2", "The Clash", "The Ramones", "The White Stripes", "Foo Fighters", "Green Day", "Gentle Giant", "Rush", "The Police", "The Velvet Underground", "Talking Heads"]),
        "GENRE": random.choice(["Classical Rock", "Progressive Rock", "Jazz Rock", "Pop Rock", "Electonic Prog", "New Wave", "Folk Rock", "Hard Rock", "Heavy Metal", "Psychedelic Rock", "Glam Rock", "Art Rock", "Symphonic Prog", "Experimental Rock", "Avant-Garde", "Funk Rock", "Indie Rock", "Alternative Rock", "Post-Rock", "Shoegaze", "Dream Pop", "Ambient", "Industrial Rock", "Noise Rock", "Post-Punk", "Garage Rock", "Soft Rock", "Rock & Roll", "Blues Rock", "Southern Rock", "Country Rock", "Surf Rock", "Rockabilly", "Punk Rock", "Grunge", "Britpop", "Emo", "Pop Punk", "Ska Punk", "Hardcore Punk", "Post-Hardcore", "Math Rock"]),
        "RELEASE YEAR": random.randint(1960, 1999),
    }

OUTPUT_DIR = sys.argv[1] if len(sys.argv) > 1 else "/data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "data.csv")

os.makedirs(OUTPUT_DIR, exist_ok=True)

rows = [generate_row() for _ in range(NUM_ROWS)]

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=COLUMNS)
    writer.writeheader()
    writer.writerows(rows)