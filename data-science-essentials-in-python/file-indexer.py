import os
import pickle
from collections import Counter

def words_in_file(path, filename):
    with open(os.path.join(path, filename), "rb") as f:
        s = f.read()
    return s.decode('utf-8').split()

def save_words_in_files(path, filename, word_dict):
    with open(os.path.join(path, filename), "wb") as f:
        pickle.dump(word_dict, f)

def load_words_in_files(path, filename):
    with open(os.path.join(path, filename), "rb") as f:
        word_dict = pickle.load(f)
    return word_dict

def main():
    path = '.'
    word_dict = {}
    # list of files current directory
    for filename in os.listdir(path):
        # is file?
        if not os.path.isfile(os.path.join(path, filename)):
            continue
        # is ignore file?
        if filename.startswith('.'):
            continue
        words = words_in_file(path, filename)
        for word in words:
            if word in word_dict:
                word_dict[word].update([filename])
            else:
                word_dict[word] = set([filename])
    # print(word_dict)

    # save to file(pickle)
    save_filename = 'word_dict.pickle'
    save_words_in_files(path, save_filename, word_dict)

    # load from file
    word_dict = load_words_in_files(path, save_filename)
    print(word_dict)


if __name__ == "__main__":
    main()