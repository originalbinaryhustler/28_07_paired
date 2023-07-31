class MusicTracker:

      def __init__(self):
        self.music_dict = {}

      def add_track(self, artist: str, track: str):
        self.music_dict.setdefault(artist, []).extend([track])
      def view_artist(self):
        artist = list(self.music_dict.keys())
        return '\n'.join(artist)

      def view_tracks_by_artist(self, artist):
         artists = {key:pair for (key,pair) in self.music_dict.items() if key == artist }
         for k,v in self.music_dict.items():
            if k == artist:
                tracks = v
         
         return'\n'.join(tracks)

      def view_library(self):
         library = self.music_dict.items()
         return list(library)
         
      def remove_track(self,artist,track):
         for item in self.music_dict.values():
            pass