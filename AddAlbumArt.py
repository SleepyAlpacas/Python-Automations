import eyed3


#CHANGE THESE VARIABLES TO THE APPROPRIATE PATHS
mp3path = 'Desktop/test.mp3'
cover_art_path = 'Desktop/index.jpg'
cover_art_type = "image/jpg"

mp3file = eyed3.load(mp3path)
cover_art = open(cover_art_path, "rb")
mp3file.tag.images.set(3, cover_art.read(), cover_art_type)
mp3file.tag.save()

