
# https://medium.com/@omerg7493/pythons-data-class-59098f4a2044
# https://realpython.com/python-data-classes/

from dataclasses import dataclass


@dataclass
class DataClassCard:
    rank: str
    suit: str

queen_of_hearts = DataClassCard('Q', 'Hearts')
print(queen_of_hearts.rank)

queen_of_hearts = DataClassCard(rank='Q', suit='Hearts')
print(queen_of_hearts == DataClassCard('Q', 'Hearts'))

class RegularCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self): 
        return (f'{self.__class__.__name__}'
                f'(rank={self.rank!r}, suit={self.suit!r})')

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.rank, self.suit) == (other.rank, other.suit)


from dataclasses import dataclass

@dataclass
class Position:
    name: str
    lon: float
    lat: float


pos = Position('Oslo', 10.8, 59.9)
print(pos)
pos.lat
print(f'{pos.name} is at {pos.lat}°N, {pos.lon}°E')

#si puo' anche creare in questo modo

from dataclasses import make_dataclass
Position = make_dataclass('Position', ['name', 'lat', 'lon'])
