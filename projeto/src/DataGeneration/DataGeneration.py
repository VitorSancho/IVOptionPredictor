import itertools
import pandas as pd
import numpy as np


maturities = [round(x, 1) for x in list(np.arange(0.2, 1, 0.1))]
spots = [round(x, 1) for x in list(np.arange(17.5, 27.5, 0.25))]
taxadesconto =  [round(x, 3) for x in list(np.arange(0.08, 0.1, 0.005))] 
premios = [round(x, 2) for x in list(np.arange(1, 6, 0.25))]
strikes = [round(x, 1) for x in list(np.arange(20, 25, 0.1))]
call_or_put = ['call','put']

combinations = itertools.product(strikes, maturities, spots, taxadesconto, premios, call_or_put)

df = pd.DataFrame(combinations, columns=['Strike', 'Maturity', 'Spot', 'TaxaDesconto', 'Premio',"CallPut"])

df.to_csv(f'base_de_dados_4.csv')
