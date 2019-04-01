import os
import pandas as pd


class DatasetReader:
    def __init__(self, root_path):
        self.root_path = root_path

    def set_root_path(self, root_path):
        self.root_path = root_path

    def get_file_names(self):
        return os.listdir(self.root_path)

    def __get_file(self, file_name, pandas=False, header=None):
        # data = pd.read_csv(self.root_path+"/"+file_name, sep=" ", header=None)
        # return data
        if header is None:
            header = ["word", "count"]
        path = self.root_path + "/" + file_name
        if not pandas:
            return open(path, "r", encoding="utf8")
        else:
            return pd.read_csv(path, error_bad_lines=False, engine="python", encoding="utf8", names=header)

    def read_file(self, file_name, double_enter=True):
        raw_file = self.__get_file(file_name)
        if double_enter:
            return ("".join(raw_file.readlines())).split("\n\n")
        else:
            return raw_file.readlines()

    def read_csv_file(self, file_name):
        raw_file = self.__get_file(file_name, True)
        return raw_file

    def read_pkl_file(self, file_name):
        raw_file = pd.read_pickle(self.root_path + "/" + file_name)
        return raw_file


if __name__ == "__main__":
    x = DatasetReader("../bows")
    mehdi = x.read_csv_file(x.get_file_names()[0])
    print(mehdi)
