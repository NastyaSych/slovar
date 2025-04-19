def main():
    print("Hello from slovar!")


if __name__ == "__main__":
    main()


vocab = {}
start_word = "ok"
while(start_word[0] != 'n' and start_word != "exit"):
    start_word = input("Choose mode (vocabulary/statistics): ")
    if start_word == "exit":
        break
    if start_word[0] == 'v':
        book = input("Enter book's name: ")
        chapter = input("Enter chapter's number: ")
        word = input("Enter the word: ")
        isin_voc = 0
        for key in vocab:
            if word == key:
                print("Translation is:", vocab[word])
                isin_voc += 1
        if isin_voc == 0:
            add_word = input("There is no such word in the vocabulary yet, want to add? ")  
            if add_word[0] == 'y':
                vocab[word] = input("Ok, add translation: ")
                print(vocab)
            else:
                break
        start_word = input("Want to continue? ")        
    elif start_word[0] == 's':
        break
    else:
        break        

    



