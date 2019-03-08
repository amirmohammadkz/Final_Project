import os
import pandas as pd


class DatasetReader:
    def __init__(self, root_path):
        self.root_path = root_path

    def get_file_names(self):
        return os.listdir(self.root_path)

    def __get_file(self, file_name):
        # data = pd.read_csv(self.root_path+"/"+file_name, sep=" ", header=None)
        # return data
        return open(self.root_path + "/" + file_name, "r", encoding="utf8")

    def read_file(self, file_name):
        raw_file = self.__get_file(file_name)
        return ("".join(raw_file.readlines())).split("\n\n")


if __name__ == "__main__":
    x = DatasetReader("../datasets")
    mehdi = x.read_file(x.get_file_names()[0])