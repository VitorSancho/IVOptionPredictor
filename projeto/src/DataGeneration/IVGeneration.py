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

# Carregar o DataFrame do arquivo CSV
df = pd.read_csv('D:\\CEDERJ\\2024.2\\tcc\\IVOptionPredictor\\projeto\\data\\iniciais\\base_de_dados.csv')

# Paralelizar o cálculo da volatilidade
volatility_list = Parallel(n_jobs=4)(delayed(calculate_volatility)(row) for _, row in df.iterrows())

# Adicionar a coluna de volatilidade ao DataFrame
voldf = pd.DataFrame(volatility_list)

# Salvar o DataFrame com a volatilidade no arquivo CSV
output_path = 'D:\\CEDERJ\\2024.2\\tcc\\IVOptionPredictor\\projeto\\data\\iniciais\\result.csv'
voldf.to_csv(output_path, index=True)
