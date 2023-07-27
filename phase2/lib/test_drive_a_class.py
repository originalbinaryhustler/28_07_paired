class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.diary_entry = []

    def format(self):
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        self.diary_entry.append('My {self.title}: {self.contents}')
        return f'My {self.title}: {self.contents}'

    def count_words(self):
        # Returns:
        #   int: the number of words in the diary entry
        return len(self.format().split())

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        return (len(self.format().split())) // wpm

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        words_read = wpm // minutes
        pop_num = 0
        words_read_list = []
        entry_format = format()
        entry_split = entry_format.split()
        while pop_num < words_read:
            words_read_list.append(entry_split[pop_num])
            pop_num += 1
        return ' '.join(words_read_list)