import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from preprocess.BowMaker import BowMaker
from preprocess.dataset_reader import DatasetReader
from preprocess.preprocessor import Preprocessor

if __name__ == "__main__":
    dataset_reader = DatasetReader("../datasets")
    print("dataset read")
    for name in dataset_reader.get_file_names():
        print(name + " tweets...")
        tweets = dataset_reader.read_file(name)
        bowMaker = BowMaker()
        for tweet in tweets:
            stemmed = Preprocessor(tweet).get_cleaned_tweet().get("stemmed")
            bowMaker.add_tweet(stemmed)
        print("generating bow...")
        bow = bowMaker.get_bow()
        bow_file = open("../bows/" + name, "w", encoding="utf8")
        print("saving bow...")
        for key in bow.keys():
            try:
                bow_file.write(key + "," + str(bow[key]) + "\n")
            except Exception as e:
                print(e)
                print(key)
                print(bow[key])
                print("#####")
        bow_file.close()
