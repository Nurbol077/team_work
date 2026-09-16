"""Проект башталды"""

class Movie:
    def __init__(self, title, year):
        self.title = title
        self.year = year
    def info(self):
        print(f'Title:{self.title}\nYear:{self.year}')

m1 = Movie('Avengers: Endgame', 2019)
print(m1.info())