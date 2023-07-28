def check_text_includes_todo(text):
    if text == "":
        return False
    else:
        if '#TODO' not in text:
            return False
        else:
            return True