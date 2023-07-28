from lib.music_tracker import *
import pytest

""" When a MusicTracker object is created, an empty list is
intialised.
"""
def test_music_tracker_object_is_created():
    music_tracker = MusicTracker()
    assert music_tracker.tracks == []

""" When a music track is added it is added to the self object"""
def test_add_track():
    music_tracker = MusicTracker()
    music_tracker.add("Track1")
    assert music_tracker.tracks == ["Track1"]

""" When list_tracks is called, a list of music tracks should be returned if music tracks have been added"""
def test_list_tracks():
    music_tracker = MusicTracker()
    music_tracker.add("Track1")
    result = music_tracker.list_tracks()
    assert result == ["Track1"]

""" When list_tracks is called, an error is raised if no music tracks have been added."""
def test_list_tracks_when_no_tracks_listed():
    music_tracker = MusicTracker()
    with pytest.raises(Exception) as e:
        music_tracker.list_tracks()
    error_message = str(e.value)
    assert error_message == "Error: no tracks added."