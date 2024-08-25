
import numpy as np
from src.IVCalculator.IVMethods.BlackScholes import black_scholes, vega

import warnings

# Suprimir todos os RuntimeWarnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

def newton_raphson_for_volatility(S, K, T, r, market_price, options_type, initial_guess=0.2, tolerance=1.e-3, max_iterations=1000):
    #Brenner-Subrahmanyam

    sigma = initial_guess
    for i in range(max_iterations):
        price = black_scholes(S, K, T, r, sigma, options_type)
        if price == -1:
            return price
        v = vega(S, K, T, r, sigma)
        price_difference = price - market_price
        if abs(price_difference) < tolerance:
            print('volatilidade: '+ str(sigma))
            return sigma
        sigma_update = price_difference / v
        sigma = max(sigma - sigma_update, 0.0)
    return -1

# # Parâmetros de entrada
# S = 50       # Preço do ativo subjacente
# K = 545      # Preço de exercício
# T = 1         # Tempo até a expiração (em anos)
# r = 0.7974      # Taxa de juros livre de risco 
# market_price = 5  # Preço de mercado da opção

# # # Cálculo da volatilidade implícita
# volatility = newton_raphson_for_volatility(S, K, T, r, market_price , "C")
# print(f"A volatilidade implícita calculada é: {volatility:.4f}")
