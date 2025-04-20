from typing import Dict
from model import Book, Chapter, Word, Counter
from uuid import UUID


class InMemoryRepository:
    _books: Dict[UUID, Book] = None
    _chapters: Dict[UUID, Chapter] = None
    _words: Dict[UUID, Word] = None
    _counters: Dict[UUID, Counter] = None

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

    def add_chapter(self, chapter: Chapter):
        self._chapters[chapter.uid] = chapter

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

    def add_chapters_to_book(self, chapters: list[Chapter], book_uid: UUID):
        for c in chapters:
            self._books[book_uid].chapters.append(c.uid)

    def is_word_exists(self, value: str) -> bool:
        all_words = self._words.values()
        matched_words = [w for w in all_words if w.value == value]
        if len(matched_words) == 1:
            return True
        else:
            return False

    def get_word_uid(self, value: str) -> UUID:
        all_words = self._words.values()
        matched_words = [w for w in all_words if w.value == value]
        return matched_words[0].uid

    def get_translation(self, value: str) -> str:
        return self._words[self.get_word_uid(value)].translation

    def add_word(self, word: Word):
        self._words[word.uid] = word
