import pytest
from lib.music_library import *

def test_init_of_class_contains_empty_list():
    library = MusicLibrary()
    assert library.music_dict == {}

def test_add_function_with_artist_track_pairs():
    library = MusicLibrary()
    library.add_track('Pink Floyd', 'Money')
    assert library.music_dict == {'Pink Floyd': ['Money']}
    library.add_track('Elbow', 'Starlings')
    assert library.music_dict == {'Pink Floyd': ['Money'], 'Elbow': ['Starlings']}
    library.add_track('Pink Floyd', 'Breathe')
    assert library.music_dict == {'Pink Floyd': ['Money', 'Breathe'], 'Elbow': ['Starlings']}

def test_remove_artist_function_removes_from_music_dict():
    library = MusicLibrary()
    library.add_track('Pink Floyd', 'Money')
    library.add_track('Elbow', 'Starlings')
    library.remove_artist('Pink Floyd')
    assert library.music_dict == {'Elbow': ['Starlings']}

def test_add_function_throws_error_when_wrong_type_used():
    library = MusicLibrary()
    with pytest.raises(Exception) as err:
        library.add_track(100, True)
    error_message = str(err.value)
    assert error_message == 'Error: Ensure that both inputs are of type string'

def test_remove_track_function_removes_track_from_music_dict():
    library = MusicLibrary()
    library.add_track('Pink Floyd', 'Money')
    library.add_track('Pink Floyd', 'Breathe')
    library.remove_track('Pink Floyd', 'Money')
    assert library.music_dict == {'Pink Floyd': ['Breathe']}

def test_view_tracks_throws_error_when_wrong_type_used():
    library = MusicLibrary()
    library.add_track('Pink Floyd', 'Money')
    with pytest.raises(Exception) as err:
        library.view_tracks_by_artist(True)
    error_message = str(err.value)
    assert error_message == 'Error: Ensure that input is of type string'

def test_remove_track_function_throws_error_when_wrong_type_used():
    library = MusicLibrary()
    library.add_track('Pink Floyd', 'Money')
    with pytest.raises(Exception) as err:
        library.remove_track(100, True)
    error_message = str(err.value)
    assert error_message == 'Error: Ensure that both inputs are of type string'

def test_remove_artist_throws_error_when_wrong_type_used():
    library = MusicLibrary()
    library.add_track('Pink Floyd', 'Money')
    with pytest.raises(Exception) as err:
        library.remove_artist(100)
    error_message = str(err.value)
    assert error_message == 'Error: Ensure that both inputs are of type string'