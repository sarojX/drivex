"""book data model"""

from dataclasses import dataclass

@dataclass
class Book:
    id: int
    title: str
    price: float
    stockcount: int
