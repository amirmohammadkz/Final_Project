from hazm import Normalizer, word_tokenize, Stemmer, Lemmatizer

from preprocess.dataset_reader import DatasetReader


class WordCountMaker:
    def __init__(self):
        self.word_count = {}

    def add_word_count_list(self, word_count_list: list):
        for word_count in word_count_list:
            try:
                word = word_count.split(",")[0]
                count = int(word_count.split(",")[1])
                if self.word_count.get(word) is None:
                    self.word_count[word] = count
                else:
                    self.word_count[word] += count
            except Exception as e:
                print(e)
                print(word_count)

    def get_word_count(self):
        return self.word_count


if __name__ == "__main__":
    dataset_reader = DatasetReader("../ngrams/bow1/E_remove_extra")
    print("bow read")
    wordCountMaker = WordCountMaker()
    for name in dataset_reader.get_file_names():
        print(name + " bow...")
        bows = dataset_reader.read_file(name, False)
        print(bows[:10])
        wordCountMaker.add_word_count_list(bows)
    wordCountMaker.get_word_count()
    print("generating word count...")
    word_count = wordCountMaker.get_word_count()
    word_count_file = open("../word_count", "w", encoding="utf8")
    print("saving word count...")
    for key in word_count.keys():
        try:
            word_count_file.write(key + "," + str(word_count[key]) + "\n")
        except Exception as e:
            print(e)
            print(key)
            print(word_count[key])
            print("#####")
    word_count_file.close()
