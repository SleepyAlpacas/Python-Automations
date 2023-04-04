import pydub
from pydub import AudioSegment
import os
import eyed3

directory_name = "Desktop/1UX7XMf"

#concatenate all mp3 files in a directory to a file
songs = os.listdir(directory_name)
songs.sort()
result = AudioSegment.empty()
for x in songs:
    print(directory_name + "/" + x)
    result += AudioSegment.from_mp3(directory_name + "/" + x)

print("Export in progress")
result.export(directory_name + "/result.mp3", format="mp3")


#setting tags for the result
sample_song = eyed3.load(directory_name + "/" + songs[0])
result = eyed3.load(directory_name + "/result.mp3")
result.initTag()
result.tag.artist = sample_song.tag.artist
result.tag.album = sample_song.tag.album
result.tag.genre = sample_song.tag.genre

#setting album art
#os.system("eyeD3 --write-images=./ " + directory_name + "/\"" + songs[0] + "\"")
os.system("ffmpeg -i " + directory_name + "/\"" + songs[0] + "\" -an -c:v copy " + directory_name + "/OTHER.jpg")
album_art = open(directory_name + "/OTHER.jpg", "rb")
album_art_data = album_art.read()

result.tag.images.set(3, album_art_data, "image/jpg")

result.tag.save()
os.system("rm " + directory_name + "/OTHER.jpg")


print("Export complete!")