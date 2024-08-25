import itertools
import pandas as pd
import numpy as np


strikes = [round(x, 1) for x in list(np.arange(4, 5, 0.1))]
maturities = [round(x, 1) for x in list(np.arange(0.3, 1, 0.1))]
spots = [round(x, 1) for x in list(np.arange(3.5, 5.5, 0.25))]
taxadesconto =  [round(x, 3) for x in list(np.arange(0.08, 0.1, 0.005))] 
premios = [round(x, 2) for x in list(np.arange(2, 5, 0.25))]
call_or_put = ['call','put']

combinations = itertools.product(strikes, maturities, spots, taxadesconto, premios, call_or_put)

df = pd.DataFrame(combinations, columns=['Strike', 'Maturity', 'Spot', 'TaxaDesconto', 'Premio',"CallPut"])

df.to_csv(f'base_de_dados.csv')
