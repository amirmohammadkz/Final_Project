import hazm

from preprocess.dataset_reader import DatasetReader
from preprocess.preprocessor import Preprocessor


class BowMaker:
    def __init__(self):
        self.bow = {}

    def add_tweet(self, tweet):
        for word in tweet:
            if self.bow.get(word) is None:
                self.bow[word] = 1
            else:
                self.bow[word] += 1

    def get_bow(self):
        return self.bow


if __name__ == "__main__":
    dataset_reader = DatasetReader("../datasets")
    mehdi = dataset_reader.read_file(dataset_reader.get_file_names()[0])
    bowMaker = BowMaker()
    for tweet in mehdi:
        stemmed = Preprocessor(tweet).get_clean_tweet().get("stemmed")
        bowMaker.add_tweet(stemmed)
    bow = bowMaker.get_bow()
    print(bow)
