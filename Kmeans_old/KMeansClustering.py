from Kmeans_old.OneHotEncoder import OneHotGenerator
from preprocess import DatasetReader
import numpy as np
from sklearn.cluster import KMeans

if __name__ == "__main__":
    one_hot_encoder = OneHotGenerator("../word_count")
    one_hot_list = one_hot_encoder.make_one_hot()
    one_hot_list_size = len(one_hot_list)
    dataset_reader = DatasetReader("../ngrams/bow1/E_remove_extra")
    file_names = dataset_reader.get_file_names()
    person_dict = {}
    for file_name in file_names:
        total_count = 0
        person_dict[file_name] = np.zeros(one_hot_list_size)
        print(file_name)
        lines = dataset_reader.read_file(file_name, False)
        for line in lines:
            try:
                word = line.split(",")[0]
                count = int(line.split(",")[1])
                person_dict[file_name] += one_hot_encoder.get_one_hot(word) * count
                total_count += count
            except Exception as e:
                print(e)
                print(line)
            # if total_count > 100:
            #     break
        person_dict[file_name] /= total_count
    array = []
    for key in person_dict.keys():
        array.append(person_dict[key])
    array = np.array(array)
    kmeans = KMeans(n_clusters=4, random_state=0).fit(array)
    for index, key in enumerate(person_dict.keys()):
        print(key + ": " + str(kmeans.labels_[index]))
    # print(key for key in person_dict.keys())
    # print(person_dict)
