import numpy as np

# def f_R(lac_h, d_h, lac_l, d_l, lac_c, d_c):
#     return np.exp(-lac_h * d_h) - np.exp(-lac_l * d_l - lac_c * d_c)
#
#
# def compute_integral(func, a, b):
#     result = quad(func, a, b)
#     return list[result][0]

# def calculate_flatness(R, E_l, E_h):
#     delta_R = np.sqrt(np.sum((R - np.mean(R))**2) / (E_h - E_l))
#     R_bar = np.mean(R)
#     eta = delta_R / R_bar
#     return eta


def T(lac_h, d_h, lac_l, d_l, lac_c, d_c):
    T_h = np.exp(-lac_h * d_h)
    T_l = np.exp(-lac_l * d_l - lac_c * d_c)
    print(T_h, T_l)
    ratio = T_h / T_l
    Subtraction_T = T_h - T_l
    return Subtraction_T, ratio


lac_h = 141.62 / 10     # 高Z滤片的线衰减系数，单位mm
d_h = 0.03               # 高Z滤片的厚度
lac_l = 52.174 / 10     # 低Z滤片的线衰减系数
d_l = 0.15              # 低Z滤片的厚度
lac_c = 0.61118 / 10     # 补偿滤片的线衰减系数
d_c = 0.2              # 补偿滤片的厚度
E_l = 46.8               # 低Z的吸收线
E_h = 67.4               # 高Z的吸收线
E = 76.4                 # 设定能量值
E_change = E_h - E_l

# 计算残余透过率
residual_transmission = T(lac_h, d_h, lac_l, d_l, lac_c, d_c)[0]
print("{:.2f}".format(E_change))
print(f"Residual Transmission at E = {E} keV: {residual_transmission}")
print(f"The ratio of T_h / T_l is :{T(lac_h, d_h, lac_l, d_l, lac_c, d_c)[1]}")
