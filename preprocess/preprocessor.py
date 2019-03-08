from hazm import *

from preprocess.dataset_reader import DatasetReader


class Preprocessor:
    def __init__(self, raw_tweet):
        self.raw_tweet = raw_tweet

    def get_cleaned_tweet(self):
        normalizer = Normalizer()
        normalized = normalizer.normalize(self.raw_tweet)
        tokenized = word_tokenize(normalized)
        stemmer = Stemmer()
        stemmed = [stemmer.stem(word) for word in tokenized]
        lemmatizer = Lemmatizer()
        lemmatized = [lemmatizer.lemmatize(word) for word in stemmed]
        return {"lemmatized": lemmatized, "stemmed": stemmed, "tokenized": tokenized, "normalized": normalized}


if __name__ == "__main__":
    dataset_reader = DatasetReader("../datasets")
    mehdi = dataset_reader.read_file(dataset_reader.get_file_names()[0])
    tweet = mehdi[0]

    preprocessor = Preprocessor(tweet)
    cleaned = preprocessor.get_cleaned_tweet()
    print("original")
    print(tweet)
    print("##########")

    for key in cleaned.keys():
        print(key)
        print(cleaned[key])
        print("##########")