# File: lib/gratitudes.py

class Gratitudes:
    def __init__(self):
        self.gratitudes = []

    def add(self, gratitude):
        self.gratitudes.append(gratitude)

    def format(self):
        formatted = "Be grateful for: "
        formatted += ", ".join(self.gratitudes)
        return formatted

class Present:
    def __init__(self):
        self.contents = None

    def wrap(self, contents):
        if self.contents is not None:
            raise Exception("A contents has already been wrapped.")
        self.contents = contents

    def unwrap(self):
        if self.contents is None:
            raise Exception("No contents have been wrapped.")
        return self.contents