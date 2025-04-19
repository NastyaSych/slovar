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
        if start_word[0] == 'v':
            value = input("Enter the word: ") 
            if db.is_word_exists(value):
                print("Translation is:", db.get_translation(value))
            else:
                translation = input("There is no such word in the vocabulary yet, add translation: ")              
                new_word = Word(value, translation)
                db.add_word(new_word)
            start_word = input("Want to continue? ")        
        elif start_word[0] == 's':
            break
        else:
            break        

if __name__ == "__main__":
    main()



