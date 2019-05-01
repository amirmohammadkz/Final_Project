import os

import numpy as np
import pandas as pd


class OneHotGenerator:
    def __init__(self):
        self.oneHotWordsDF = pd.DataFrame()

    def make_one_hot(self, source, min_count=2):
        file = pd.read_pickle(source)
        self.oneHotWordsDF = self.oneHotWordsDF.append(file.loc[file["count"] >= min_count])
        self.oneHotWordsDF = self.oneHotWordsDF.append({'word': "unknown_words", 'count': None}, ignore_index=True)
        dummies = pd.get_dummies(self.oneHotWordsDF['word'], prefix='word')
        self.oneHotWordsDF = pd.concat([self.oneHotWordsDF, dummies], axis=1)
        # for word in self.oneHotWordsDF['word']:
        #     if int(self.oneHotWordsDF.loc[self.oneHotWordsDF['word'] == word]["word_" + word]) != 1:
        #         print("noooooooooo")
        # print(int(self.oneHotWordsDF.loc[self.oneHotWordsDF["word"] == "سلام"]['word_سلام']))

        return self.oneHotWordsDF

    def get_one_hot_row(self, word):
        row = self.oneHotWordsDF.loc[self.oneHotWordsDF["word"] == word]
        if row.empty:
            return self.oneHotWordsDF.loc[self.oneHotWordsDF["word"] == 'unknown_words']
        return row

    def get_one_hot_vector(self, word):
        row = self.get_one_hot_row(word)
        on_hot_df = row.drop(['word', 'count'], axis=1)
        return np.array(on_hot_df)[0]

    def get_one_hot_vector_v2(self, word):
        row = self.get_one_hot_row(word)
        on_hot_df = row.drop(['word', 'count'], axis=1)
        return on_hot_df

    def save_one_hot_df(self, dest):
        self.oneHotWordsDF.to_pickle(dest)

    def load_one_hot_df(self, source):
        self.oneHotWordsDF = pd.read_pickle(source)


if __name__ == "__main__":
    oneHotGenerator = OneHotGenerator()
    x = oneHotGenerator.make_one_hot("../tfidf/bow1/G_remove_unrelated/word_count.pkl", 200)
    path = "../generalDF/"
    if not os.path.exists(path):
        os.makedirs(path)
    x.to_pickle(path + "one_hot_words_df.pkl")
