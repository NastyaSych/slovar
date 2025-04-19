import sys
from database import InMemoryRepository
from model import *

def main():
    db = InMemoryRepository()
    start_word = "ok"
    while(start_word[0] != 'n' and start_word != "exit"):
        start_word = input("Choose mode (vocabulary/statistics): ")
        if start_word == "exit":
                sys.exit("Goodbye")
        elif start_word[0] == 'v':
                curr_book = input("Enter book's name: ")
                if not db.is_book_exists(curr_book):
                    book_chapters = input("There is no book with such name. We will add it now. How many chapters in this book? ")
                    chapters = []
                    for chapt_num in range(1, book_chapters + 1):
                        chapter_name = input(f"Enter chapter {chapt_num} title (if it has no title, enter 0): ")
                        if chapter_name == '0':
                            chapter_name = f"Chapter {chapt_num}" 
                        chapters.append(Chapter(chapt_num, chapter_name, []))
                    new_book = Book(curr_book, chapters)
                    db.add_book(new_book)
                curr_num_chapter = input("Enter chapter's number: ")   
                word_name = input("Enter the word: ") 
                if db.is_word_exists(word_name):
                    print("Translation is:", db.get_translation(word_name))
                    # здесь счётчик вызова ++
                else:
                    translation = input("There is no such word in the vocabulary yet, add translation: ")              
                    new_word = Word(word_name, translation)
                    db.add_word(new_word)
                    curr_chapter = Chapter(Chapter.number == chapt_num)
                    db.add_new_word_in_chapter(curr_chapter)
                start_word = input("Want to continue? ")        
        elif start_word[0] == 's':
            curr_book = input("Enter book's name: ")
            while not db.is_book_exists(curr_book):
                curr_book = input("There is no book with such name. Please, enter again: ")
            curr_num_chapter = input("Enter chapter's number: ")
            curr_chapter = Chapter(Chapter.number == chapt_num)
            if len(Chapter.new_words) == 1:
                 print("There is only one (1) new word in this chapter")
            else:
                print(f"There are {len(Chapter.new_words)} new words in this chapter") 
        else:
            break        

if __name__ == "__main__":
    main()



