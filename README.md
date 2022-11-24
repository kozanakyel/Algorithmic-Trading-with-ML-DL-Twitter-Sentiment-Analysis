# Algorithmic-Trading-with-ML-DL-Twitter-Sentiment-Analysis
This is my project. That is an Algoritmic Trading Bot at CryptoCurrencies and Analysis for Financial Data Science. Additionally it includes Twitter Sentiment analysis and functionalities. The other side i add XGboost, LightGBM, DecisitonTree, Random Walk strategies and also LSTM modelling..

Example: Bitcoin sentiment analysis with 2 million tweets from 2022-10 and 2022-11
![Bitcoin Sentiment Analysis](/KZ_project_setup//assets/images/btc_twitter_sentimen.png)

The aim of this project is to price prediction (Cryptocurrencies, Bitcoin, and National Exchange platforms like BIST) any asset on exchanges with machine learning and deep learning methods especially trending methods recently used like the Xgboost, LigthGBM, LSTM etc., whether the price predictions of the products in the stock markets and the next day or the candle structure will increase or decrease. For this purposes, a sequence of steps and a machine learning workflow structure that will be applied sequentially will be followed. First of all, data pre-processing will be done. We will use tradingview api, binance api, yahoo finance api, ctxc api etc. Many API structures will be examined with various trials. Afterwards, studies will be carried out with technical analysis libraries under the python language for technical analysis and creation of new features. After the necessary indicators and features are determined, technical analysis strategies that give good results in the finance market will be labelled. One of the desired studies is to add Japanese candlestick recognition to these features. With the created data pipeline, the necessary data frames for both deep learning modelling and technical analysis and determining strategies with high profitability will be automatically created and easy to use with the help of pandas library.

INNOVATION: Always ask myself why and when all the people say buy coin but then price decrease, Sell the coin then price UP.
So i innovate a new Indicator with combination 23 indicators and also some strategies most popular. then all this indicators converted to binary matrix. at the last step i sum up all rows for obtain some knowledge about them. I named it the KZ_INDEX/SCORE.
This indicator shows the all the indicators says strong buy signal and the bottom point say that all the indicators stromg sell. and you can see actually this 2 things works opposite direction. and you can define buy/sell points. but you cannot implement esaily this indicator because it has very complex calculation.
![KZ_INDEX/SCORE](/KZ_project_setup//assets/images/kz_index.png)

Twitter and telegram APIs will be purchased for natural language process operations, and the related data will be provided with data mining and its APIs, and the effect of new features and people's thoughts and sentiments on this subject on the price will be monitored. With the process to be added to the data pipeline, the optimization and effects of the model will be observed. The results obtained in the last stage will be evaluated as both technical, deep learning and sentimental analysis, and it will be tried to determine where the price can go in the next candle. It seems like a topic that has been mentioned in many places, but when you enter it, it will be noticed how small the visible part of the iceberg is. My purpose in choosing this subject, which has been talked about so much and information pollution is at a high level. It comes from my curiosity to determine how price algorithms move in scientific ways.