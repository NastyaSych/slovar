import sys
from database import InMemoryRepository
from model import Book, Chapter, Word


def main():
    db = InMemoryRepository()
    start_word = "ok"
    while start_word != "no" and start_word != "exit":
        start_word = input("Choose mode (v for vocabulary, s for statistics): ")
        if start_word == "exit":
            sys.exit("Goodbye")
        if start_word == "v":
            curr_book = input("Enter book's name: ")
            if curr_book == "exit":
                sys.exit("Goodbye")
            if not db.is_book_with_title_exists(curr_book):
                num_chapters = input(
                    "There is no book with such name. We will add it now. How many chapters are in this book (without prologue)? "
                )
                new_book = Book(uid=None, title=curr_book, chapters=[])
                db.add_book(new_book)  # тут у книги появляется uid
                if num_chapters == "exit":
                    sys.exit("Goodbye")
                num_chapters = int(num_chapters)
                list_Chapters = []
                chapters = {}  # словарь номер главы - название
                chapters[0] = input(
                    "Is there prologue/prelude (enter title for yes, 0 for no): "
                )

                if chapters[0] == "0":
                    new_chapter = Chapter(
                        uid=None,
                        book_uid=new_book.uid,
                        number=0,
                        title=chapters[0],
                        new_words=[],
                    )
                    db.add_chapter(new_chapter)  # тут у главы появляется uid
                    list_Chapters.append(new_chapter)
                chapter_1 = input(
                    "Enter title of chapter 1 (if it has no title, enter 0; if all chapters have no title, enter 00 ): "
                )
                if chapter_1 == "0" or chapter_1 == "00":
                    chapters[1] = "Chapter 1"
                new_chapter = Chapter(
                    uid=None,
                    book_uid=new_book.uid,
                    number=1,
                    title=chapters[1],
                    new_words=[],
                )
                db.add_chapter(new_chapter)  # тут у главы появляется uid
                list_Chapters.append(new_chapter)
                for num_chapter in range(2, num_chapters + 1):
                    if chapter_1 == "00":
                        chapters[num_chapter] = f"Chapter {num_chapter}"
                    else:
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
                    )
                    db.add_chapter(new_chapter)  # тут у главы появляется uid
                    list_Chapters.append(new_chapter)
                db.add_chapters_to_book(list_Chapters, new_book.uid)
            curr_chapter_num = input("Enter chapter's number: ")
            if curr_chapter_num == "exit":
                sys.exit("Goodbye")
            curr_chapter_num = int(curr_chapter_num)
            word_name = input("Enter the word: ")
            if word_name == "exit":
                sys.exit("Goodbye")
            if db.is_word_exists(word_name):
                print("Translation is:", db.get_translation(word_name))
                # здесь счётчик вызова ++
            else:
                translation = input(
                    "There is no such word in the vocabulary yet, add translation: "
                )
                if translation == "exit":
                    sys.exit("Goodbye")
                new_word = Word(uid=None, value=word_name, translation=translation)
                db.add_word(new_word)  # тут у слова появляется uid
                book_uid = db.get_book_by_title(curr_book).uid
                chapter_uid = db.get_chapter_uid_by_number(curr_chapter_num, book_uid)
                db.add_new_word_in_chapter(chapter_uid, new_word.uid)
            start_word = input("Want to continue? ")
        elif start_word == "s":
            curr_book = input("Enter book's name: ")
            if curr_book == "exit":
                sys.exit("Goodbye")
            while not db.is_book_exists(curr_book):
                curr_book = input(
                    "There is no book with such name. Please, enter again: "
                )
                if curr_book == "exit":
                    sys.exit("Goodbye")
            curr_chapter_num = input("Enter chapter's number: ")
            if curr_chapter_num == "exit":
                sys.exit("Goodbye")
            curr_chapter_num = int(curr_chapter_num)
            curr_chapter = db.get_chapter_uid_by_number(
                curr_chapter_num, db.get_book_by_title(curr_book)
            )
            if len(curr_chapter.new_words) == 1:
                print("There is only one (1) new word in this chapter")
            elif len(curr_chapter.new_words) == 0:
                print("There are no new words in this chapter")
            else:
                print(f"There are {len(Chapter.new_words)} new words in this chapter")
        else:
            sys.exit("Goodbye")


if __name__ == "__main__":
    main()
