from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass
class Word:
    uid: UUID
    value: str
    translation: str

    def __post_init__(self):
        if self.uid is None:
            self.uid = uuid4()


@dataclass
class Chapter:
    uid: UUID
    book_uid: UUID
    number: int
    title: str
    new_words: list[UUID]

    def __post_init__(self):
        if self.uid is not None:
            self.uid = uuid4()


@dataclass
class Book:
    uid: UUID
    title: str
    chapters: list[UUID]

    def __post_init__(self):
        if self.uid is not None:
            self.uid = uuid4()


@dataclass
class Counter:
    uid: UUID
    value: int
    chapter: UUID
    word: UUID

    def __post_init__(self):
        if self.uid is not None:
            self.uid = uuid4()
