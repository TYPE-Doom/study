"""
假设S(E)在探测范围内稳定，数值为一
那么只需要计算穿透T也就是残余响应R的积分相关即可
"""
import numpy as np
from scipy.integrate import quad


# def compute_integral(func, a, b):   # 积分
#     result = quad(func, a, b)[0]
#     error = quad(func, a, b)[1]
#     return result, error


def T(lac_h, d_h, lac_l, d_l, lac_c, d_c):
    T_h = np.exp(-lac_h * d_h)
    T_l = np.exp(-lac_l * d_l - lac_c * d_c)
    print(T_h, T_l)
    ratio = T_h / T_l
    Subtraction_T = T_h - T_l
    return Subtraction_T, ratio


lac_h = 87.808 / 10     # 高Z滤片的线衰减系数，单位mm
d_h = 0.02               # 高Z滤片的厚度
lac_l = 124.59 / 10     # 低Z滤片的线衰减系数
d_l = 0.15              # 低Z滤片的厚度
lac_c = 0.95261 / 10     # 补偿滤片的线衰减系数
d_c = 0.75              # 补偿滤片的厚度
E_l = 46.8               # 低Z的吸收线
E_h = 67.4               # 高Z的吸收线
E = 51.2                 # 设定能量值
E_change = E_h - E_l

# 计算残余透过率
residual_transmission = T(lac_h, d_h, lac_l, d_l, lac_c, d_c)[0]
print("{:.2f}".format(E_change))
print(f"Residual Transmission at E = {E} keV: {residual_transmission}")
print(f"The ratio of T_h / T_l is :{T(lac_h, d_h, lac_l, d_l, lac_c, d_c)[1]}")
