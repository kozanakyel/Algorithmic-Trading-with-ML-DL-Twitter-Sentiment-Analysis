from twitter.twitter_collection import TwitterCollection


if __name__ == '__main__':

    client = TwitterCollection()

    query_list = ['btc','eth','xrp','bnb', 'ens']
    query_list_bist = ['sumas', 'orma', 'xu100', 'bist', 'sasa']
    test_query = ['agyo', 'sngyo']

    
    for i in query_list_bist[:3]:
        df_tweets = client.get_tweets_with_interval(i, 'tr', hour=24*7, interval=4)
        print(f'shape of {i} tweets df: {df_tweets.shape}')
        path_df = f'./KZ_project_setup/data/tweets_data/{i}/'
        file_df = f'{i}_tweets.csv'
        client.write_tweets_csv(df_tweets, path_df, file_df)
    
    
  