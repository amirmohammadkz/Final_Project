import os
from pathlib import Path

import numpy as np
from bidi.algorithm import get_display
import matplotlib.pyplot as plt
import arabic_reshaper

from preprocess.dataset_reader import DatasetReader


class WordCountGenerator:
    def __init__(self):
        pass

    def generate_word_count_graph(self, table_name, words, counts, position):
        try:
            words = [get_display(arabic_reshaper.reshape(word)) for word in words]
        except Exception as e:
            print(e)
        indexes = np.arange(len(words))
        width = 0.7
        plt.subplot(position[0], position[1], position[2])
        plt.title(table_name)
        plt.bar(indexes, counts, align='edge', width=width)
        plt.xticks(indexes + width * 0.5, words)
        plt.setp(plt.gca().get_xticklabels(), rotation=30, horizontalalignment='right')
        plt.gca().minorticks_on()
        plt.gca().grid(which='major', color='red')
        plt.gca().grid(which='minor', linestyle='--')

    def generate_full_chart(self, table_name, df, fields, item_count, path=None):
        fig = plt.figure(figsize=(40, 15))  # width:20, height:3
        plt.gcf().suptitle(table_name)
        fig.subplots_adjust(top=0.88, hspace=1)
        for index, field in enumerate(fields):
            df = df.replace("$$ی", "dollardollarی").sort_values(by=[field], ascending=False)
            self.generate_word_count_graph(field, df.iloc[:item_count]["word"],
                                           df.iloc[:item_count][field], (len(fields), 1, index + 1))
        if path is None:
            plt.show()
        else:
            if not os.path.exists(path):
                os.makedirs(path)
            print(path + "/" + table_name + ".png")
            plt.savefig(path + "/" + table_name + ".png")
            plt.close('all')
