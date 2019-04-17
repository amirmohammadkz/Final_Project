import numpy as np


class OneHotGenerator:
    def __init__(self, source):
        self.oneHotList = []
        self.source = source

    def make_one_hot(self, min_count=2):
        self.oneHotList.append("unknown_words")
        file = open(self.source, "r", encoding="utf8")
        for line in file.readlines():
            try:
                word = line.split(",")[0]
                count = int(line.split(",")[1])
                if count >= min_count:
                    self.oneHotList.append(word)
            except Exception as e:
                print(e)
                print(line)
        return self.oneHotList

    def get_one_hot(self, word):
        if word in self.oneHotList:
            return np.eye(len(self.oneHotList))[self.oneHotList.index(word)]
        else:
            return np.eye(len(self.oneHotList))[0]


if __name__ == "__main__":
    oneHotGenerator = OneHotGenerator("../word_count")
    x = oneHotGenerator.make_one_hot()
    print(oneHotGenerator.get_one_hot("سلام"))
    print(oneHotGenerator.get_one_hot("بستن"))
    print(oneHotGenerator.get_one_hot("شیشسیشسیشسیشسیسش"))
