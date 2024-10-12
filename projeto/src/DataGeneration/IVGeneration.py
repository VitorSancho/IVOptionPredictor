import numpy as np
from scipy.stats import norm
import sys
import os
from joblib import Parallel, delayed


# Adicione o diretório raiz do projeto ao sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(project_root)

from src.IVCalculator.IterativeMethods.NewtonRaphson import newton_raphson_for_volatility


import pandas as pd
import numpy as np


def calculate_volatility(row):
    S = row['Spot']
    K = row['Strike']
    T = row['Maturity']
    r = row['TaxaDesconto']
    market_price = row['Premio']
    call_or_put = row['CallPut']
    
    vol = newton_raphson_for_volatility(S, K, T, r, market_price, call_or_put)
    
    if ( vol != -1 and vol < 100):        
        print(f"############################# {row.name} volatilidade {vol}")


    print(f"row {row.name}")

    return vol

strikes = [5,10,15,20]

for strike in strikes:

    # Carregar o DataFrame do arquivo CSV
    strike2 = strike + 5
    path = f'D:\\CEDERJ\\2024.2\\tcc\\IVOptionPredictor\\projeto\\data\\iniciais\\novos_premios\\strike_strike1astrike2'
    path_ajustado = path.replace("strike1",str(strike))
    path_ajustado = path_ajustado.replace("strike2",str(strike2))
    df = pd.read_csv(path_ajustado + '\\strike_' + str(strike) + 'a' + str(strike2) + '.csv')

    # Paralelizar o cálculo da volatilidade
    volatility_list = Parallel(n_jobs=-1)(delayed(calculate_volatility)(row) for _, row in df.iterrows())

    # Adicionar a coluna de volatilidade ao DataFrame
    voldf = pd.DataFrame(volatility_list)

    # Salvar o DataFrame com a volatilidade no arquivo CSV
    voldf.to_csv(path_ajustado + '\\result.csv', index=True)
