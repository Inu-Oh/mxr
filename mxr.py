from datetime import datetime
from sys import exit
from time import sleep
import vlc


def play_song(source, volume):
    instance = vlc.Instance('--input-repeat=999') # increase repeats if needed
    player = instance.media_player_new()
    player.audio_set_volume(volume)
    media = instance.media_new(source)
    player.set_media(media)
    player.play()
    sleep(2)
    raw_duration = int(media.get_duration())
    seconds = int((raw_duration / 1000) % 60)
    minutes = int(raw_duration / (60 * 1000) % 60)
    hours = int(raw_duration / (60 * 60 * 1000))
    print(f"  Playing: {source.split('/')[7].split('.')[0]:>25}  -  Volume:", end=" ")
    print(f"{player.audio_get_volume()}  -  Duration:{hours:4d}:{minutes:02}:{seconds:02}\n")


# Audio data  TODO: add your file paths and change volume as needed 
tracks = [ 
    {"source": "file:///path/to/your/music/file/Eg Beach Waves.mp3", "volume": 53},
    {"source": "file:///path/to/your/music/file/Eg Rainforest Rain Soundx.mp3", "volume": 65},
    {"source": "file:///path/to/your/music/file/Eg Gentle Stream Sounds.mp3", "volume": 50},
]

# Display current time
print("\n  Start time:", datetime.now(), "\n")


# Play three songs to repeat 999 times each
# Add songs or increase repeats if needed
play_song(tracks[0]["source"], tracks[0]["volume"])
play_song(tracks[1]["source"], tracks[1]["volume"])
play_song(tracks[2]["source"], tracks[2]["volume"])

# Display play time and close program with CTRL + C
count = 0
print("  Press 'Ctrl + C' to exit\n")
try:
    while True:
        if count <= 60: 
            print(f"  Playing about {count:02} minutes", end="\r")
        else:
            hours = int(count / 60)
            minutes = int(count % 60)
            print(f"  Playing about {hours} hours and {minutes:02} minutes", end="\r")
        sleep(60)
        count += 1
except KeyboardInterrupt:
    print("\n\n  Goodbye !")
    exit(0)
