import pandas as pd
import numpy as np
from scipy.stats import ttest_ind
from scipy.stats import permutation_test

chat_id = 326525586 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    p_value = permutation_test((x, y), lambda x, y, axis: np.mean(x, axis=axis) - np.mean(y, axis=axis),
                                            vectorized=True,
                                            n_resamples=5000).pvalue
    alpha = 0.07
    return p_value < alpha # Ваш ответ, True или False
