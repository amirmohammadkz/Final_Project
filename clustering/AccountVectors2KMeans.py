from preprocess.dataset_reader import DatasetReader
import numpy as np
from sklearn.cluster import KMeans


def convert(root_input):
    dataset_reader = DatasetReader(root_input)
    all_names = dataset_reader.get_file_names()
    for file_name in all_names:
        for k in range(4, 5):
            print(file_name, "#############################")
            data = dataset_reader.read_pkl_file(file_name)
            kmeans = KMeans(n_clusters=k, random_state=0).fit(np.vstack(data['vector'].values))
            for index, row in data.iterrows():
                print(row['name'], ": ", kmeans.labels_[index])
            # print("k:", k, " cost:", kmeans.inertia_)


if __name__ == "__main__":
    r_input = "../one_hots"
    convert(r_input)
