from hazm import Normalizer, word_tokenize, Stemmer, Lemmatizer
from pandas import DataFrame
import pandas as pd

from preprocess.dataset_reader import DatasetReader


class WordCountMaker:
    def __init__(self):
        self.word_count = pd.DataFrame(columns=["word", "count"])

    def add_word_count_list(self, word_count_list: DataFrame):
        merged = pd.merge(self.word_count, word_count_list[["word", "count"]], how="outer", on=["word"]).fillna(0)
        merged["count"] = merged["count_x"] + merged["count_y"]
        self.word_count = merged[["word", "count"]]
        print(self.word_count.loc[self.word_count["word"] == "سلام"])

        # print(self.word_count.head(5))

    def get_word_count(self):
        return self.word_count


if __name__ == "__main__":
    root = "../tfidf/bow1/G_remove_unrelated"
    dataset_reader = DatasetReader(root)
    print("bow read")
    wordCountMaker = WordCountMaker()
    for name in dataset_reader.get_file_names():
        if name == "word_count.pkl":
            continue

        print(name + " bow...")
        bows = dataset_reader.read_pkl_file(name)
        # print(bows[["word", "count"]][:10])
        wordCountMaker.add_word_count_list(bows)
    wordCountMaker.get_word_count()
    print("generating word count...")
    word_count = wordCountMaker.get_word_count()
    word_count.to_pickle(root+"/word_count.pkl")
    print(word_count.loc[word_count["word"] == "سلام"])
