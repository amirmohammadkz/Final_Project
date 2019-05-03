
import tweepy
import time
from preprocess.dataset_reader import DatasetReader


def gat_tweets():
    usernames = ['mhdi_gh01', 'e_aliakbar', 'domesoldosol', 'newsha_s3', 'DontStayTooFar', 'SaDeGhTb', 'Zeinaaab_hm',
                 'hvmoolfa', 'bardia_heydari', 'miladibra10', 'ho3ein_khalili', 'SepehrHerasat', 'clonerrr', 'AliAbdolahii',
                 'Ahmad__kani', 'sarsanaee', 'amirhossein___a', 'salarn14' , 'Pooya448','erfanafre', 'fatemev3q', 'MrAlihoseiny',
                 'nabykhany']

    consumer_key='ShhlxIxled7fNgAL2jZNH2dhp'
    consumer_secret='w7oT2RYszrKo3FpZNG9UZaIMqwQW5yRYgt9EGrqb1qREE7auJZ'
    access_token_key='942100765925142529-rr8BOrtV0uFBniSXHdN5PLRxDzgJfMl'
    access_token_secret='dRpe3zoSZydOgy81YohYZtEFdjKmse9Pk0fUuo2Y0V37m'


    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)

    api = tweepy.API(auth)

    i = 0

    for username in usernames:
        filename = '../datasets_V2/'+ username +'.txt'
        print(username)
        file = open(filename,'w')
        tweets = tweepy.Cursor(api.user_timeline, screen_name = username, count = 3000, include_rts = True, tweet_mode="extended").items()

        for tweet in tweets:
            #print tweet
            tweet = tweet._json
            txt = tweet['full_text'].encode('utf-8')
            if txt[:2] != 'RT' and tweet['lang'] != 'en' :
                file.write(txt)
                file.write('\n\n')
                i += 1

    print(i)


def data_randon_patitioning(dataset_reader, root_path):
    if root_path is not None:
        dataset_reader.set_root_path(root_path)
    file_names = dataset_reader.get_file_names()

    for file_name in file_names:
        file = []
        tweets = dataset_reader.read_file(file_name)
        for j in range(0,int(len(tweets)/200)+1):
            dist_file_name = '../little_datasets/' +file_name + '_' + str(j) + '.txt'
            file.append(open(dist_file_name,'w'))
        print(file_name, ' : ' ,len(file))
        for i in range(len(tweets)):
            for j in range(0,int(len(tweets)/200)+1):
                file[j].write(tweets[i])
                i+=1
                if i >= len(tweets):
                    break


if __name__ == "__main__":
    #gat_tweets()
    dataset_reader = DatasetReader("../datasets_V2")
    data_randon_patitioning(dataset_reader, "../datasets_V2")


