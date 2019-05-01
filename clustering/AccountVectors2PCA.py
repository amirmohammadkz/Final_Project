import os

from sklearn.manifold import TSNE

from clustering.OneHotEncoder import OneHotGenerator
from preprocess.dataset_reader import DatasetReader
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA, TruncatedSVD
import matplotlib.cm as cm


def convert(root_input, root_output):
    dataset_reader = DatasetReader(root_input)
    all_names = dataset_reader.get_file_names()
    for file_name in all_names:
        data = dataset_reader.read_pkl_file(file_name)
        array = None
        for index, row in data.iterrows():
            # print(row['vector'])
            if array is None:
                array = np.array([row['vector']])
            else:
                array = np.append(array, [row['vector']], axis=0)
        print(array)
        print(array.shape)
        df = pd.DataFrame(array)
        # print(df)
        x = StandardScaler().fit_transform(df)
        x = array
        print(x.shape)
        # print(x)

        pca = TruncatedSVD(n_components=2)

        principalComponents = pca.fit_transform(x)
        print(pca.explained_variance_ratio_)
        principalDf = pd.DataFrame(data=principalComponents
                                   , columns=['principal component {}'.format(i + 1) for i in
                                              range(principalComponents.shape[1])])

        finalDF = pd.concat([data['name'], principalDf], axis=1)
        path = root_output
        if path is not None:
            if not os.path.exists(path):
                os.makedirs(path)
            pd.to_pickle(finalDF, "{}/{}.pkl".format(path, file_name.split(".")[0]))

        # todo: visualization...(another file has already created)
        # print(finalDF)
        # fig = plt.figure(figsize=(8, 8))
        # ax = fig.add_subplot(1, 1, 1)
        # ax.set_xlabel('Principal Component 1', fontsize=15)
        # ax.set_ylabel('Principal Component 2', fontsize=15)
        # ax.set_title('2 component TruncatedSVD for {} of words'.format(file_name.split(".")[0]), fontsize=20)
        # targets = np.array(finalDF['name'])
        # # colors = ['r', 'g', 'b', 'r', 'g', 'b', 'r', 'g', 'b', 'r', 'g', 'b', 'b']
        # colors = cm.rainbow(np.linspace(0, 1, len(targets)))
        # # for i in finalDF['principal component 1']:
        # # print(i)
        # for target, pc1, pc2, color in zip(targets, finalDF['principal component 1'],
        #                                    finalDF['principal component 2'], colors):
        #     ax.scatter(pc1, pc2, s=50, label=target, color=color)
        #     # print(finalDF)
        # ax.legend()
        # ax.grid()
        # # plt.show()
        # path = root_output
        # if path is None:
        #     plt.show()
        # else:
        #     if not os.path.exists(path):
        #         os.makedirs(path)
        #     plt.savefig("{}/{}.pkl".format(path, file_name.split(".")[0]))
        #     plt.clf()

        # todo: use these comments
        # x = [sum(pca.explained_variance_ratio_[:i]) for i in range(len(pca.explained_variance_ratio_))]
        # plt.title(file_name)
        # plt.plot(x)


if __name__ == "__main__":
    r_input = "../one_hots"
    r_output = "../generalDF/TruncatedSVD"
    # r_output = None
    convert(r_input, r_output)
    pass
