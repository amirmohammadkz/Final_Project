import os

from scipy.cluster import hierarchy

from preprocess.dataset_reader import DatasetReader
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def convert(root_input, root_output):
    dataset_reader = DatasetReader(root_input)
    all_names = dataset_reader.get_file_names()
    for file_name in all_names:
        print(file_name, "#############################")
        data = dataset_reader.read_pkl_file(file_name)
        vector = np.vstack(data['vector'].values)
        print(vector)
        Z = hierarchy.linkage(vector, 'single')
        plt.figure(figsize=(10, 8))
        names = data['name'].values
        plt.xticks(np.arange(len(names)), names)
        plt.title(file_name.split(".")[0])
        dn = hierarchy.dendrogram(Z, labels=names)
        plt.setp(plt.gca().get_xticklabels(), rotation=30, horizontalalignment='right')
        plt.grid()

        print(names)
        table_name = file_name.split(".")[0]
        path = root_output
        if path is None:
            plt.show()
        else:
            if not os.path.exists(path):
                os.makedirs(path)
            print(path + "/" + table_name + ".png")
            plt.savefig(path + "/" + table_name + ".png")
            plt.close('all')


if __name__ == "__main__":
    r_input = "../one_hots"
    r_output = "../all_charts/dendrogram"
    convert(r_input, r_output)
