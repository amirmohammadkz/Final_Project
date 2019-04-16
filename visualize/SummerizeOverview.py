import math
from hazm import *

from preprocess import DatasetReader
import matplotlib.pyplot as plt
import numpy as np


class Sumerizer:
    def __init__(self, dataset_reader: DatasetReader):
        self.dataset_reader = dataset_reader
        pass

    def generate_person_tweet_count_chart(self, root_path=None):
        if root_path is not None:
            self.dataset_reader.set_root_path(root_path)
        file_names = self.dataset_reader.get_file_names()
        dic = {}
        for file_name in file_names:
            dic[file_name.split(".")[0]] = len(self.dataset_reader.read_file(file_name))
        plt.title("tweet count")
        width = 0.7
        indexes = np.arange(len(dic))
        plt.bar(indexes, dic.values(), align='edge', width=width)
        plt.xticks(indexes + width * 0.5, dic.keys())
        plt.setp(plt.gca().get_xticklabels(), rotation=30, horizontalalignment='right')
        plt.gca().minorticks_on()
        plt.gca().grid(which='major', color='red')
        plt.gca().grid(which='minor', linestyle='--')
        plt.show()

    def generate_mean_tweet_words_count_chart(self, root_path=None):
        if root_path is not None:
            self.dataset_reader.set_root_path(root_path)
        file_names = self.dataset_reader.get_file_names()
        dic = {}
        for file_name in file_names:
            tweets = self.dataset_reader.read_file(file_name)
            words = [len(word_tokenize(tweet)) for tweet in tweets]
            dic[file_name.split(".")[0]] = np.mean(words)
        plt.title("mean tweet word count")
        width = 0.7
        indexes = np.arange(len(dic))
        plt.bar(indexes, dic.values(), align='edge', width=width)
        plt.xticks(indexes + width * 0.5, dic.keys())
        plt.setp(plt.gca().get_xticklabels(), rotation=30, horizontalalignment='right')
        plt.gca().minorticks_on()
        plt.gca().grid(which='major', color='red')
        plt.gca().grid(which='minor', linestyle='--')
        plt.show()

    def generate_unique_words_count_chart(self, threshold=1, root_path=None):
        if root_path is not None:
            self.dataset_reader.set_root_path(root_path)
        file_names = self.dataset_reader.get_file_names()
        dic = {}
        for file_name in file_names:
            bow = self.dataset_reader.read_csv_file(file_name)
            print(file_name)
            print(bow)
            tmp = bow.loc[bow['word'] == "دانلود"]
            tmp = bow.loc[bow['word'] == "حلالیت"]
            print(tmp)
            dic[file_name.split(".")[0]] = len(bow)
        plt.title("unique words")
        width = 0.7
        indexes = np.arange(len(dic))
        plt.bar(indexes, dic.values(), align='edge', width=width)
        plt.xticks(indexes + width * 0.5, dic.keys())
        plt.setp(plt.gca().get_xticklabels(), rotation=30, horizontalalignment='right')
        plt.gca().minorticks_on()
        plt.gca().grid(which='major', color='red')
        plt.gca().grid(which='minor', linestyle='--')
        plt.show()


if __name__ == "__main__":
    summerizer = Sumerizer(DatasetReader("../datasets"))
    summerizer.generate_person_tweet_count_chart()
    summerizer.generate_unique_words_count_chart(root_path="../bows")
