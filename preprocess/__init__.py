import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from preprocess.BowMaker import BowMaker
from preprocess.dataset_reader import DatasetReader
from preprocess.preprocessor import Preprocessor

if __name__ == "__main__":
    grams = [1, 2, 3]
    root_input = "../datasets"
    root_output = "../ngrams"
    # todo: reform options and utilize it
    options = ["A_original", "B_normalized", "C_stem", "D_remove_punc", "E_remove_rabt", "F_remove_extra",
               "G_remove_unrelated"]
    ###########################################

    dataset_reader = DatasetReader(root_input)
    preprocessor = Preprocessor()
    print("dataset read")
    for name in dataset_reader.get_file_names():
        print(name + " tweets...")
        tweets = dataset_reader.read_file(name)
        # print("some tweets:")
        # print(tweets[:2])
        bowMakers = {}
        for gram in grams:
            for level in options:
                bowMakers[(gram, level)] = BowMaker()
        for index, tweet in enumerate(tweets):
            process = preprocessor.clean_tweet(tweet)
            grams_tokenized = {}
            for gram in grams:
                for level, tokenized in enumerate(process):
                    # print(len(options))
                    bowMakers[(gram, options[level])].add_tweet(
                        [" ".join(tokenized[i:i + gram]) for i in range(len(tokenized) - gram + 1)])
        print("generating bow...")
        for key in bowMakers.keys():
            bowMaker = bowMakers[key]
            # bowMaker.remove_extra_words()
            bow = bowMaker.get_bow()
            directory = "../ngrams/bow" + str(key[0]) + "/" + key[1]
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
