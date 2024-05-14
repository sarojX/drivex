""" Member data model """

from dataclasses import dataclass, field
from typing import Set

@dataclass
class Member:
    id: int = None
    name: str = None
    dues: int = 0
    books: Set[int] = field(default_factory=set)
