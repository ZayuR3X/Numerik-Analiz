import numpy as np
import pandas as pd  # Tabloyu kolayca gösterebilmek için

def richardson_extrapolation(f, x, h, m, n):
    # f: türevini hesaplayacağımız fonksiyon
    # x: türevini hesaplamak istediğimiz nokta
    # h: başlangıç adım boyutu
    # m: adım sayısı
    # n: ekstrapolasyon seviyesi (daha hassas sonuç için)

    # Richardson tablosu için boş bir matris oluşturuyoruz
    R = np.zeros((m, n))

    # İlk adımda merkezi fark yaklaşımını kullanarak türev hesaplanır
    for i in range(m):
        h_i = h / (2 ** i)
        R[i, 0] = (f(x + h_i) - f(x - h_i)) / (2 * h_i)

    # Ekstrapolasyon işlemi Richardson tablosunda yapılır
    for j in range(1, n):
        for i in range(m - j):
            R[i, j] = (4 ** j * R[i + 1, j - 1] - R[i, j - 1]) / (4 ** j - 1)

    # Tabloyu göstermek için DataFrame oluştur
    df = pd.DataFrame(R, columns=[f'Level {i}' for i in range(1, n+1)])
    
    return df

# Kullanım örneği
def f(x):
    return np.sin(x)

x = np.pi / 4  # Türevini hesaplamak istediğimiz nokta (pi/4)
h = 0.1        # Başlangıç adım boyutu
m = 5          # Adım sayısı
n = 3          # Ekstrapolasyon seviyesi

# Türev hesaplama ve tabloyu yazdırma
df = richardson_extrapolation(f, x, h, m, n)
print(df)
