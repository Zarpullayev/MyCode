import os
import platform
import uuid
import socket
import hashlib

# 📌 **1️⃣ Qurilmaning noyob Device ID sini yaratish**
def get_device_id():
    system_name = platform.system()  # Windows, Linux, macOS
    node_name = platform.node()  # Qurilma nomi
    mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xFF) for elements in range(0, 2*6, 8)][::-1])  # MAC Address
    hostname = socket.gethostname()  # Kompyuter nomi
    
    # Barcha ma'lumotlarni birlashtirib, xesh orqali noyob Device ID yaratamiz
    raw_id = f"{system_name}-{node_name}-{mac_address}-{hostname}"
    device_id = hashlib.sha256(raw_id.encode()).hexdigest()  # Xavfsiz xesh qilish

    return device_id

# 📌 **2️⃣ Qurilma ID ni olish va ekranga chiqarish**
current_device = get_device_id()
print(f"🖥 Qurilma ID: {current_device}")

# 📌 **3️⃣ GitHub Secrets'dan DEVICE_ID ni olish**
allowed_device = os.getenv("DEVICE_ID")

# 📌 **4️⃣ Qurilma ID ni tekshirish**
if allowed_device is None:
    print("❌ Ruxsat yo'q: GitHub Secrets'da DEVICE_ID topilmadi!")
    exit()

if current_device != allowed_device:
    print("❌ Ruxsat yo'q: Noto'g'ri qurilma!")
    exit()

print("✅ Ruxsat berildi! Kod ishga tushmoqda...")

# 📌 **5️⃣ Asosiy kod (faqat ruxsat berilgan qurilmalarda ishlaydi)**
print("🚀 Telegram bot ishlayapti...")
