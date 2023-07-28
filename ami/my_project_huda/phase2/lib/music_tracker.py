class MusicTracker:
    def __init__(self):
        self.tracks = []

    def add(self, track):
        self.tracks.append(track)

    def list_tracks(self):
        if self.tracks:
            return self.tracks
        else:
            raise Exception("Error: no tracks added.")



    