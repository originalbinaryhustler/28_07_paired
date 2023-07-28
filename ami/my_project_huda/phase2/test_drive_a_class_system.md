"""
When we add two diary entries,
we get the entries back in the diary
entry list.
"""
diary = Diary()
entry1 = DiaryEntry("28th July","I had a good day")
entry2 = DiaryEntry("29th July","Today was also good")
diary.add(entry1)
diary.add(entry2)
diary.entry_list # => ["28th July: I had a good day",
"29th July: Today was also good"]

"""
When we call the all method on an instance of Diary,
we should get back a list of diary entries.
"""
diary = Diary()
entry1 = DiaryEntry("28th July","I had a good day")
entry2 = DiaryEntry("29th July","Today was also good")
diary.add(entry1)
diary.add(entry2)
diary.all() # =>
"28th July: I had a good day"
"29th July: Today was also good"

"""When we call the method count_words on an instance of
Diary we should get the number of words in all diary entries
"""
diary = Diary()
entry1 = DiaryEntry("28th July","I had a good day")
entry2 = DiaryEntry("29th July","Today was also good")
diary.add(entry1)
diary.add(entry2)
diary.count_words() # => 13

"""When we call the reading time method we should get
the reading time if the user were to read all diary entries
"""
diary = Diary()
entry1 = DiaryEntry("28th July","I had a good day")
entry2 = DiaryEntry("29th July","Today was also good")
diary.add(entry1)
diary.add(entry2)
diary.reading_time(13) # => 1

"""When we call #find_best_entry_for_reading_time, we
should get an instance of DiaryEntry representing the entry
that is closest to, but not over, the length that the user
could read in the minutes (minutes) they have given their
reading speed (wpm)
"""
diary = Diary()
entry1 = DiaryEntry("28th July","Good")
entry2 = DiaryEntry("29th July","Today was also good")
diary.add(entry1)
diary.add(entry2)
diary.find_best_entry_for_reading_time(4,1) # => 
"28th July: Good"