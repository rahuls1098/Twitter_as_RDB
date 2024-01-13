from TwitterMysql import TwitterMysql
import pandas as pd
import time
from tqdm import tqdm
from random import randint

# Performance testing

if __name__ == "__main__":

    # Import tweets from data directory
    tweet_table = pd.read_csv(r"./data/tweet.csv")

    # Instantiate a TwitterMysql object
    twitter = TwitterMysql()

    # Post all tweets and check the number of tweets inserted per second
    def postAllTweets():

        # Get starting time of tweet insertions
        start_time_posts = time.time()

        # Iterate through the rows of the tweets.csv table
        for row in tqdm(tweet_table.iterrows()):
            user_id = row[1][0]
            tweet_text = row[1][1]

            # API call
            twitter.postTweet(user_id, tweet_text)

        # Calculate total time
        total_time = time.time() - start_time_posts

        # Calculate tweets per second
        tweets_per_sec = tweet_table.shape[0]/total_time

        print("Total time: %.2f seconds" % total_time)
        print("Tweets/sec: %.1f" % tweets_per_sec)

    # Repeatedly get timelines (10 most recent tweets - implemented in SQL procedure) of randomly selected users
    def getRandomTimelines():

        # Get the max number of users to limit random number generator
        max_users = tweet_table.sort_values(by="USER_ID", ascending=False, ignore_index=True)["USER_ID"][0]

        start_time = time.time()

        timelines_retrieved = 0

        # Run timeline retrieval for 1 minute
        while((time.time() - start_time) < 60):
            # Select random user ID
            user_id = randint(0, max_users)
            print("Retrieving timeline for user_id: " + str(user_id) + "\n")

            # API call
            twitter.getTimeline(user_id)
            timelines_retrieved += 1

        # Compute timelines retrieved per second
        total_time = time.time() - start_time

        timelines_per_sec = timelines_retrieved / total_time
        print("\nTotal time spent retrieving timelines: %.2f seconds" % total_time)
        print("Timelines/sec: %.1f" % timelines_per_sec)


    # Execute post all tweets function
    postAllTweets()

    # Repeatedly pick a random user and return user's home timeline (10 most recent tweets of their followers)
    # for 60 seconds
    getRandomTimelines()






