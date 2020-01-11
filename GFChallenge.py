import tweepy
import numpy as np

def shuffle(_arr, _times):
    for _ in range(_times):
        np.random.shuffle(_arr)
    return _arr[0]

def post(_sentence):
    consumer_key = 'YOUR-CONSUMER-KEY'
    consumer_secret = 'YOUR-CONSUMER-SECRET'
    access_token_key = 'YOUR-ACCESS-TOKEN'
    access_token_secret = 'YOUR-ACCESS-TOKEN-SECRET'

    auth_ = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth_.set_access_token(access_token_key, access_token_secret)
    api = tweepy.API(auth_)

    api.update_status(status = _sentence)


def main():
    connector = ["も", "は", "のところは", "こそ"]
    end = ["た", "ていた", "なかった", "た気がした", "る気がした"]

    sentence = "今日" + shuffle(connector, 5) + "彼女ができ" + shuffle(end, 4)

    print(sentence)
    post(sentence)



if __name__ == "__main__":
    main()
