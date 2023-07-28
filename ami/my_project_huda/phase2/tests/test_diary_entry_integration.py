from lib.diary_2 import *
from lib.diary_entry_2 import *

"""
When we add two diary entries,
we get the entries back in the diary
entry list.
"""

def test_get_list_of_entries():
    diary = Diary()
    entry1 = DiaryEntry("28th July","I had a good day")
    entry2 = DiaryEntry("29th July","Today was also good")
    diary.add(entry1)
    diary.add(entry2)
    assert diary.entry_list == ["28th July: I had a good day", "29th July: Today was also good"]