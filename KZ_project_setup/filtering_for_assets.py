import warnings
import pandas as pd
warnings.simplefilter(action = 'ignore', category = pd.errors.PerformanceWarning)
warnings.filterwarnings('ignore')


from strategy_kz.tradingviewstrategy import TradingViewStrategy
from strategy_kz.strategy_var import StrategyVar
from data_pipelines.data_manipulation import DataManipulation
from technical_analysis.backtest_kz import *

screener="turkey"
exchange="BIST"
path_symbol = './data/symbol_data/ana_market.csv'
index = 'Order'
#screener="crypto"
#exchange="BINANCE"
#path_symbol = './data/symbol_data/usdtcoins.csv'
#index = 'Order'

SYMBOL = ''
scale = 1
range_list = [5, 8, 10, 15, 20, 25]
range_list = [i*scale for i in range_list]
period = '3mo'
interval = '1h'
start_date = ''
end_data = ''
source = 'yahoo'

if __name__ == '__main__':

    st_main_market = TradingViewStrategy(exchange, screener, path_symbol)
    filter_list = st_main_market.get_st_result_list('1h')

    filtre = []
    if screener == 'crypto':
        for i in filter_list:
            r = i[-4:]
            r = f'{i[:-4]}-{r[:-1]}'
            filtre.append(r)
        print(len(filter_list))
    elif screener == 'turkey':
        for i in filter_list:
            filtre.append(f'{i}.IS')
        print(len(filter_list))

    df_filter_list = []
    for i in filtre:
        SYMBOL = f'{i}'
        data = DataManipulation(SYMBOL, source, range_list, period=period, interval=interval, 
                                        scale=scale, prefix_path='./binance_st', saved_to_csv=False)
        if data.df is not None:
            kalman_out = StrategyVar().kalman_strategy_filter(df1=data.df, symbol=data.symbol)
            if kalman_out[7] and kalman_out[8] and kalman_out[11]:
                df_filter_list.append(i)
                bt_plot_indicators(data.df[-24*5:], i)


    
