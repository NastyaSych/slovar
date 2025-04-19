from dataclasses import dataclass 

@dataclass
class Word:
    value: str
    translation: str
    
@dataclass
class Chapter:
    number: int
    title: str
    new_words: list[Word]    

@dataclass
class Book:
    title: str
    chapters: list[Chapter]

@dataclass
class Counter:
    value: int
    chapter: Chapter
    word: Word
