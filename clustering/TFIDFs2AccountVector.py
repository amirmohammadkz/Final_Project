import os
import time

from clustering.OneHotEncoder import OneHotGenerator
from preprocess.dataset_reader import DatasetReader
import numpy as np
from sklearn.cluster import KMeans
import pandas as pd


def convert(root_input, root_output, word_count_path, one_hot_tresh):
    start = time.time()
    one_hot_encoder = OneHotGenerator()
    one_hot = one_hot_encoder.make_one_hot(word_count_path, one_hot_tresh)
    print("making_one_hot:{} sec".format(time.time() - start))
    start = time.time()
    dataset_reader = DatasetReader(root_input)
    file_names = dataset_reader.get_file_names()
    print("initializing loop:{} sec".format(time.time() - start))
    start = time.time()
    for column in ['TF', 'IDF', 'TFIDF']:
        all_df = pd.DataFrame(columns=["name", "vector"])
        for file_name in file_names:
            if file_name == "word_count.pkl":
                continue
            person_tfidf = dataset_reader.read_pkl_file(file_name)
            merged = person_tfidf.merge(one_hot, how="inner", on=['word'])
            # print(len(person_tfidf))
            # print(len(merged))
            # print(len(subtracted))
            # print("inner size: ")
            merged['one_hot'] = merged.apply(lambda row: np.array(row[6:]) * row[column], axis=1)
            # print(merged[merged['word'] == "سلام"]['word', 'TF'])
            # x = np.where(merged[merged['word'] == "سلام"]['one_hot'].values[0] != 0.0)
            # print(merged[merged['word'] == "سلام"]['one_hot'].values[0][x])
            # todo: check unknown
            subtracted = person_tfidf[~person_tfidf['word'].isin(merged['word'])]
            unknown_TF = subtracted['TF'].sum(axis=0)

            unknown_vector = one_hot_encoder.get_one_hot_vector("unknown_words") * unknown_TF
            word_vector = merged[['word', 'one_hot']]
            word_vector = word_vector.append({'word': "unknown_words", 'one_hot': unknown_vector}, ignore_index=True)
            word_vector['one_hot'].sum()
            final_vector = word_vector['one_hot'].sum()
            all_df = all_df.append({"name": file_name.split(".")[0], "vector": final_vector}, ignore_index=True)
            print(all_df)
            print("time taked for {}:{} sec".format(file_name, time.time() - start))
            start = time.time()
        path = root_output
        if not os.path.exists(path):
            os.makedirs(path)
        all_df.to_pickle("{}/{}.pkl".format(path, column))
        # print(word_vector['one_hot'].sum())
        # print(one_hot[one_hot["word"] == "unknown_words"])
        # break
        # print(subtracted[['word', 'count_x']].describe())
        # print("left inner size: ")
        # print(merged2.describe())

    def convert_v2(root_input, root_output, word_count_path, one_hot_tresh):
        start = time.time()
        one_hot_encoder = OneHotGenerator()
        one_hot = one_hot_encoder.make_one_hot(word_count_path, one_hot_tresh)
        print("making_one_hot:{} sec".format(time.time() - start))
        start = time.time()
        dataset_reader = DatasetReader(root_input)
        file_names = dataset_reader.get_file_names()
        print("initializing loop:{} sec".format(time.time() - start))
        start = time.time()
        for column in ['TF', 'IDF', 'TFIDF']:
            all_df = pd.DataFrame(columns=["name"] + list(one_hot.columns[2:]))
            for file_name in file_names:
                if file_name == "word_count.pkl":
                    continue
                person_tfidf = dataset_reader.read_pkl_file(file_name)
                merged = person_tfidf.merge(one_hot, how="inner", on=['word'])
                # print(len(person_tfidf))
                # print(len(merged))
                # print(len(subtracted))
                # print("inner size: ")
                merged['one_hot'] = merged.apply(lambda row: np.array(row[6:]) * row[column], axis=1)
                # print(merged[merged['word'] == "سلام"]['word', 'TF'])
                # x = np.where(merged[merged['word'] == "سلام"]['one_hot'].values[0] != 0.0)
                # print(merged[merged['word'] == "سلام"]['one_hot'].values[0][x])
                # todo: check unknown
                subtracted = person_tfidf[~person_tfidf['word'].isin(merged['word'])]
                unknown_TF = subtracted['TF'].sum(axis=0)
                unknown_vector = one_hot_encoder.get_one_hot_vector_v2("unknown_words") * unknown_TF


if __name__ == "__main__":
    w_c_path = "../tfidf/bow1/G_remove_unrelated/word_count.pkl"
    o_h_tresh = 200
    r_input = "../tfidf/bow1/G_remove_unrelated"
    r_output = "../one_hots"
    convert(r_input, r_output, w_c_path, o_h_tresh)
