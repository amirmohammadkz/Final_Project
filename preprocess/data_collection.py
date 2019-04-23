
import tweepy
import time

usernames = ['mhdi_gh01', 'e_aliakbar', 'domesoldosol', 'newsha_s3', 'DontStayTooFar', 'SaDeGhTb', 'Zeinaaab_hm',
             'hvmoolfa', 'bardia_heydari', 'miladibra10', 'ho3ein_khalili', 'SepehrHerasat', 'clonerrr', 'AliAbdolahii',
             'Ahmad__kani', 'sarsanaee', 'amirhossein___a', 'salarn14' , 'Pooya448','erfanafre', 'fatemev3q', 'MrAlihoseiny',
             'nabykhany']

'''

old_usernames = ['mhdi_gh01', 'e_aliakbar', 'domesoldosol', 'newsha_s3', 'DontStayTooFar', 'SaDeGhTb', 'Zeinaaab_hm',
             'hvmoolfa', 'bardia_heydari', 'miladibra10', 'ho3ein_khalili', 'SepehrHerasat', 'clonerrr']

'''

consumer_key='ShhlxIxled7fNgAL2jZNH2dhp'
consumer_secret='w7oT2RYszrKo3FpZNG9UZaIMqwQW5yRYgt9EGrqb1qREE7auJZ'
access_token_key='942100765925142529-rr8BOrtV0uFBniSXHdN5PLRxDzgJfMl'
access_token_secret='dRpe3zoSZydOgy81YohYZtEFdjKmse9Pk0fUuo2Y0V37m'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

api = tweepy.API(auth)

i = 0
'''
user_count = 0
dic = {}
for username in usernames:
    for follower in tweepy.Cursor(api.followers, screen_name = usernames).items():
        user_count += 1
        print dic
        if follower not in usernames:
            if follower.screen_name in dic:
                dic[follower.screen_name] += 1
            else:
                dic[follower.screen_name] = 1

        if user_count >= 279:
            user_count = 0
            time.sleep(60*15)

for key,value in dic.items():
    if value > 2 :
        print key
        usernames.append(key)

'''
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