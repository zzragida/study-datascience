import nltk
from nltk.tokenize import WordPunctTokenizer
# nltk.download()

def main():
    wn = nltk.corpus.wordnet
    print(wn.synsets('cat'))

    x = wn.synset('cat.n.01')
    y = wn.synset('lynx.n.01')
    print(x.path_similarity(y))

    result = [simxy.definition() for simxy in max(
        (x.path_similarity(y), x, y)
        for x in wn.synsets('cat')
        for y in wn.synsets('dog')
        if x.path_similarity(y)
    )[1:]]
    print(result)

    # tokenizer
    text = 'hello world'
    word_punct = WordPunctTokenizer()
    print(word_punct.tokenize(text))


if __name__ == "__main__":
    main()