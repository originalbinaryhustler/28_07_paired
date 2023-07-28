from lib.diary_entry_2 import *

def test_initialise_diary_entry():
    diary_entry = DiaryEntry('28th July', 'Today was good')
    assert diary_entry.title == '28th July'
    assert diary_entry.contents == 'Today was good'

# def test_