import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from preprocess.BowMaker import BowMaker
from preprocess.dataset_reader import DatasetReader
from preprocess.preprocessor import Preprocessor

if __name__ == "__main__":
    grams = 3
    dataset_reader = DatasetReader("../datasets")
    print("dataset read")
    for name in dataset_reader.get_file_names():
        print(name + " tweets...")
        tweets = dataset_reader.read_file(name)
        print("some tweets:")
        print(tweets[:2])
        bowMaker = BowMaker()
        for tweet in tweets:
            tokenized = Preprocessor(tweet).get_cleaned_tweet().get("tokenized")
            if grams > 1:
                tokenized = [" ".join(tokenized[i:i + grams]) for i in range(len(tokenized) - grams + 1)]
            # print(tokenized)
            bowMaker.add_tweet(tokenized)
        print("generating bow...")
        bowMaker.remove_extra_words()
        bow = bowMaker.get_bow()
        bow_file = open("../bows3/" + name, "w", encoding="utf8")
        print("saving bow...")
        for key in bow.keys():
            try:
                if "," in key:
                    print("comma key:" + key)
                else:
                    bow_file.write(key + "," + str(bow[key]) + "\n")
            except Exception as e:
                print(e)
                print(key)
                print(bow[key])
                print("#####")
        bow_file.close()
