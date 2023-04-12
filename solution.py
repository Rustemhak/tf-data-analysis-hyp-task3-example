import pandas as pd
import numpy as np
from scipy.stats import ttest_ind
from scipy.stats import permutation_test

chat_id = 326525586 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
     _, p_value = ttest_ind(x, y, equal_var=False, permutations=5000, alternative='less')
    alpha = 0.07
    return p_value < alpha
