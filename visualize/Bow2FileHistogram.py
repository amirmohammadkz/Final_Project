import os

import matplotlib.pyplot as plt
import numpy as np

from preprocess.dataset_reader import DatasetReader


def convert(root_input, root_output):
    dataset_reader = DatasetReader(root_input)
    print(dataset_reader.get_nested_file_names())
    cat_lines = {}
    for person in dataset_reader.get_nested_file_names()[0][1]:
        cat_lines[person] = [[], []]
        for cat in dataset_reader.get_nested_file_names():
            # dataset_reader.set_root_path(cat[0])
            cat_lines[person][0].append(cat[0].split("/")[-1])
            cat_lines[person][1].append(
                len(dataset_reader.read_csv_file(cat[0][len(dataset_reader.root_path):] + "/" + person)))
    print(cat_lines)

    for person, data in cat_lines.items():
        plt.figure(figsize=(10, 11))
        plt.title(person)
        plt.plot(data[1])
        plt.xticks(np.arange(len(data[0])), data[0])
        plt.setp(plt.gca().get_xticklabels(), rotation=30, horizontalalignment='right')
        path = root_output
        plt.grid()
        if path is None:
            plt.show()
        else:
            if not os.path.exists(path):
                os.makedirs(path)

        plt.savefig("{}/{}.png".format(path, person.split(".")[0]))
        plt.clf()
        # plt.show()
        print(person)
        print(data)


if __name__ == "__main__":
    pass
