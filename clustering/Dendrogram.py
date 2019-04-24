import os

from scipy.cluster import hierarchy

from preprocess import DatasetReader
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

if __name__ == "__main__":
    dataset_reader = DatasetReader("../one_hots")
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
        #
        #     hierarchy.set_link_color_palette(['m', 'c', 'y', 'k'])
        #     fig, axes = plt.subplots(1, 2, figsize=(8, 3))
        #     dn1 = hierarchy.dendrogram(Z, ax=axes[0], above_threshold_color='y',
        #
        #                                orientation='top')
        #     dn2 = hierarchy.dendrogram(Z, ax=axes[1],
        #                                above_threshold_color='#bcbddc',
        #
        #                                orientation='right')
        # hierarchy.set_link_color_palette(None)  # reset to default after use
        # plt.show()
        table_name = file_name.split(".")[0]
        path = "../all_charts/dendrogram"
        if path is None:
            plt.show()
        else:
            if not os.path.exists(path):
                os.makedirs(path)
            print(path + "/" + table_name + ".png")
            plt.savefig(path + "/" + table_name + ".png")
            plt.close('all')
