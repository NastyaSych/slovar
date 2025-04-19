from typing import Dict
from model import *

class InMemoryRepository():
    
    _books: Dict[str, Book] = None
    _vocab: Dict[str, Word] = None
    _counters: list[Counter] = None
    _new_words: Dict[Chapter, list[Word]] = None

    def __init__(self):
        self._vocab = {}
        self._counters = []

    def add_book(self, book: Book):
        self._books.append(book)

    def add_new_word_in_chapter(self, chapter: Chapter, word: Word):
        self._new_words[Chapter].append(Word)

    def is_book_exists(self, value: str) -> bool:
        return value in self._books    

    def is_word_exists(self, value: str) -> bool:
        return value in self._vocab

    def get_word(self, value: str) -> Word:
        return self._vocab[value]
        
    def get_translation(self, value: str) -> str:
        return self.get_word(value).translation

    def add_word(self, word: Word):
        self._vocab[word.value] = word