from hazm import *

from preprocess.dataset_reader import DatasetReader


class Preprocessor:
    def __init__(self, raw_tweet):
        self.raw_tweet = raw_tweet

    def get_cleaned_tweet(self):
        normalizer = Normalizer()
        normalized = normalizer.normalize(self.raw_tweet)
        stemmer = Stemmer()
        stemmed = stemmer.stem(normalized)
        # stemmed = [stemmer.stem(word) for word in normalized]
        cleaned_stemmed = stemmed.replace(".", "")
        cleaned_stemmed = cleaned_stemmed.replace("؟", "")
        cleaned_stemmed = cleaned_stemmed.replace("!", "")
        # cleaned_stemmed = cleaned_stemmed.replace("؛", "")
        # cleaned_stemmed = cleaned_stemmed.replace(":", "")
        tokenized = word_tokenize(cleaned_stemmed)
        lemmatizer = Lemmatizer()
        lemmatized = [lemmatizer.lemmatize(word) for word in tokenized]
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
    print(Stemmer().stem(word=" باید گیفش رو ساخت تا تو مواقع لازم استفاده کردی"))
