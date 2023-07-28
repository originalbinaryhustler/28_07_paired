from lib.diary_2 import *
from lib.diary_entry_2 import *

def test_add_diary_entry():
    diary = Diary()
    diary_entry = DiaryEntry('28th July', 'Today is good')
    diary.add(diary_entry)
    assert diary.entry_list == ['28th July: Today is good']