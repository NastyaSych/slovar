from typing import Dict
from model import *
from uuid import UUID, uuid4

class InMemoryRepository():
    
    _books: Dict[UUID, Book] = None
    _words: Dict[UUID, Word] = None
    _counters: Dict[UUID, Counter] = None
    _chapters: Dict[UUID, Chapter] = None

    def __init__(self):
        self._words = {}
        self._counters = {}
        self._books = {}
        self._chapters = {}

    def get_book_by_id(self, uid: UUID) -> Book:
        return self._books[uid]

    def get_book_by_title(self, title: str) -> Book:
        all_books = self._books.values()
        matched_books = [b for b in all_books if b.title == title]
        if len(matched_books) == 1:
            return matched_books[0]
        elif len(matched_books) == 0:
            raise Exception("There is no book with such title")
        else:
            raise Exception("There are more than one book with such title")
        
    def add_book(self, book: Book):
        self._books[book.uid] = book

    def is_book_with_title_exists(self, title: str) -> bool:
        all_books = self._books.values()
        matched_books = [b for b in all_books if b.title == title]
        if len(matched_books) == 1:
            return True
        elif len(matched_books) == 0:
            return False
        else:
            raise Exception("There are more than one book with such title")

    def add_new_word_in_chapter(self, chapter_uid: UUID, word_uid: UUID):
        self._chapters[chapter_uid].new_words.append(word_uid)

    def get_chapter_uid_by_number(self, chapter_number: int, book_uid: UUID) -> UUID:
        curr_book = self._books[book_uid]
        chapter_uids = curr_book.chapters
        chapters = [self._chapters[uid] for uid in chapter_uids]
        matched_chapters = [c for c in chapters if c.number == chapter_number]
        if len(matched_chapters) == 1:
            return matched_chapters[0].uid
        elif len(matched_chapters) == 0:
            raise Exception("There is no such chapter in the book")
        else:
            raise Exception("There are more than two chapters in the book")

    # def is_word_exists(self, value: str) -> bool:
    #     return value in self._vocab

    # def get_word(self, value: str) -> Word:
    #     return self._vocab[value]
        
    # def get_translation(self, value: str) -> str:
    #     return self.get_word(value).translation

    # def add_word(self, word: Word):
    #     self._vocab[word.value] = word