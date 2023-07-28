ONE

1. Describe the Problem
   As a user
   So that I can keep track of my music listening
   I want to add tracks I've listened to and see a list of them.

2. Design the Class Interface

class MusicTracker:

    def __init__(self):
        # Parameters:
        #   No parameters
        # Side effects:
        #   Initialises a list to store music tracks
        pass # No code here yet

    def add(self, track):
        # Parameters:
        #   track: string representing a single music track
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the track to the self object
        pass # No code here yet

    def list_tracks(self):
        # Returns:
        #   A list consisting of music tracks
        # Side-effects:
        #   Throws an exception if no tracks have been added
        pass # No code here yet

3. Create Examples as Tests

""" When a MusicTracker object is created, an empty list is
intialised.
"""
music_tracker = MusicTracker()

""" When a music track is added it is added to the self object"""
music_tracker = MusicTracker()
music_tracker.add("Track1") => returns Nothing

""" When list_tracks is called, a list of music tracks should be returned if music tracks have been added""".
music_tracker = MusicTracker()
music_tracker.add("Track1")
music_tracker.list_tracks() => A list of music tracks

""" When list_tracks is called, an error is raised if no music tracks have been added."""
music_tracker = MusicTracker()
music_tracker.list_tracks() => Raises an error "No tracks have been added".
