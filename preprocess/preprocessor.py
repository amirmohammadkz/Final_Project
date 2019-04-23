from hazm import *

from preprocess.dataset_reader import DatasetReader


class Preprocessor:
    def __init__(self):
        self.normalizer = Normalizer()
        self.stemmer = Stemmer()
        self.tokenizer = WordTokenizer()

    def get_cleaned_tweet(self, raw_tweet):
        normalizer = Normalizer()
        normalized = normalizer.normalize(raw_tweet)
        stemmer = Stemmer()
        stemmed = stemmer.stem(normalized)
        # stemmed = [stemmer.stem(word) for word in normalized]
        # stemmed = stemmed.replace(".", "")
        # stemmed = stemmed.replace("؟", "")
        # stemmed = stemmed.replace("!", "")
        # stemmed = stemmed.replace("\"", "")
        # stemmed = stemmed.replace("؛", "")
        # stemmed = stemmed.replace(":", "")
        tokenized = word_tokenize(stemmed)
        # lemmatizer = Lemmatizer()
        # lemmatized = [lemmatizer.lemmatize(word) for word in tokenized]
        lemmatized = []
        return {"lemmatized": lemmatized, "stemmed": stemmed, "tokenized": tokenized, "normalized": normalized}

    def clean_tweet(self, raw_tweet, normalize=True, stem=True, remove_punc=True, tokenize=True, remove_rabt=True,
                    remove_extra=True, remove_unrelated=True):
        process = []
        tweet = raw_tweet
        process.append(tweet)
        if normalize:
            tweet = self.normalizer.normalize(raw_tweet)
            process.append(tweet)
        if stem:
            tweet = self.stemmer.stem(tweet)
            process.append(tweet)
        if remove_punc:
            tweet = tweet.replace(".", "")
            tweet = tweet.replace("؟", "")
            tweet = tweet.replace("!", "")
            tweet = tweet.replace("\"", "")
            tweet = tweet.replace("؛", "")
            tweet = tweet.replace(":", "")
            tweet = tweet.replace(",", " ")
            process.append(tweet)
        if tokenize:
            process = [self.tokenizer.tokenize(text) for text in process]
        if remove_rabt:
            process.append(self.remove_rabt(process[-1]))
        if remove_extra:
            process.append(self.remove_ezafe(process[-1]))
        if remove_unrelated:
            process.append(self.remove_unrelated(process[-1]))

        x = all([process[0] == process])
        if process[0] != process[1]:
            print(process[0])
            print(process[1])
        return process

    def remove_rabt(self, word_list):
        return [word for word in word_list if
                word not in ["باری", "ولی", "هم", "نیز", "لیکن", "که", "زیرا", "خواه", "پس", "اما", "تا",
                             "چه",
                             "چون", "نه", "اگر", "پس", "یا", "و"]]

    def remove_ezafe(self, word_list):
        return [word for word in word_list if
                word not in [" ", "نیز", "در", "با", "ترین", "تر", "برای", "از", "به", "را", "رو"]]

    def remove_unrelated(self, word_list):
        final = []
        for word in word_list:
            add = True
            if word[:4] == "http":
                add = False
            if word[0] == "@":
                add = False
            try:
                if float(word) > 10:
                    add = False
            except ValueError:
                pass
            if add:
                final.append(word)
        return final
        # words = [word for word in word_list if
        #          not (word[:4] == "http" or word[0] == "@")
        #          ]
        # tmp = [word for word in words if word.isdigit()]
        # print(tmp)
        # return words


if __name__ == "__main__":
    dataset_reader = DatasetReader("../datasets")
    mehdi = dataset_reader.read_file(dataset_reader.get_file_names()[0])
    tweet = mehdi[1]

    preprocessor = Preprocessor(tweet)
    cleaned = preprocessor.clean_tweet()
    print("cleaned")
    print(cleaned)
    print("##########")

    for key in cleaned:
        print(key)
        print("##########")
    # print(Stemmer().stem(word=" باید گیفش رو ساخت تا تو مواقع لازم استفاده کردی"))
