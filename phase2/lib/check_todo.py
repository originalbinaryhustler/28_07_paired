# First attempt
# def check_todo(text: str):
#     string_split = text.split()
#     for word in string_split:
#         if '#TODO' in word:
#             return True
#     return False

# Refactored
def check_todo(text: str):
    words_list: str = [word for word in text.split() if '#TODO' in word]
    return len(words_list) > 0