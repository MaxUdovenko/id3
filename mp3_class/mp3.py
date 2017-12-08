import os

class MP3_format():
    def __init__(self, name, path):
        self.name = name + '.mp3'
        self.path = path

    # IDv


mp3_track = MP3_format('my love', 'Romantic collection')
print(mp3_track.name)
print(os.path)
