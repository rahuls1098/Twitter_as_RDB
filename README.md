## Overview 
Twitter started out with a MySQL backend. In this project, I tested the speed of posting 1,000,000 tweets and the rate at which timelines
are retrieved using a relational database. The latter simulates a user opening the Twitter app and refreshing their timeline to see new posts. I created a driver program that carries out the performance testing, and an API which implements the Twitter-related functionality (post/retrieve timeline). 
The implementation of the API is abstracted from the driver program such that the performance testing can be redone (without changing the driver code) with Redis, a key-value store database. See Twitter_as_KeyValue for comparison.


## Setup and Configuration
- Ensure that MySQL is installed and running.
- Import the twitter_rdb_dump.sql file into MySQL to set up the database schema.
- Install required Python packages: yaml, pandas, mysql-connector-python, tqdm.
- Configure database credentials in config/settings.yaml (not provided in the files).
- Load the data in follows.csv into the FOLLOWS table using MySQLWorkbench.
  
## Usage
- Run TwitterDriverMain.py to start performance tests
  - Post tweets will output the rate at which 1,000,000 tweets from tweets.csv are uploaded to the database.
  - Get home timeline will repeatedely pick a random user and return that user's home timeline (10 most recent tweets posted by that user's followers), and output the API calls/sec.
 
## Results
- postTweet: 1454.2 API calls/sec
- getHomeTimeline: 527 API calls/sec
