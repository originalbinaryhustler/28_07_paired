def reading_time(text,wpm):
    if isinstance(text,str):
        minute = 60
        words_list = text.split()
        if text == "":
            return 'No text has been entered'
        else:
            return f"At your reading speed of {wpm} WPM it would take you {int(len(words_list)/wpm)} minutes and {int((len(words_list)/wpm)*minute)%60} seconds to read the given text."
    else:
        raise Exception("Error: Input type is incorrect.")