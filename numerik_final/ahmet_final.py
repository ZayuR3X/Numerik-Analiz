# #----------------------------------------#
# This code is contributed by Ahmet KILIC  #
# #----------------------------------------#

import numpy as np
import matplotlib.pyplot as plt

# van der Pol salınıcısının diferansiyel denklemi
def van_der_pol(t, y, mu):
    # Diferansiyel denklemin sağ tarafını tanımlıyoruz
    dydt = np.zeros(2)
    dydt[0] = y[1]  # y1'in türevi y2'dir
    dydt[1] = mu * (1 - y[0]**2) * y[1] - y[0]  # y2'nin türevi denkleme göre hesaplanır
    return dydt

# Runge-Kutta yöntemi (4. dereceden)
def runge_kutta(f, t0, y0, h, n, mu):
    """
    Runge-Kutta yöntemiyle diferansiyel denklem çözümü.
    Parametreler:
    f  : Çözülecek diferansiyel denklem (fonksiyon)
    t0 : Başlangıç zamanı
    y0 : Başlangıç koşulları (array)
    h  : Adım boyu
    n  : Adım sayısı
    mu : van der Pol denklemi için parametre
    """
    t = t0
    y = y0
    adim = [y0]  # Çözümün başlangıç noktası
    for _ in range(n):
        k1 = f(t, y, mu)
        k2 = f(t + h / 2, y + h * k1 / 2, mu)
        k3 = f(t + h / 2, y + h * k2 / 2, mu)
        k4 = f(t + h, y + h * k3, mu)
        y = y + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6  # Runge-Kutta formülü
        adim.append(y)
        t += h
    return np.array(adim)

h = 0.1   # Adım boyu: Her bir iterasyonda zamanın ne kadar ilerleyeceğini belirler
n = 1000  # Adım sayısı: Çözüm için kaç iterasyon yapılacağını belirler
t0 = 0.0  # Başlangıç zamanı
y0 = np.array([0.01, 0.01])  # Başlangıç koşulları: y1 ve y2'nin başlangıç değerleri

# Farklı mu değerleri için faz diyagramı
mu_degerleri = [0.0, 0.3, 1.0, 3.0]
plt.figure(figsize=(10, 8))

for mu in mu_degerleri:
    adimlar = runge_kutta(van_der_pol, t0, y0, h, n, mu)
    y1 = adimlar[:, 0]  # y1 değerleri
    y2 = adimlar[:, 1]  # y2 değerleri
    plt.plot(y1, y2, label=f"μ = {mu}")

plt.title("Van der Pol Salınıcısı Faz Uzayı")
plt.xlabel("y1")  
plt.ylabel("y2")  
plt.legend()
plt.grid()  
plt.show()