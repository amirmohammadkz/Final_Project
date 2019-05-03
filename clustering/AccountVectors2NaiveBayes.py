from sklearn import naive_bayes

from preprocess.dataset_reader import DatasetReader
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import metrics


def convert(root_input):
    dataset_reader = DatasetReader(root_input)
    all_names = dataset_reader.get_file_names()

    classifier = naive_bayes.MultinomialNB()
    labels = []
    boys = ['mhdi_gh01', 'e_aliakbar', 'domesoldosol', 'SaDeGhTb',
            'hvbashiri', 'bardia_heydari', 'miladibra10', 'ho3ein_khalili', 'SepehrHerasat', 'clonerrr',
            'AliAbdolahii', 'Ahmad__kani', 'sarsanaee', 'amirhossein___a', 'salarn14', 'Pooya448',
            'erfanafre', 'MrAlihoseiny', 'nabykhany', 'shsadatipour', 'tawha33'
            ]
    girls = ['newsha_s3', 'DontStayTooFar', 'Zeinaaab_hm', 'fatemev3q', 'motevaari']

    for file_name in all_names:
        for k in range(4, 5):
            labels = []
            print(file_name, "#############################")
            data = dataset_reader.read_pkl_file(file_name)

            for name in data['name']:
                if name in boys:
                    labels.append(1)
                else:
                    labels.append(0)

            print(labels)
            train_x, valid_x, train_y, valid_y = train_test_split(np.vstack(data['vector'].values), labels,
                                                                  test_size=0.2, random_state=0)
            classifier.fit(train_x, train_y)
            predictions = classifier.predict(valid_x)
            print( metrics.accuracy_score(predictions, valid_y))

if __name__ == "__main__":
    r_input = "../one_hots"
    convert(r_input)
