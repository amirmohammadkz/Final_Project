import math

from sklearn.feature_extraction.text import TfidfVectorizer

from preprocess import DatasetReader


class TF_IDF:

    def __init__(self, bow_list):
        self.bow_list = bow_list

    def add_TF(self):
        for bow in self.bow_list:
            bow['TF'] = (bow['count'] + 0.0) / bow['count'].sum()

    def add_IDF(self):
        word_list = [word for bow in self.bow_list for word in bow['word']]
        word_set = set(word_list)
        print(len(word_set))
        word_accours = {}
        for word in word_set:
            count = 0
            for bow in self.bow_list:
                if word in bow['word'].values:
                    count += 1
            word_accours[word] = count
        for bow in self.bow_list:
            bow['IDF'] = bow.apply(lambda row: math.log((len(self.bow_list) / word_accours[row.word])), axis=1)

    def add_TFIDF(self):
        for bow in self.bow_list:
            bow['TFIDF'] = bow['TF'] * bow['IDF']

    def get_bow_list(self):
        return self.bow_list


if __name__ == "__main__":
    dataset_reader = DatasetReader("../bows3")
    print(dataset_reader.get_file_names())
    tf_idf = TF_IDF([dataset_reader.read_csv_file(df) for df in dataset_reader.get_file_names()])
    tf_idf.add_TF()
    print(tf_idf.get_bow_list()[0].sort_values(by=['count'], ascending=False).iloc[0:5])
    tf_idf.add_IDF()
    tf_idf.add_TFIDF()
    print(tf_idf.get_bow_list()[0])
    for index, bow in enumerate(tf_idf.get_bow_list()):
        bow.to_pickle("../tfidf3/" + dataset_reader.get_file_names()[index] + ".pkl")

#
# f = open("word_repeat_word_cloud", encoding="utf8")
# text = f.read()
# print(text)
#
# corpus = ['سلام سلام سلام', 'This document is the second document.', 'And this is the third one.',
#           'Is this the first document?', text]
# vectorizer = TfidfVectorizer()
# X = vectorizer.fit_transform(corpus)
# print(vectorizer.get_feature_names())
# print(X.shape)
# print(X)
