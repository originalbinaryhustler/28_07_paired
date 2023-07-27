import pytest
from lib.test_drive_a_class import *

def test_initialise_title_assigned():
    example = DiaryEntry('Diary', 'My name is Ben')
    assert example.title == 'Diary'

def test_initialise_contents_assigned():
    example = DiaryEntry('Diary', 'My name is Ben')
    assert example.contents == 'My name is Ben'

def test_format_functions_correctly():
    example = DiaryEntry('Diary', 'My name is Ben')
    assert example.format() == 'My Diary: My name is Ben'

def test_count_words_functions_correctly():
    example = DiaryEntry('Diary', 'My name is Ben')
    assert example.count_words() == 6

def test_reading_time_functions_correctly():
    example = DiaryEntry('Diary', 'My name is Ben')
    assert example.reading_time(3) == 2

def test_reading_chunk_intial_assert():
    example = DiaryEntry('Diary', 'My name is Ben')
    assert example.reading_chunk(3, 1) == 'My Diary: My'

def test_reading_chunk_second_assert():
    example = DiaryEntry('Diary', 'My name is Ben')
    example.reading_chunk(3, 1)
    assert example.reading_chunk(3, 1) == 'name is Ben'