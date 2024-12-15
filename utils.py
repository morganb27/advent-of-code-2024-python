from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: float
    y: float

    def __add__(self, right_side: 'Point') -> 'Point':
        return Point(self.x + right_side.x, self.y + right_side.y)
    
    def __sub__(self, right_side: 'Point') -> 'Point':
        return Point(self.x - right_side.x, self.y - right_side.y)
    
    def __mul__(self, factor: 'int') -> 'Point':
        return Point(self.x * factor, self.y * factor)
    
    def neighbours(self) -> list['Point']:
        return [self + d for d in DIRS_4]
    

DIRS_8 = [
    Point(0, 1),   #N
    Point(1, 1),   #NE
    Point(1, 0),   #E
    Point(-1, 1),  #SE
    Point(0, -1),  #S
    Point(-1, -1), #SW
    Point(-1, 0),  #W
    Point(1, -1)   #NW
]

DIRS_4 = [
    Point(0, 1),   #N
    Point(1, 0),   #E
    Point(0, -1),  #S
    Point(-1, 0),  #W
]