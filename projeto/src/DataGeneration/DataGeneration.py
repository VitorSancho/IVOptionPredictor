import itertools
import pandas as pd
import numpy as np

strike1 = 10
strike2 = 15

maturities = [round(x, 1) for x in list(np.arange(0.1, 0.4, 0.1))]
spots = [round(x, 1) for x in list(np.arange(strike1 - strike1*0.15, strike2 + strike2*0.12, 0.25))]
taxadesconto =  [round(x, 3) for x in list(np.arange(0.09, 0.11, 0.01))] 
premios = [round(x, 2) for x in list(np.arange(0.05, 1.2, 0.05))]
strikes = [round(x, 1) for x in list(np.arange(strike1, strike2, 0.1))]
call_or_put = ['call','put']

combinations = itertools.product(strikes, maturities, spots, taxadesconto, premios, call_or_put)

df = pd.DataFrame(combinations, columns=['Strike', 'Maturity', 'Spot', 'TaxaDesconto', 'Premio',"CallPut"])

path = f'D:\\CEDERJ\\2024.2\\tcc\\IVOptionPredictor\\projeto\\data\\iniciais\\novos_premios\\strike_strike1astrike2\\strike_strike1astrike2.csv'
path_ajustado = path.replace("strike1",str(strike1))
path_ajustado = path_ajustado.replace("strike2",str(strike2))
df.to_csv(path_ajustado)
