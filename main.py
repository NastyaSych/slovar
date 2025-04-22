import sys
from database import InMemoryRepository
from model import Book, Chapter, Word
from uuid import UUID


def create_new_chapter(num_chapter: int, new_book_uid: UUID):
    chapter = input(
        f"Enter title of chapter {num_chapter} (if it has no title, enter 0): "
    )
    if chapter == "0":
        chapter = f"Chapter {num_chapter}"
    new_chapter = Chapter(
        uid=None,
        book_uid=new_book_uid,
        number=num_chapter,
        title=chapter,
        new_words=[],
    )  # тут у главы появляется uid
    return new_chapter


def create_new_book(db: InMemoryRepository, curr_book):
    num_chapters = int(
        input(
            "There is no book with such name. We will add it now. How many chapters are in this book? "
        )
    )
    new_book = Book(uid=None, title=curr_book, chapters=[])
    # выше у книги появляется uid при создании
    db.add_book(new_book)
    list_Chapters = []
    for num_chapter in range(1, num_chapters + 1):
        new_chapter = create_new_chapter(num_chapter, new_book.uid)
        db.add_chapter(new_chapter)
        list_Chapters.append(new_chapter)
    db.add_chapters_to_book(list_Chapters, new_book.uid)


def vocabulary_mode(db: InMemoryRepository):
    curr_book = input("Enter book's name: ")
    if not db.is_book_with_title_exists(curr_book):
        create_new_book(db, curr_book)
    curr_chapter_num = int(input("Enter chapter's number: "))
    word_name = input("Enter the word: ")
    if db.is_word_exists(word_name):
        print("Translation is:", db.get_translation(word_name))
        book_uid = db.get_book_by_title(curr_book).uid
        chapter_uid = db.get_chapter_by_number(curr_chapter_num, book_uid)
        db.counter_inc(chapter_uid, db.get_word_uid(word_name))
    else:
        translation = input(
            "There is no such word in the vocabulary yet, add translation: "
        )
        new_word = Word(uid=None, value=word_name, translation=translation)
        db.add_word(new_word)  # тут у слова появляется uid
        book_uid = db.get_book_by_title(curr_book).uid
        chapter_full_uid = db.get_chapter_by_number(curr_chapter_num, book_uid)
        db.add_new_word_in_chapter(chapter_full_uid, new_word.uid)
        db.counter_inc(chapter_full_uid, new_word.uid)


def new_words_number_book(db: InMemoryRepository, curr_book: str):
    curr_book_full = db.get_book_by_title(curr_book)
    new_words_num = 0
    for ch_uid in curr_book_full.chapters:
        new_words_num += db.get_num_new_words_in_chapter(ch_uid)
    if new_words_num == 1:
        print("There is only one (1) new word in this book")
    elif new_words_num == 0:
        print("There are no new words in this book")
    else:
        print(f"There are {new_words_num} new words in this book")
    pass


def calls_number_book(db: InMemoryRepository, word_inq: str, curr_book: str):
    curr_book_full = db.get_book_by_title(curr_book)
    calls_num = 0
    word_uid = db.get_word_uid(word_inq)
    for ch_uid in curr_book_full.chapters:
        calls_num += db.get_counter(ch_uid, word_uid).value
    if calls_num == 1:
        print(f"There is only one (1) call for word {word_inq} in this book")
    elif calls_num == 0:
        print(f"There are no calls for word {word_inq} in this book")
    else:
        print(f"There are {calls_num} calls for word {word_inq} in this book")
    pass


def new_words_number_chapter(
    db: InMemoryRepository, curr_chapter_num: int, curr_book: str
):
    curr_chapter = db.get_chapter_by_number(
        curr_chapter_num, db.get_book_by_title(curr_book)
    )
    if len(curr_chapter.new_words) == 1:
        print("There is only one (1) new word in this chapter")
    elif len(curr_chapter.new_words) == 0:
        print("There are no new words in this chapter")
    else:
        print(f"There are {len(curr_chapter.new_words)} new words in this chapter")


def calls_number_chapter(
    db: InMemoryRepository, word_inq: str, curr_chapter_num: int, curr_book: str
):
    book_uid = db.get_book_by_title(curr_book).uid
    chapter_uid = db.get_chapter_by_number(curr_chapter_num, book_uid)
    word_uid = db.get_word_uid(word_inq)
    number = db.get_counter(chapter_uid, word_uid).value
    if number == 1:
        print(f"There is only one (1) call for word {word_inq} in this chapter")
    elif number == 0:
        print(f"There are no calls for word {word_inq} in this chapter")
    else:
        print(f"There are {number} calls for word {word_inq} in this chapter")


def num_all_words(db):
    new_words = db.get_len_list("words")
    if new_words == 1:
        print("There is only one (1) word in vocabulary")
    elif new_words == 0:
        print("There are no wordd in vocabulary")
    else:
        print(f"There are {new_words} words in vocabulary")


def num_all_calls(db, word_inq: str):
    word_inq_uid = db.get_word_uid(word_inq)
    matched_count = db.get_counter_for_word(word_inq_uid)
    if matched_count == 1:
        print(f"There is only one(1) call for word {word_inq} for all time")
    elif matched_count == 0:
        print(f"There are no calls for word {word_inq} for all time")
    else:
        print(f"There are {matched_count} calls for word {word_inq} for all time")


def statistics_mode(db: InMemoryRepository):
    stat_type = int(
        input(
            "What information you want to get? Enter 1 for number of new words, 2 for number of calls: "
        )
    )
    stat_range = int(
        input(
            "Enter 0 if you want complete info, 1 if you want info about book, 2 - about chapter: "
        )
    )
    if stat_range == 0:
        if stat_type == 1:  # количество новых слов вообще
            num_all_words(db)
        else:  # количество вызовов слова вообще
            word_inq = input("Enter word: ")
            num_all_calls(db, word_inq)
    elif stat_range == 1:
        curr_book = input("Enter book's name: ")
        while not db.is_book_with_title_exists(curr_book):
            curr_book = input("There is no book with such name. Please, enter again: ")
        if stat_type == 1:  # количество новых слов в книге
            new_words_number_book(db, curr_book)
        else:  # количество вызовов в книге
            word_inq = input("Enter word: ")
            calls_number_book(db, word_inq, curr_book)
    else:
        curr_book = input("Enter book's name: ")
        while not db.is_book_with_title_exists(curr_book):
            curr_book = input("There is no book with such name. Please, enter again: ")
        curr_chapter_num = int(input("Enter chapter's number: "))
        if stat_type == 1:  # количество новых слов в главе
            new_words_number_chapter(db, curr_chapter_num, curr_book)
        else:  # количество вызовов слова в главе
            word_inq = input("Enter word: ")
            calls_number_chapter(db, word_inq, curr_chapter_num, curr_book)


def main():
    db = InMemoryRepository()
    start_word = "ok"
    while start_word != "no" and start_word != "exit":
        start_word = input("Choose mode (v for vocabulary, s for statistics): ")
        if start_word == "v":
            vocabulary_mode(db)
            start_word = input("Want to continue? ")
        elif start_word == "s":
            statistics_mode(db)
            start_word = input("Want to continue? ")
        else:
            sys.exit("Goodbye")


if __name__ == "__main__":
    main()
