"""import pandas as pd

# Puanlama tablosu
risk_puanlama = {
    'Düşük Risk': 1,
    'Orta Risk': 2,
    'Yüksek Risk': 3
}


# Kol, Bel ve Diz bölgesi için puanları hesaplayacak fonksiyon
def calculate_puan(row, body_part):
    # Risk sütunlarını al ve puanla
    risk_column = f'{body_part} _Risk'  # 'Kol Risk', 'Bel Risk', 'Diz Risk'
    repeat_risk_column = f'{body_part} Tekrar Risk'  # 'Kol Tekrar Risk', 'Bel Tekrar Risk', 'Diz Tekrar Risk'

    # Risk puanını ve tekrar risk puanını al
    risk_puan = risk_puanlama.get(row[risk_column], 0)  # Eğer risk durumu yoksa 0 puan
    repeat_risk_puan = risk_puanlama.get(row[repeat_risk_column], 0)

    # İki puanı toplar
    return risk_puan + repeat_risk_puan


def process_data(input_file, output_file):
    # Veriyi oku
    df = pd.read_excel(input_file)

    # Kol, Bel ve Diz bölgesi için puan hesaplama
    df['Kol Puan'] = df.apply(lambda row: calculate_puan(row, 'Kol'), axis=1)
    df['Bel Puan'] = df.apply(lambda row: calculate_puan(row, 'Bel'), axis=1)
    df['Diz Puan'] = df.apply(lambda row: calculate_puan(row, 'Diz'), axis=1)

    # Kol, Bel ve Diz puanlarının toplamını hesapla
    df['Toplam Puan'] = df['Kol Puan'] + df['Bel Puan'] + df['Diz Puan']

    # Sonuçları sadece Zaman Dilimi, Kol Puan, Bel Puan, Diz Puan ve Toplam Puan olarak yazdır
    df_output = df[['Zaman Dilimi', 'Kol Puan', 'Bel Puan', 'Diz Puan', 'Toplam Puan']]

    # Sonuçları yeni Excel dosyasına yazdır
    df_output.to_excel(output_file, index=False)


# Dosya isimleri
input_file = 'sonuc.xlsx'  # Giriş dosyanız (artık 'sonuc' olacak)
output_file = 'puanli_sonuc.xlsx'  # Çıktı dosyası (puanları içeren yeni dosya)

# Veriyi işleme
process_data(input_file, output_file)
"""

import pandas as pd

# Puanlama tablosu
risk_puanlama = {
    'Düşük Risk': 1,
    'Orta Risk': 2,
    'Yüksek Risk': 3
}

# Kol, Bel ve Diz bölgesi için puanları hesaplayacak fonksiyon
def calculate_puan(row, body_part):
    # Risk sütunlarını al ve puanla
    risk_column = f'{body_part}_Risk'  # 'Kol Risk', 'Bel Risk', 'Diz Risk'
    repeat_risk_column = f'{body_part} Tekrar Risk'  # 'Kol Tekrar Risk', 'Bel Tekrar Risk', 'Diz Tekrar Risk'

    # Risk puanını ve tekrar risk puanını al
    risk_puan = risk_puanlama.get(row[risk_column], 0)  # Eğer risk durumu yoksa 0 puan
    repeat_risk_puan = risk_puanlama.get(row[repeat_risk_column], 0)

    # İki puanı toplar
    return risk_puan + repeat_risk_puan

# Toplam puana göre risk durumu belirleyen fonksiyon
def determine_risk(total_puan):
    # 0-12 arası Düşük, 13-16 arası Orta, 17 ve üstü Yüksek risk
    if total_puan <= 12:
        return 'Düşük'
    elif 12 < total_puan <= 16:
        return 'Orta'
    else:
        return 'Yüksek'

def process_data(input_file, output_file):
    # Veriyi oku
    df = pd.read_excel(input_file)

    # Kol, Bel ve Diz bölgesi için puan hesaplama
    df['Kol Puan'] = df.apply(lambda row: calculate_puan(row, 'Kol'), axis=1)
    df['Bel Puan'] = df.apply(lambda row: calculate_puan(row, 'Bel'), axis=1)
    df['Diz Puan'] = df.apply(lambda row: calculate_puan(row, 'Diz'), axis=1)

    # Kol, Bel ve Diz puanlarının toplamını hesapla
    df['Toplam Puan'] = df['Kol Puan'] + df['Bel Puan'] + df['Diz Puan']

    # Toplam puana göre risk durumunu belirleyip yeni bir kolon ekle
    df['Toplam Risk'] = df['Toplam Puan'].apply(determine_risk)

    # Sonuçları sadece Zaman Dilimi, Kol Puan, Bel Puan, Diz Puan, Toplam Puan ve Toplam Risk olarak yazdır
    df_output = df[['Zaman Dilimi', 'Kol Puan', 'Bel Puan', 'Diz Puan', 'Toplam Puan', 'Toplam Risk']]

    # Sonuçları yeni Excel dosyasına yazdır
    df_output.to_excel(output_file, index=False)


# Dosya isimleri
input_file = 'sonuc.xlsx'  # Giriş dosyanız (artık 'sonuc' olacak)
output_file = 'puanli_sonuc.xlsx'  # Çıktı dosyası (puanları içeren yeni dosya)

# Veriyi işleme
process_data(input_file, output_file)
