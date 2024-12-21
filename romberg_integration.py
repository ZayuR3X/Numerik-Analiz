import numpy as np

LIMIT = 10

def F(x):
    return np.exp(-x**2)

# Kullanıcıdan entegral sınırlarını ve Romberg tablosu satır sayısını alalım
A, B = map(float, input("INTEGRAL SINIRLARI? (A B): ").split())
NROWS = int(input("ROMBERG INTEGRASYONU KAC SATIR? "))

DELX = B - A
ROM = np.zeros((LIMIT, LIMIT), dtype=float)  # Romberg tablosunu oluştur
ROM[0, 0] = DELX / 2.0 * (F(A) + F(B))       # İlk trapez kuralı hesaplaması
NSUBS = 1

# İlk sonucu yazdır
print(f"{NSUBS:4d} {ROM[0, 0]:10.6f}")

# Romberg entegrasyonunu gerçekleştiren döngü
for N in range(1, NROWS):
    NSUBS *= 2
    DELX /= 2.0
    TSUM = 0.0
    
    # Trapez kuralı ile ara noktaların toplamını hesapla
    for K in range(1, NSUBS, 2):
        TSUM += F(A + K * DELX)
    
    ROM[N, 0] = ROM[N-1, 0] / 2.0 + DELX * TSUM
    
    # Romberg tablosunun daha yüksek dereceli elemanlarını hesapla
    for K in range(1, N + 1):
        ROM[N, K] = ROM[N, K-1] + (ROM[N, K-1] - ROM[N-1, K-1]) / (4**K - 1)
    
    # Sonuçları yazdır
    print(f"{NSUBS:4d} " + " ".join(f"{ROM[N, K]:10.6f}" for K in range(0, N + 1)))
