import pandas as pd

def calculate_risk(angle, body_part):
    # Açıya göre risk hesaplama
    if body_part == 'waist':  # Bel açısı
        if angle < 30:
            return 'Düşük Risk'
        elif 30 <= angle < 60:
            return 'Orta Risk'
        else:
            return 'Yüksek Risk'
    elif body_part == 'knee':  # Diz açısı
        if 90 <= angle < 120:
            return 'Düşük Risk'
        elif 120 <= angle < 160:
            return 'Orta Risk'
        else:
            return 'Yüksek Risk'
    elif body_part == 'armpit':  # Kol açısı
        if 30 <= angle < 60:
            return 'Düşük Risk'
        elif 60 <= angle < 90:
            return 'Orta Risk'
        else:
            return 'Yüksek Risk'
    return 'Bilinmiyor'

def repeat_risk(repeat_count):
    # Tekrar sayısına göre risk belirleme
    if repeat_count <= 10:
        return 'Düşük Risk'
    elif 10 < repeat_count <= 15:
        return 'Orta Risk'
    else:
        return 'Yüksek Risk'

def count_repeats(angle):
    # Tekrar sayma (100-190 dışında olan açıları sayma)
    if angle < 100 or angle > 190:
        return 1
    return 0

def process_data(input_file, output_file):
    # Veriyi oku
    df = pd.read_excel(input_file)

    # Zamanı 5 saniyelik dilimlere ayırmak
    df['Zaman'] = pd.to_datetime(df['Zaman'])
    df['Zaman Dilimi'] = (df['Zaman'].dt.second // 5) * 5  # 5 saniyelik dilimler

    # Kol, Bel ve Diz açılarına göre risk hesaplaması
    df['Kol Risk'] = df['Kol Açısı'].apply(lambda x: calculate_risk(x, 'armpit'))
    df['Bel Risk'] = df['Bel Açısı'].apply(lambda x: calculate_risk(x, 'waist'))
    df['Diz Risk'] = df['Diz Açısı'].apply(lambda x: calculate_risk(x, 'knee'))

    # Her bölge için tekrar sayısı hesaplama
    df['Kol Tekrar'] = df['Kol Açısı'].apply(count_repeats)
    df['Bel Tekrar'] = df['Bel Açısı'].apply(count_repeats)
    df['Diz Tekrar'] = df['Diz Açısı'].apply(count_repeats)

    # 5 saniyelik dilimlere göre gruplama ve toplam tekrarı hesaplama
    grouped = df.groupby('Zaman Dilimi').agg(
        Kol_Tekrar=('Kol Tekrar', 'sum'),
        Bel_Tekrar=('Bel Tekrar', 'sum'),
        Diz_Tekrar=('Diz Tekrar', 'sum'),
        Kol_Risk=('Kol Risk', 'first'),
        Bel_Risk=('Bel Risk', 'first'),
        Diz_Risk=('Diz Risk', 'first')
    ).reset_index()

    # Her bölge için tekrar riskini belirleme
    grouped['Kol Tekrar Risk'] = grouped['Kol_Tekrar'].apply(repeat_risk)
    grouped['Bel Tekrar Risk'] = grouped['Bel_Tekrar'].apply(repeat_risk)
    grouped['Diz Tekrar Risk'] = grouped['Diz_Tekrar'].apply(repeat_risk)

    # Sonuçları Excel'e yazdırma
    grouped.to_excel(output_file, index=False)

# Dosya isimleri
input_file = 'ergonomi.xlsx'  # Giriş dosyası
output_file = 'sonuc.xlsx'  # Çıktı dosyası (Excel formatında)

# Veriyi işleme
process_data(input_file, output_file)

