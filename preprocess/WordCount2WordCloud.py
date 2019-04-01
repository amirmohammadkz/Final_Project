from persian_wordcloud.wordcloud import PersianWordCloud, add_stop_words
# import langdetect


def create_word_cloud(x="result.png"):
    f = open("word_repeat_word_cloud", encoding="utf8")
    text = f.read()

    # stopwords = add_stop_words(['نیست'])
    # stopwords = add_stop_words(['هست'])
    # stopwords = add_stop_words(['می‌کنیم'])
    # stopwords = add_stop_words(['کردند'])
    # stopwords = add_stop_words(['کنید'])
    # stopwords = add_stop_words(['می‌کنند'])
    # stopwords = add_stop_words(['کردم'])
    # stopwords = add_stop_words(['کردیم'])
    # stopwords = add_stop_words(['داریم'])
    # stopwords = add_stop_words(['کرده'])
    # stopwords = add_stop_words(['کرد'])
    # stopwords = add_stop_words(['می‌کند'])
    # stopwords = add_stop_words(['می‌کنم'])
    # stopwords = add_stop_words(['هستیم'])
    # stopwords = add_stop_words(['کردید'])
    # stopwords = add_stop_words(['کنیم'])
    # stopwords = add_stop_words(['کنند'])
    # stopwords = add_stop_words(['باشیم'])
    # stopwords = add_stop_words(['کند'])
    # stopwords = add_stop_words(['کند'])
    # stopwords = add_stop_words(['می‌شود'])
    # stopwords = add_stop_words(['می‌شویم'])
    # stopwords = add_stop_words(['می‌شوید'])
    # stopwords = add_stop_words(['اینها'])
    # Generate a word cloud image
    wordcloud = PersianWordCloud(
        only_persian=True,
        max_words=300,
        margin=0,
        width=1000,
        height=1000,
        min_font_size=1,
        collocations=False,
        max_font_size=500,
        # stopwords=stopwords,
        background_color="black"
    ).generate(text)
    # Display the generated image:
    image = wordcloud.to_image()
    image.show()
    image.save(x)
    f.close()


def saveWordRepeatForWordCloud(sorted_list):
    bw = open("word_repeat_word_cloud", "w", encoding="utf8")
    for wordTuple in sorted_list:
        try:
            for i in range(wordTuple[1]):
                bw.write(wordTuple[0] + "\n")
        except Exception:
            print(wordTuple)
    bw.close()


if __name__ == "__main__":
    word_count = open("../word_count", "r", encoding="utf8").readlines()
    cleaned_word_count = []
    lines = len(word_count)
    for index, line in enumerate(word_count):
        if index % 100 == 0:
            print(index * 100 / lines)

        word = line.split(",")[0]
        count = int(line.split(",")[1])
        try:
            # langdetect.detect(word)
            cleaned_word_count.append((word, count))
            # if langdetect.detect(word) in ("fa","ar"):
            # else:
            #     print(word, langdetect.detect(word))
        except Exception as e:
            print(e)
            print(word)

    # word_count = [(line.split(",")[0], int(line.split(",")[1])) for line in word_count if
    #               langdetect.detect(line.split(",")[0] == "fa")]
    # saveWordRepeatForWordCloud(cleaned_word_count)
    create_word_cloud()
