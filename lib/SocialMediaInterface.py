import tweepy

class SocialMediaInterface:

    def get_twittes(self):
        consumer_key = 'your_consumer_key'
        consumer_secret = 'your_consumer_secret'
        access_token = 'your_access_token'
        access_token_secret = 'your_access_token_secret'

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)

        query = 'python'
        max_tweets = 100

        tweets = tweepy.Cursor(api.search, q=query).items(max_tweets)

        for tweet in tweets:
            print(tweet.text)

