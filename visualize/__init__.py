from preprocess import DatasetReader
from visualize.WordCountGenerator import WordCountGenerator

if __name__ == "__main__":
    dataset_reader = DatasetReader("../tfidf")
    # name = [0]
    value = 100

    for name in dataset_reader.get_file_names():
        name_file = dataset_reader.read_pkl_file(name)
        items = ["count", "TF", "IDF", "TFIDF"]
        word_count_generator = WordCountGenerator()
        word_count_generator.generate_full_chart(name, name_file, items, value)
