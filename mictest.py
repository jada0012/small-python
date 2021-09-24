from pydub import AudioSegment
from pydub.playback import play
from pathlib import Path

folder = Path("D:/python/small-python/takeabreak.mp3")
song = AudioSegment.from_mp3(folder)
play(song)