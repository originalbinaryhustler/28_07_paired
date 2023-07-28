class Diary():
    def __init__(self):
        self.entry_list = []
    
    def add(self, diary_entry):
        print(f'self.entry_list: {self.entry_list}')
        self.entry_list.append(f'{diary_entry.title}: {diary_entry.contents}')