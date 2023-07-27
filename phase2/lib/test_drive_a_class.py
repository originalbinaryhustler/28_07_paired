class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.chunk_count = 1

    def format(self):
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
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
        if isinstance(wpm, bool):
            raise Exception('Error: WPM should be of type integer.')
        elif isinstance(wpm, int):
            return (len(self.format().split())) // wpm
        else:
            raise Exception('Error: WPM should be of type integer.')


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
        self.words_read_list = []
        entry_format = self.format()
        print(f'entry format: {entry_format}')
        entry_split = entry_format.split()
        print(f'entry_split: {entry_split}')
        while pop_num < words_read:
            if self.chunk_count == 1:
                print('Iteration starts here')
                self.words_read_list.append(entry_split[pop_num])
                print(f'self.words_read_list: {self.words_read_list}')
                print(f'pop_num starts as: {pop_num}')
                pop_num += 1
                print(f'pop num after count: {pop_num}')
                print(f'amount of words to be read: {words_read}')
                print(f'self.chunk_count starts as: {self.chunk_count}')
                self.chunk_count + 1
                print(f'self.chunk_count after count: {self.chunk_count}')
                print('Iteration ends here \n')
            else:
                # print('Iteration starts here')
                # self.words_read_list.append(entry_split[pop_num + words_read])
                # pop_num += 1
                # self.chunk_count + 1
                ans = entry_split[words_read:(words_read * self.chunk_count)]
                return ' '.join(ans)
        self.chunk_count += 1
        return ' '.join(self.words_read_list)
    '''
    
    '''