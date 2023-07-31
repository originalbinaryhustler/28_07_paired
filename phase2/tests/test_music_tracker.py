from lib.music_tracker import *
import pytest

def test_music_add_track_and_view_artists():
    music = MusicTracker()
    music.add_track('Tupac','Uppercut')
    view = music.view_artist()
    assert view == 'Tupac'
    music.add_track('The Jacka','Die Young')
    music.add_track('Tupac','Hail Mairy')
    viewer = music.view_artist()
    assert viewer == 'Tupac\nThe Jacka'

def test_view_tracks_by_artist():
    music = MusicTracker()
    music.add_track('Tupac','Uppercut')
    music.add_track('The Jacka','Die Young')
    music.add_track('The Jacka','Hamm Sammich')
    music.add_track('Tupac','Hail Mairy')
    music.add_track('Tupac','Starin Through My Rearview')
    result = music.view_tracks_by_artist('Tupac')
    assert result == 'Uppercut\nHail Mairy\nStarin Through My Rearview'
    result1 = music.view_tracks_by_artist('The Jacka')
    assert result1 == 'Die Young\nHamm Sammich'


def test_view_library():
    music = MusicTracker()
    music.add_track('Tupac','Uppercut')
    music.add_track('The Jacka','Die Young')
    music.add_track('The Jacka','Hamm Sammich')
    music.add_track('Tupac','Hail Mairy')
    music.add_track('Tupac','Starin Through My Rearview')
    result = music.view_library()
    assert result == 'Tupac:\nUppercut\nHail mairy\nStaring Through My Rearview\n\n The Jacka:\nDie Young\nHamm Sammich'