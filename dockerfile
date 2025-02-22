# Python 3.9 tabanlı bir Docker imajı kullan
FROM python:3.9

# Çalışma dizinini belirle
WORKDIR /app

# Gerekli dosyaları kopyalıyoruz
COPY src /app/src
COPY requirements.txt /app
COPY main.py /app

# Bağımlılıkları yüklüyoruz
RUN pip install --no-cache-dir -r requirements.txt

# Uygulamayı başlatıyoruz
CMD ["python", "./main.py"]
