from lib.diary_entry import *

def test_create_object():
    diary_entry = DiaryEntry("title", "contents")
    assert diary_entry.title == "title"
    assert diary_entry.contents == "contents"

def test_format():
    diary_entry = DiaryEntry("title", "contents")
    assert diary_entry.format() == "title: contents"

def test_count_words():
    diary_entry = DiaryEntry("title", "contents")
    num_words = diary_entry.count_words()
    assert num_words == 1
    
