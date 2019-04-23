import math
from hazm import *

from preprocess import DatasetReader
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class Sumerizer:
    def __init__(self, dataset_reader: DatasetReader):
        self.dataset_reader = dataset_reader
        pass


    def draw_chart(self, path, dic, title):
        plt.title("word count")
        width = 0.7
        indexes = np.arange(len(dic))
        plt.bar(indexes, dic.values(), align='edge', width=width)
        plt.xticks(indexes + width * 0.5, dic.keys())
        plt.setp(plt.gca().get_xticklabels(), rotation=30, horizontalalignment='right')
        plt.gca().minorticks_on()
        plt.gca().grid(which='both', linestyle='--', axis='y')
        dist_folder_name = path.split("/")[-2]
        print(dist_folder_name)
        dist = "../all_charts/new_version" + title + '/' + dist_folder_name + '.png'
        plt.savefig(dist)
        plt.show()


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


    def generate_person_word_count_chart(self, root_path):
        if root_path is not None:
            self.dataset_reader.set_root_path(root_path)
        folder_names = self.dataset_reader.get_file_names()
        for  folder in folder_names:
            folder = root_path + folder + '/'
            if root_path is not None:
                self.dataset_reader.set_root_path(folder)
            file_names = self.dataset_reader.get_file_names()
            dic = {}
            for file_name in file_names:
                if file_name != 'word_count.pkl':
                    total_file_name = folder + file_name
                    file = pd.read_pickle(total_file_name)
                    total_count = file['count'].sum()
                    dic[file_name.split(".")[0]] = total_count

            self.draw_chart(folder,dic, "person_word_count_chart")


    def generate_person_unique_word_count_chart(self, root_path):
        if root_path is not None:
            self.dataset_reader.set_root_path(root_path)
        folder_names = self.dataset_reader.get_file_names()
        for  folder in folder_names:
            folder = root_path + folder + '/'
            if root_path is not None:
                self.dataset_reader.set_root_path(folder)
            file_names = self.dataset_reader.get_file_names()
            dic = {}
            normal_dic = {}
            for file_name in file_names:
                if file_name != 'word_count.pkl':
                    total_file_name = folder + file_name
                    file = pd.read_pickle(total_file_name)
                    file = pd.read_pickle(total_file_name)
                    total_count_uniquewords = file.shape[0]
                    dic[file_name.split(".")[0]] = total_count_uniquewords
                    total_count = file['count'].sum()
                    normal_dic[file_name.split(".")[0]] = total_count_uniquewords / total_count

            self.draw_chart(folder,dic, "uniqueـwordsـwordـcount")
            self.draw_chart(folder, normal_dic, "uniqueـwordsـwordـcount_normalized")


    def generate_word_of_each_tweet_chart(self, root_path=None):
        if root_path is not None:
            self.dataset_reader.set_root_path(root_path)
        file_names = self.dataset_reader.get_file_names()
        list = []
        maxi = 0
        dist = "../all_charts/person_tweet_word_count/"
        for file_name in file_names:
            tweets = self.dataset_reader.read_file(file_name)
            for tweet in tweets:
                list.append(len(tweet.split(" ")))
                if len(tweet.split(" ")) > maxi:
                    maxi = len(tweet.split(" "))
            avg = sum(list)/len(list)

            plt.title("word of each tweet : " + file_name.split(".")[0])
            plt.hist(list,bins=80, range=[0, 80])
            plt.gca().minorticks_on()
            plt.gca().grid(which='both', linestyle='--', axis = 'y')
            dist_file = dist + file_name + '.png'
            plt.savefig(dist_file)
            plt.show()


if __name__ == "__main__":
    summerizer = Sumerizer(DatasetReader("../datasets_V2"))
   # summerizer.generate_person_tweet_count_chart()
    summerizer.generate_word_of_each_tweet_chart()
   # summerizer.generate_person_word_count_chart(root_path='../tfidf/bow1/')
   # summerizer.generate_person_unique_word_count_chart(root_path='../tfidf/bow1/')
   # summerizer.generate_unique_words_count_chart(root_path="../bows")
