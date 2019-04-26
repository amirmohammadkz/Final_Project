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


