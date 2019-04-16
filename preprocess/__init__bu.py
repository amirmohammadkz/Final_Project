import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from preprocess.BowMaker import BowMaker
from preprocess.dataset_reader import DatasetReader
from preprocess.preprocessor import Preprocessor

if __name__ == "__main__":
    grams = [1, 2, 3]
    root_input = "../datesets"
    root_output = "../ngrams"
    all_options = True
    options = ["normalize1", "stem2", "remove_punc3", "remove_rabt4", "remove_extra5"]
    ###########################################

    dataset_reader = DatasetReader(root_input)
    print("dataset read")
    for name in dataset_reader.get_file_names():
        print(name + " tweets...")
        tweets = dataset_reader.read_file(name)
        # print("some tweets:")
        # print(tweets[:2])
        bowMakers = {}
        for gram in grams:
            bowMakers[gram] = BowMaker()
        for index, tweet in enumerate(tweets):
            tokenized = Preprocessor(tweet).get_cleaned_tweet().get("tokenized")
            grams_tokenized = {}
            for gram in bowMakers.keys():
                bowMakers[gram].add_tweet([" ".join(tokenized[i:i + gram]) for i in range(len(tokenized) - gram + 1)])
        print("generating bow...")
        for gram in bowMakers.keys():
            bowMaker = bowMakers[gram]
            bowMaker.remove_extra_words()
            bow = bowMaker.get_bow()
            directory = "../ngrams/bow" + str(gram)
            if not os.path.exists(directory):
                os.makedirs(directory)
            bow_file = open(directory + "/" + name, "w", encoding="utf8")
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
