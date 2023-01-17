import yfinance as yf
import pandas as pd
import requests as r

class asimov_finance: 
    def __init__(self,):
        print("Classe iniciada")
        self.period = 'max'
        '''
        period : str
                Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
                Either Use period parameter or use start and end
        '''
    
    def get_cdi(self) -> pd.DataFrame:
        url = 'https://www.valor.srv.br/indices/cdi.php'
        html = r.get(url).content
        df_list = pd.read_html(html, decimal=',', thousands='.')
        return df_list[0]

    def get_ibovespa(self) -> pd.DataFrame:
        ibovespa = yf.Ticker("^BVSP")
        return ibovespa.history(period='max')
        

        