import random

class quotes:
    def __init__(self):
        self.quotes = []
        self.count = 0
        self.length = 0

    def load(self):
        with open('quotes.txt', 'r') as q:
            self.quotes = q.readlines()
        self.length = len(self.quotes)

    def rotate(self):
        self.count += 1
        self.quotes.append(self.quotes.pop(0))

    def shuffle(self):
        self.count = 0
        random.shuffle(self.quotes)

    def add(self, newquote):
        newquote = '\n' + ''.join(newquote)
        with open('quotes.txt', 'a') as q:
            q.write(newquote)