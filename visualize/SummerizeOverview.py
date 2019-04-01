from preprocess import DatasetReader
import matplotlib.pyplot as plt


class Sumerizer:
    def __init__(self, dataset_reader: DatasetReader):
        self.dataset_reader = dataset_reader
        pass

    def generate_person_tweet_count_chart(self, root_path=None):
        if root_path is not None:
            self.dataset_reader.set_root_path(root_path)
        file_names = self.dataset_reader.get_file_names()
        dic = {}
        for file_name in file_names:
            dic[file_name] = len(self.dataset_reader.read_file(file_name))
        plt.bar()
        return True

    def generate_mean_tweet_words_count_chart(self):
        pass

    def generate_unique_words_count_chart(self):
        pass


if __name__ == "__main__":
    summerizer = Sumerizer(DatasetReader("../datasets"))
    summerizer.generate_person_tweet_count_chart()
