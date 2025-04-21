import sys
from database import InMemoryRepository
from model import Book, Chapter, Word


def vocabulary_mode(db: InMemoryRepository):
    curr_book = input("Enter book's name: ")
    if not db.is_book_with_title_exists(curr_book):
        num_chapters = int(
            input(
                "There is no book with such name. We will add it now. How many chapters are in this book? "
            )
        )
        new_book = Book(uid=None, title=curr_book, chapters=[])
        # выше у книги появляется uid при создании
        db.add_book(new_book)
        list_Chapters = []
        chapters = {}  # словарь номер главы - название
        for num_chapter in range(1, num_chapters + 1):
            chapters[num_chapter] = input(
                f"Enter title of chapter {num_chapter} (if it has no title, enter 0): "
            )
            if chapters[num_chapter] == "0":
                chapters[num_chapter] = f"Chapter {num_chapter}"
            new_chapter = Chapter(
                uid=None,
                book_uid=new_book.uid,
                number=num_chapter,
                title=chapters[num_chapter],
                new_words=[],
            )  # тут у главы появляется uid
            db.add_chapter(new_chapter)
            list_Chapters.append(new_chapter)
        db.add_chapters_to_book(list_Chapters, new_book.uid)
    curr_chapter_num = int(input("Enter chapter's number: "))
    word_name = input("Enter the word: ")
    if db.is_word_exists(word_name):
        print("Translation is:", db.get_translation(word_name))
        # здесь счётчик вызова ++
    else:
        translation = input(
            "There is no such word in the vocabulary yet, add translation: "
        )
        new_word = Word(uid=None, value=word_name, translation=translation)
        db.add_word(new_word)  # тут у слова появляется uid
        book_uid = db.get_book_by_title(curr_book).uid
        chapter_full = db.get_chapter_by_number(curr_chapter_num, book_uid)
        db.add_new_word_in_chapter(chapter_full.uid, new_word.uid)


def statistics_mode(db: InMemoryRepository):
    curr_book = input("Enter book's name: ")
    while not db.is_book_with_title_exists(curr_book):
        curr_book = input("There is no book with such name. Please, enter again: ")
    curr_chapter_num = int(input("Enter chapter's number: "))
    curr_chapter = db.get_chapter_by_number(
        curr_chapter_num, db.get_book_by_title(curr_book).uid
    )
    if len(curr_chapter.new_words) == 1:
        print("There is only one (1) new word in this chapter")
    elif len(curr_chapter.new_words) == 0:
        print("There are no new words in this chapter")
    else:
        print(f"There are {len(curr_chapter.new_words)} new words in this chapter")


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
