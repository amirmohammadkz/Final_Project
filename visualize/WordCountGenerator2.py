import numpy as np
from bidi.algorithm import get_display
import matplotlib.pyplot as plt
import arabic_reshaper

from preprocess import DatasetReader


class WordCountGenerator:
    def __init__(self):
        pass

    # todo: refactor for subplot
    def generate_word_count_graph(self, table_name, words, counts, axe: plt.Subplot):
        words = [get_display(arabic_reshaper.reshape(word)) for word in words]
        indexes = np.arange(len(words))
        width = 0.7
        # plt.subplot(position[0], position[1], position[2])
        axe.set_title(table_name)
        axe.bar(indexes, counts, align='edge', width=width)
        axe.set_xticks(indexes + width * 0.5, words)
        axe.set_xticklabels(words)
        # return ax
        # axe.gca().minorticks_on()
        # axe.gca().grid(which='major', color='red')
        # axe.gca().grid(which='minor', linestyle='--')

    def generate_full_chart(self, table_name, df, fields, item_count, path=None):
        fig = plt.figure(figsize=(40, 15))  # width:20, height:3
        plt.gcf().suptitle(table_name)
        fig.subplots_adjust(top=0.88, hspace=1)
        _, axes = plt.subplots(4)

        # print(subplots)
        for index, field in enumerate(fields):
            print(axes[index])
            df = df.sort_values(by=[field], ascending=False)
            self.generate_word_count_graph(field, df.iloc[:item_count]["word"],
                                           df.iloc[:item_count][field], axes[index])
        # plt.setp(axes, rotation=30, horizontalalignment='right')

        if path is None:
            plt.show()
        else:
            plt.savefig(path + "/" + table_name + ".png")


if __name__ == "__main__":
    dataset_reader = DatasetReader("../tfidf3")
    # name = [0]
    value = 100

    for name in dataset_reader.get_file_names():
        name_file = dataset_reader.read_pkl_file(name)
        items = ["count", "TF", "IDF", "TFIDF"]
        word_count_generator = WordCountGenerator()
        word_count_generator.generate_full_chart(name.split(".")[0], name_file, items, value)
        # for item in items:
        #     name_file = name_file.sort_values(by=[item], ascending=False)
        #     print(name_file.iloc[:value])
        #     print("all other" + str(name_file.iloc[value:][item].sum()))
        #     word_count_generator = WordCountGenerator()
        #     word_count_generator.generate_word_count_graph(name, name_file.iloc[:value]["word"],
        #                                                    name_file.iloc[:value][item])
        # word_count_generator.generate_word_count_raph(dic)
