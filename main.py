import cv2
import mediapipe as mp
import numpy as np
import os
import pandas as pd
import math
import datetime

"""
def update_excel(file_name, elbow_angle, waist_angle, knee_angle):
    # Eğer dosya yoksa, başlıklarla birlikte oluştur
    if not os.path.exists(file_name):
        data = {
            'Kol Açısı': [],
            'Bel Açısı': [],
            'Diz Açısı': []
        }
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)


    # Mevcut Excel dosyasını sil
    if os.path.exists(file_name):
        os.remove(file_name)

    # Açıları toplamak için bir liste oluştur
    data = {
        'Kol Açısı': [elbow_angle],
        'Bel Açısı': [waist_angle],
        'Diz Açısı': [knee_angle]
    }

    # DataFrame oluştur ve dosyaya yazdır
    df = pd.DataFrame(data)
    df.to_excel(file_name, index=False)"""


def evaluate_risk(angle, body_part):
    """
    Belirli bir açıya göre risk seviyesini döndürür.

    :param angle: İncelenen vücut parçasının açısı
    :param body_part: Değerlendirilen vücut parçası ('waist', 'knee', 'armpit')
    :return: Risk seviyesi ('Düşük Risk', 'Orta Risk', 'Yüksek Risk', 'Bilinmeyen Risk')
    """

    # Bel açısını değerlendirme
    if body_part == 'waist':
        if angle < 30:
            return 'Düşük Risk'
        elif 30 <= angle < 60:
            return 'Orta Risk'
        else:
            return 'Yüksek Risk'

    # Diz açısını değerlendirme
    elif body_part == 'knee':
        if 90 <= angle < 120:
            return 'Düşük Risk'
        elif 120 <= angle < 160:
            return 'Orta Risk'
        else:
            return 'Yüksek Risk'

    # Koltuk altı açısını değerlendirme
    elif body_part == 'armpit':
        if 30 <= angle < 60:
            return 'Düşük Risk'
        elif 60 <= angle < 90:
            return 'Orta Risk'
        else:
            return 'Yüksek Risk'

    # Eğer vücut parçası tanımlı değilse
    return 'Bilinmeyen Risk'

"""
def update_excel(file_name, armpit_angle, waist_angle, knee_angle):
    # Eğer dosya yoksa, başlıklarla birlikte oluştur
    if not os.path.exists(file_name):
        data = {
            'Kol Açısı': [],
            'Bel Açısı': [],
            'Diz Açısı': []
        }
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)

    # Mevcut Excel dosyasını oku
    df = pd.read_excel(file_name)

    # Yeni açılar için bir DataFrame oluştur
    new_data = pd.DataFrame({
        'Kol Açısı': [armpit_angle],
        'Bel Açısı': [waist_angle],
        'Diz Açısı': [knee_angle]
    })

    # Yeni satırı DataFrame'e ekle
    df = pd.concat([df, new_data], ignore_index=True)

    # Güncellenmiş DataFrame'i dosyaya yaz
    df.to_excel(file_name, index=False)

# Kullanım örneği
# update_excel('angles.xlsx', 30, 45, 60)

"""

"""
# Excel dosyasını güncelleme fonksiyonu
def update_excel(file_name, armpit_angle, waist_angle, knee_angle):
    
    Bu fonksiyon, verilen açıları ve bu açıların risk seviyelerini Excel dosyasına ekler.

    :param file_name: Güncellenecek Excel dosyasının adı
    :param armpit_angle: Kol açısı
    :param waist_angle: Bel açısı
    :param knee_angle: Diz açısı
    

    # Eğer belirtilen Excel dosyası yoksa, başlıklarla birlikte yeni bir dosya oluştur
    if not os.path.exists(file_name):
        data = {
            'Kol Açısı': [],  # Kol açısı için boş bir liste oluşturuluyor
            'Bel Açısı': [],  # Bel açısı için boş bir liste oluşturuluyor
            'Diz Açısı': [],  # Diz açısı için boş bir liste oluşturuluyor
            'Kol Risk': [],  # Kol açısı için risk seviyeleri için boş bir liste oluşturuluyor
            'Bel Risk': [],  # Bel açısı için risk seviyeleri için boş bir liste oluşturuluyor
            'Diz Risk': []  # Diz açısı için risk seviyeleri için boş bir liste oluşturuluyor
        }
        # DataFrame oluşturuluyor ve belirtilen dosyaya kaydediliyor
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)

    # Mevcut Excel dosyasını oku
    df = pd.read_excel(file_name)

    # Verilen açıların risk seviyelerini hesapla
    armpit_risk = evaluate_risk(armpit_angle, 'armpit')  # Kol açısı için risk hesaplanıyor
    waist_risk = evaluate_risk(waist_angle, 'waist')  # Bel açısı için risk hesaplanıyor
    knee_risk = evaluate_risk(knee_angle, 'knee')  # Diz açısı için risk hesaplanıyor

    # Yeni açılar ve risk seviyeleri için bir DataFrame oluşturuluyor
    new_data = pd.DataFrame({
        'Kol Açısı': [armpit_angle],  # Kol açısı yeni veriye ekleniyor
        'Bel Açısı': [waist_angle],  # Bel açısı yeni veriye ekleniyor
        'Diz Açısı': [knee_angle],  # Diz açısı yeni veriye ekleniyor
        'Kol Risk': [armpit_risk],  # Kol açısının risk seviyesi yeni veriye ekleniyor
        'Bel Risk': [waist_risk],  # Bel açısının risk seviyesi yeni veriye ekleniyor
        'Diz Risk': [knee_risk]  # Diz açısının risk seviyesi yeni veriye ekleniyor
    })

    # Yeni veriyi mevcut DataFrame'e ekle
    df = pd.concat([df, new_data], ignore_index=True)

    # Güncellenmiş DataFrame'i belirtilen dosyaya kaydet
    df.to_excel(file_name, index=False)

"""

def update_excel(file_name, armpit_angle, waist_angle, knee_angle):
    """
    Bu fonksiyon, verilen açıları ve bu açıların risk seviyelerini Excel dosyasına ekler.
    Ayrıca her kayda zaman bilgisini de ekler.

    :param file_name: Güncellenecek Excel dosyasının adı
    :param armpit_angle: Kol açısı
    :param waist_angle: Bel açısı
    :param knee_angle: Diz açısı
    """

    # Eğer belirtilen Excel dosyası yoksa, başlıklarla birlikte yeni bir dosya oluştur
    if not os.path.exists(file_name):
        data = {
            'Zaman': [],  # Zaman bilgisini ekliyoruz
            'Kol Açısı': [],  # Kol açısı için boş bir liste oluşturuluyor
            'Bel Açısı': [],  # Bel açısı için boş bir liste oluşturuluyor
            'Diz Açısı': [],  # Diz açısı için boş bir liste oluşturuluyor
            'Kol Risk': [],  # Kol açısı için risk seviyeleri için boş bir liste oluşturuluyor
            'Bel Risk': [],  # Bel açısı için risk seviyeleri için boş bir liste oluşturuluyor
            'Diz Risk': []  # Diz açısı için risk seviyeleri için boş bir liste oluşturuluyor
        }
        # DataFrame oluşturuluyor ve belirtilen dosyaya kaydediliyor
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)

    # Mevcut Excel dosyasını oku
    df = pd.read_excel(file_name)

    # Verilen açıların risk seviyelerini hesapla
    armpit_risk = evaluate_risk(armpit_angle, 'armpit')  # Kol açısı için risk hesaplanıyor
    waist_risk = evaluate_risk(waist_angle, 'waist')  # Bel açısı için risk hesaplanıyor
    knee_risk = evaluate_risk(knee_angle, 'knee')  # Diz açısı için risk hesaplanıyor

    # Zaman bilgisini al
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Yeni açılar, risk seviyeleri ve zaman bilgisini içeren bir DataFrame oluşturuluyor
    new_data = pd.DataFrame({
        'Zaman': [current_time],  # Zaman bilgisini yeni veriye ekliyoruz
        'Kol Açısı': [armpit_angle],  # Kol açısı yeni veriye ekleniyor
        'Bel Açısı': [waist_angle],  # Bel açısı yeni veriye ekleniyor
        'Diz Açısı': [knee_angle],  # Diz açısı yeni veriye ekleniyor
        'Kol Risk': [armpit_risk],  # Kol açısının risk seviyesi yeni veriye ekleniyor
        'Bel Risk': [waist_risk],  # Bel açısının risk seviyesi yeni veriye ekleniyor
        'Diz Risk': [knee_risk]  # Diz açısının risk seviyesi yeni veriye ekleniyor
    })

    # Yeni veriyi mevcut DataFrame'e ekle
    df = pd.concat([df, new_data], ignore_index=True)

    # Güncellenmiş DataFrame'i belirtilen dosyaya kaydet
    df.to_excel(file_name, index=False)


# Kullanım örneği
# update_excel('angles.xlsx', 30, 45, 60)


# Poz tahmini için MediaPipe kurulumları
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose


# Açı hesaplama fonksiyonu
def calculate_angle(a, b, c):
    a = np.array(a)  # İlk nokta
    b = np.array(b)  # Orta nokta (açı burada hesaplanacak)
    c = np.array(c)  # Son nokta

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180.0:
        angle = 360 - angle

    return angle


excel_file = 'ergonomi.xlsx'

# Webcam'i açalım
cap = cv2.VideoCapture(0)

# Kameranın çözünürlüğünü almak için:
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # Kameranın genişliği
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # Kameranın yüksekliği

# Pose modülüyle poz tespiti
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    # Biceps curl sayısını takip eden değişkenler
    count = 0
    direction = 0

    while cap.isOpened():
        ret, frame = cap.read()

        # Görüntüyü işleme
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        # Poz tahmini yapalım
        results = pose.process(image)

        # Görüntüyü geri BGR'ye çevir
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Poz tahmini sonuçlarını alalım
        try:
            landmarks = results.pose_landmarks.landmark

            """# Sağ kol için eklem noktalarını belirleyelim
            shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                        landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
            elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                     landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
            wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                     landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]

            # Açıyı hesaplayalım
            angle = calculate_angle(shoulder, elbow, wrist)

            # Açıyı ekrana yazalım
            cv2.putText(image, str(int(angle)),
                        tuple(np.multiply(elbow, [width, height]).astype(int)),  # width ve height kullanımı
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA
                        )
            """
            # Sağ kol için eklem noktalarını alalım (omuz, dirsek, kalça)
            shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                        landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
            elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                     landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
            hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                   landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]

            # Koltuk altı açısını hesapla
            armpit_angle = calculate_angle(hip, shoulder, elbow)

            # Açıyı ekrana yazdır
            cv2.putText(image, str(int(armpit_angle)),
                        tuple(np.multiply(shoulder, [width, height]).astype(int)),  # width ve height
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA
                        )

            # Sağ diz için eklem noktalarını belirleyelim
            hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                   landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
            knee = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,
                    landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
            ankle = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,
                     landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]

            # Diz açısını hesaplayalım
            knee_angle = calculate_angle(hip, knee, ankle)

            # Diz açısını ekrana yazalım
            cv2.putText(image, str(int(knee_angle)),
                        tuple(np.multiply(knee, [width, height]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA
                        )

            # Sağ bel açısını hesaplamak için eklem noktalarını belirleyelim
            shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                        landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
            hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                   landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
            knee = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,
                    landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]

            # Bel açısını hesaplayalım
            waist_angle = calculate_angle(shoulder, hip, knee)

            # Bel açısını ekrana yazalım
            cv2.putText(image, str(int(waist_angle)),
                        tuple(np.multiply(hip, [width, height]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA
                        )

            # Risk seviyelerini belirle ve ekrana yazdır
            waist_risk = evaluate_risk(waist_angle, 'waist')
            knee_risk = evaluate_risk(knee_angle, 'knee')
            armpit_risk = evaluate_risk(armpit_angle, 'armpit')

            # Ekrana yazdır
            cv2.putText(image, f'Waist Risk: {waist_risk}',
                        tuple(np.multiply(hip, [width, height]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

            cv2.putText(image, f'Knee Risk: {knee_risk}',
                        tuple(np.multiply(knee, [width, height]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

            cv2.putText(image, f'Armpit Risk: {armpit_risk}',
                        tuple(np.multiply(elbow, [width, height]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

            """           
            # Biceps curl hareketini sayma mantığı
            if angle > 160:
                direction = 0
            if angle < 30 and direction == 0:
                count += 1
                direction = 1

            # Curl sayısını ekrana yazalım
            cv2.putText(image, 'Reps: ' + str(count),
                        (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA
                        )
            """

            update_excel(excel_file, armpit_angle, waist_angle, knee_angle)

        except Exception as e:
            print("Error:", e)

        except:
            pass

        # Poz çizimlerini görüntüye yerleştirelim
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                  mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                                  )

        # Sonucu göster
        cv2.imshow('AI Trainer', image)

        # Çıkış için 'q' tuşuna basabilirsiniz
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()