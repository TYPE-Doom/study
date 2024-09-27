import numpy as np


def T(lac_h, d_h, lac_l, d_l, lac_c, d_c):
    T_h = np.exp(-lac_h * d_h)
    T_l = np.exp(-lac_l * d_l - lac_c * d_c)
    print(T_h, T_l)
    ratio = T_h / T_l
    Subtraction_T = T_h - T_l
    return Subtraction_T, ratio


lac_h = 391.59 / 10        # 高Z滤片的线衰减系数，单位mm
d_h = 0.05             # 高Z滤片的厚度
lac_l = 312.53 / 10        # 低Z滤片的线衰减系数
d_l = 0.06             # 低Z滤片的厚度
lac_c = 23.14 / 10        # 补偿滤片的线衰减系数
d_c = 0.07               # 补偿滤片的厚度
E_l = 20.00             # 低Z的吸收线
E_h = 26.7           # 高Z的吸收线
E = 14.4           # 设定能量值
E_change = E_h - E_l

# 计算残余透过率
residual_transmission = T(lac_h, d_h, lac_l, d_l, lac_c, d_c)[0]
print("{:.2f}".format(E_change))
print(f"Residual Transmission at E = {E} keV: {residual_transmission}")
print(f"The ratio of T_h / T_l is :{T(lac_h, d_h, lac_l, d_l, lac_c, d_c)[1]}")
