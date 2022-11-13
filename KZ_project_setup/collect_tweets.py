from twitter.twitter_collection import TwitterCollection


if __name__ == '__main__':

    client = TwitterCollection()

    query_list = ['btc','eth','xrp','bnb', 'matic', 'sol', 'ens']
    query_list_bist = ['sumas', 'orma', 'xu100', 'bist', 'sasa']

    for i in query_list:
        df_tweets = client.get_tweets_with_interval(i, 'en', hour=24*4)
        print(f'shape of {i} tweets df: {df_tweets.shape}')
        path_df = f'./KZ_project_setup/data/tweets_data/{i}/'
        file_df = f'{i}_tweets.csv'
        client.write_tweets_csv(df_tweets, path_df, file_df)
        client.throw_unnamed_cols(i, path_df, file_df)